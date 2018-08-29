import pygame
import math
import copy

# from roadwatcher import RoadWatcher
# from mycode import road_watcher

class Body(pygame.sprite.Sprite):
    def __init__(self, dest, road_watcher, color=(23,179,73)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10, 10])
        self.image.fill(color)
        self.rect = self.image.get_rect()

        posX = dest[0].getP1X()
        posY = dest[0].getP1Y()

        self.rect.center = [posX,posY]
        self.obj_x = posX
        self.obj_y = posY

        # control motion here
        self.speed = 0
        self.dt = 1        
        self.acc = 1.1

        self.angle = 0
        self.road_watcher = road_watcher

        self.should_kill = False
        
        self.dest = copy.copy(dest)
        self.dest_counter = 0
        self.lencheck = len(self.dest)

        # signal counters
        self.s_count = 0
        self.s_max_count = 0
        self.s_road_list = []

        self.sig_list = []
        self.makeSigList()

    def update(self):

        if self.dest_counter < self.lencheck:

            # check if destination is a road or a signal
            # destination = [r1,r2,[s1,"03"],r4]
            proceed = False
            try:
                v = self.dest[self.dest_counter][1]
                proceed = True
            except Exception as e:
                pass

            if proceed:
                # destination-single is a signal                
                
                # get route
                '''
                routes are assigned clockwise
                    0
                  +--+
                3 |  | 1
                  +--+
                    4                
                '''
                signal = self.dest[self.dest_counter][0]
                signal_route = self.dest[self.dest_counter][1]

                # get max count
                # get sroadlist
                if self.s_max_count == 0:
                    self.s_max_count = signal.getMaxS_Count(signal_route)
                    self.s_road_list = signal.getSRoadList(signal_route)
                    # print(self.s_max_count)

                # check cur count
                if self.s_count < self.s_max_count:                
                    # same as road
                    s_road = self.s_road_list[self.s_count]

                    target_x = s_road.getP2X()
                    target_y = s_road.getP2Y()
                                        
                    self.angle = s_road.getAngle()                                

                    dir_x = math.cos(math.radians(self.angle))
                    dir_y = math.sin(math.radians(self.angle))                    
                
                    checkx = math.fabs(self.obj_x - target_x)
                    checkx = round(checkx, 2)

                    checky = math.fabs(self.obj_y - target_y)
                    checky = round(checky, 2)
                    # print("target_x{} target_y{} dir_x{} dir_y{} checkx{} checky{}".format(target_x,target_y,dir_x,dir_y,checkx, checky))                    
                    # print(checky)
                    # print(self.angle)


                    # THIS NEEDS TO BE REFACTORED
                    # HORRIBLE CODE
                    if (self.angle == 0) or (self.angle == 180):

                        if( checkx > 1.0):
                            self.motionAction(dir_x, dir_y)
                        else:                            
                            self.s_count += 1

                    elif (self.angle == 90) or (self.angle == -90):

                        if( checky > 1.0):
                            self.motionAction(dir_x, dir_y)
                        else:
                            self.s_count += 1

                else:
                    # print("into else")
                    # quit()
                    # reassign counters
                    self.s_max_count = 0
                    self.dest_counter += 1


            else:
                # destination-single is a road
                road = self.dest[self.dest_counter]

                # we need to know where this car is
                # add to road watcher
                self.road_watcher.addToCarList(self, road)
                
                target_x = road.getP2X()
                target_y = road.getP2Y()

                self.angle = road.getAngle()

                dir_x = math.cos(math.radians(self.angle))
                dir_y = math.sin(math.radians(self.angle))
            
                checkx = math.fabs(self.obj_x - target_x)
                checkx = round(checkx, 2)

                checky = math.fabs(self.obj_y - target_y)
                checky = round(checky, 2)
                # print(checky)
                # if( checkx > 0.1) and ( checkx != self.last_valx):

                 # THIS NEEDS TO BE REFACTORED
                # HORRIBLE CODE
                if (self.angle == 0) or (self.angle == 180):

                    if( checkx > 1.0):
                        self.motionAction(dir_x, dir_y)
                    else:
                        self.dest_counter += 1

                elif (self.angle == 90) or (self.angle == -90):

                    if( checky > 1.0):
                        self.motionAction(dir_x, dir_y)
                    else:
                        self.dest_counter += 1                

        else:
            # allow car to be killed
            self.should_kill = True
            self.road_watcher.removeFromCarList(self)
            # pass


    # get position
    # topleft, bottomleft, topright, bottomright
    def getTopRight(self):
        return self.rect.topright

    def getTopLeft(self):
        return self.rect.topleft

    def getBottomRight(self):
        return self.rect.bottomright
        
    def getBottomLeft(self):
        return self.rect.bottomleft 



    def getAngle(self):
        return self.angle

    def setAcc(self, acc):
        self.acc = acc   

    def setColor(self, color):
        self.image.fill(color)

    # private functions
    def motionAction(self, dir_x, dir_y):
        self.obj_x += self.acc * dir_x * self.dt
        self.obj_y += self.acc * dir_y * self.dt
        
        self.rect.center = [self.obj_x, self.obj_y]
        self.image = pygame.transform.rotate(self.image, self.angle)

    def makeSigList(self):
        for idx, road in enumerate(self.dest):
            try:
                signal = self.dest[idx][0]
                signal_route = self.dest[idx][1]
                # print(signal)
                # print(signal_route)
                self.sig_list.append([signal, signal_route])
            except Exception as e:
                # print(e)
                pass

    def getSigList(self):
        print(self.sig_list)


    def canGo(self, signal):
        for s in self.sig_list:
            if signal == s[0]:
                # print(s[1])
                # [s1,'03'] --> 0
                # [s3,'23'] --> 2
                # [s3,'12'] --> 1
                k = int(s[1][:1])
                return signal.getBoolAtIndex(k)
        return False
    

    def shouldKill(self):
        return self.should_kill
