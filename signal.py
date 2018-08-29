import pygame

class Signal(pygame.sprite.Sprite):
    def __init__(self, pos, color=(73,73,73)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([60, 60])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        
        self.rect.topleft = pos
        self.sr_list = []
        self.time_list = []
        self.bool_list = []
        self.bool_counter = 0
        self.max_bool_counter = 0
        self.prev_time = 0
        self.list_length = 0


    def addSRoad(self, s_road):
    	self.sr_list.append(s_road)


    def getTopLeft(self):
    	return self.rect.topleft

    def getTopRight(self):
    	return self.rect.topright

    def getBottomLeft(self):
    	return self.rect.bottomleft

    def getBottomRight(self):
    	return self.rect.bottomright

    def getBottomRight(self):
        return self.rect.bottomright

    def setColor(self, color):
        self.image.fill(color)

    # get amount of sroads for a signal route
    def getMaxS_Count(self, signal_route):
        count = 0
        for s_road in self.sr_list:            
            if signal_route == s_road.getName():
                count += 1
        return count

    def getSRoadList(self, signal_route):
        retList = []
        for s_road in self.sr_list:            
            if signal_route == s_road.getName():
                retList.append(s_road)
        return retList



    def setTime(self, time):
        self.prev_time = time

    def addTimeList(self, list1):
        self.time_list = list1
        self.list_length = len(list1)
        self.bool_list = [False] * self.list_length
        self.bool_list[0] = True
        self.max_bool_counter = self.list_length - 1
        print(self.time_list)
        print(self.bool_list)


    def updateBoolArray(self, now):
        
        diff = (now - self.prev_time) / 1000

        t = self.time_list[self.bool_counter]
        if diff > t:
            # reset prev time
            self.prev_time = now

            # reset the counter after max
            if self.bool_counter < self.max_bool_counter:
                self.bool_counter += 1
            else:
                self.bool_counter = 0

            # make all bool elems False
            self.bool_list = [False] * self.list_length
            # change the bool value
            self.bool_list[self.bool_counter] = True

            # debug
            print("{} passed".format(t))
            print(self.bool_list)


    def getBoolAtIndex(self, key):
        return self.bool_list[key]



