'''
main.py

'''


import pygame
import math
import copy
from road import Road
from roadwatcher import RoadWatcher
from body import Body
from near import Near
from far import Far
from cargroup import CarGroup
from carsingle import CarSingle
from signal import Signal
from s_road import S_Road

import os
# clear = lambda: os.system('cls')


# init
pygame.init()
# display
screen = pygame.display.set_mode((800,600))
# window title
pygame.display.set_caption('SpiderWeb')
# clock
clock = pygame.time.Clock()
fps = 60
# game logic
crashed = False


# points
# --------------------------
# r1
p1 = [240.0,60.0]
p2 = [240.0,150.0]
# r2
p3 = [240.0,210.0]
p4 = [240.0,400.0]
# r3
p5 = [240.0,460.0]
p6 = [240.0,540.0]

# r4
p7 = [540.0,60.0]
p8 = [540.0,150.0]
# r5
p9 = [540.0,210.0]
p10 = [540.0,400.0]
# r6
p11 = [540.0,460.0]
p12 = [540.0,540.0]
# --------------------------
# r7
p13 = [220.0,540.0]
p14 = [220.0,460.0]
# r8
p15 = [220.0,400.0]
p16 = [220.0,210.0]
# r9
p17 = [220.0,150.0]
p18 = [220.0,60.0]


# r10
p19 = [520.0,540.0]
p20 = [520.0,460.0]
# r11
p21 = [520.0,400.0]
p22 = [520.0,210.0]
# r12
p23 = [520.0,150.0]
p24 = [520.0,60.0]
# --------------------------
# r13
p25 = [100,170]
p26 = [200,170]
# r14
p27 = [260,170]
p28 = [500,170]
# r15
p29 = [560,170]
p30 = [650,170]

# r16
p31 = [100,420]
p32 = [200,420]
# r17
p33 = [260,420]
p34 = [500,420]
# r18
p35 = [560,420]
p36 = [650,420]

# --------------------------
# r19
p37 = [650,190]
p38 = [560,190]
# r20
p39 = [500,190]
p40 = [260,190]
# 21
p41 = [200,190]
p42 = [100,190]


# 22
p43 = [650,440]
p44 = [560,440]
# 23
p45 = [500,440]
p46 = [260,440]
# 24
p47 = [200,440]
p48 = [100,440]
# --------------------------



# colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
cyan = (66, 244, 176)
bg_grey = (35,35,35)
sig_grey = ()
road_grey = ()
green = ()

# make roads
# --------------------------
r1 = Road(p1,p2,90,"r1")
r2 = Road(p3,p4,90,"r2")
r3 = Road(p5,p6,90,"r3")

r4 = Road(p7,p8,90,"r4")
r5 = Road(p9,p10,90,"r5")
r6 = Road(p11,p12,90,"r6")
# --------------------------
r7 = Road(p13,p14,-90,"r7")
r8 = Road(p15,p16,-90,"r8")
r9 = Road(p17,p18,-90,"r9")

r10 = Road(p19,p20,-90,"r10")
r11 = Road(p21,p22,-90,"r11")
r12 = Road(p23,p24,-90,"r12")
# --------------------------
r13 = Road(p25,p26,0,"r13")
r14 = Road(p27,p28,0,"r14")
r15 = Road(p29,p30,0,"r15")

r16 = Road(p31,p32,0,"r16")
r17 = Road(p33,p34,0,"r17")
r18 = Road(p35,p36,0,"r18")
# --------------------------
r19 = Road(p37,p38,180,"r19")
r20 = Road(p39,p40,180,"r20")
r21 = Road(p41,p42,180,"r21")

r22 = Road(p43,p44,180,"r22")
r23 = Road(p45,p46,180,"r23")
r24 = Road(p47,p48,180,"r24")
# --------------------------

# road watcher 
# watches roads
road_watcher = RoadWatcher(screen)
road_watcher.add(r1)
road_watcher.add(r2)
road_watcher.add(r3)

road_watcher.add(r4)
road_watcher.add(r5)
road_watcher.add(r6)
# --------------------------
road_watcher.add(r7)
road_watcher.add(r8)
road_watcher.add(r9)

road_watcher.add(r10)
road_watcher.add(r11)
road_watcher.add(r12)
# --------------------------
road_watcher.add(r13)
road_watcher.add(r14)
road_watcher.add(r15)

road_watcher.add(r16)
road_watcher.add(r17)
road_watcher.add(r18)
# --------------------------
road_watcher.add(r19)
road_watcher.add(r20)
road_watcher.add(r21)

road_watcher.add(r22)
road_watcher.add(r23)
road_watcher.add(r24)
# --------------------------

# pass time to each signal
now = pygame.time.get_ticks()

s_group = pygame.sprite.Group()
sig1 = Signal([200,150])
sig1.addTimeList([10,8,6,5])
sig1.setTime(now)
# print(sig1.getTopRight())
# quit()

# create signals 
sig2 = Signal([500,150])
sig3 = Signal([200,400])
sig4 = Signal([500,400])
# add to group
s_group.add(sig1)
s_group.add(sig2)
s_group.add(sig3)
s_group.add(sig4)


# REMEBER SEQUENCE MATTERS
# sr1 = S_Road(p4, [300,230], 90, "03")
# sr2 = S_Road([300,230], p5, 180, "03")
# sr3 = S_Road(p4, [200,230], 90, "02")
# sr4 = S_Road([200,230], p7, 90, "02")

# sig1.addSRoad(sr1)
# sig1.addSRoad(sr2)
# sig1.addSRoad(sr3)
# sig1.addSRoad(sr4)




# make combinations out of roads
destination1 = [r22,r23,r24]
# destination2 = [r2,[sig1,"02"],r3]


# groups to handle intersections
body_sect = pygame.sprite.Group()
near_sect = pygame.sprite.Group()
far_sect = pygame.sprite.Group()

# group that holds all car singles
car_group = CarGroup()

class CarFactory():
    def __init__(self, limit, destination):
        self.last = pygame.time.get_ticks()
        self.cooldown = 4000 
        self.limit = limit
        self.counter = 0        
        self.destination = destination

        self.p1 = destination[0].getP1()

        self.near_sect = near_sect
        self.body_sect = body_sect
        self.far_sect = far_sect
        self.car_group = car_group


    def spawn(self):
        # fire gun, only if cooldown has been 0.5 seconds since last
        now = pygame.time.get_ticks()
        if (self.limit == -1)  or (self.counter < self.limit):
            if now - self.last >= self.cooldown:
                self.last = now

                n1 = Near(self.p1)
                self.near_sect.add(n1)

                b1 = Body(self.destination, road_watcher)
                self.body_sect.add(b1)

                f1 = Far(self.p1)
                self.far_sect.add(f1)


                car = CarSingle()
                car.add(b1)
                car.add(n1)
                car.add(f1)

                car_group.add(car)

                self.counter += 1

cf = CarFactory(-1, destination1)
# cf2 = CarFactory(-1, destination2)

while not crashed:
    # events
    for event in pygame.event.get():
        # exit event
        if event.type == pygame.QUIT:
            crashed = True
            pygame.quit()
            quit()

    screen.fill(bg_grey)
    s_group.draw(screen)    
    road_watcher.drawRoads()

    # clear()
    # for l in road_watcher.getRoads():        
    #     print("{} {}".format(l.getName(),len(l.getCarList())))

    # collision code
    # far collision
    # --------------------------------------------
    # col_far = []
    # result_far = pygame.sprite.groupcollide(body_sect, far_sect, False, False)
    # # print(result_far)
    # for sprite in result_far:
    #     if result_far[sprite]:
    #         # print(result_far[sprite])
    #         for far in result_far[sprite]:                
    #             if far in far_sect:
    #                 # far.groups()[1] = car single
    #                 cg = far.groups()[1]
    #                 # print(cg)
    #                 cg.setCarAcc(0.2)
    #                 # cg.setCarColor((0,0,255))
    #                 # # add to compare list
    #                 col_far.append(cg)

    # # revert cars to original acceleration
    # # once they are out of the collision zone
    # for revert_far in car_group.getList():
    #     if revert_far not in col_far:
    #         revert_far.setCarAcc(1.1)


    # # near collision
    # col_near = []
    # result_near = pygame.sprite.groupcollide(body_sect, near_sect, False, False)
    # # print(result_near)
    # for sprite2 in result_near:
    #     if result_near[sprite2]:
    #         for near in result_near[sprite2]:    
    #             if near in near_sect:
    #                 # near.groups()[1] = car single
    #                 # print(near.groups()[1])
    #                 cg2 = near.groups()[1]
    #                 # cg2.setCarColor((0,0,255))
    #                 cg2.setCarAcc(0.0)
    #                 col_near.append(cg2)

    # # revert cars to original acceleration
    # # once they are out of the collision zone
    # for revert_near in car_group.getList():
    #     if revert_near not in col_near:
    #         revert_near.setCarAcc(1.1)


    # result_sig = pygame.sprite.groupcollide(body_sect, s_group, False, False)
    # for sprite3 in result_sig:
    #     # each car-body
        
    #     # quit()
    #     if result_sig[sprite3]:
    #         for s in result_sig[sprite3]:
    #             # each signal
    #             # s.setColor((0,0,0))
    #             sprite3.setColor((0,0,255))
    #             # print(sprite3.groups()[1])
    #             if not sprite3.canGo(s):
    #                 sprite3.setAcc(0.0)
    #             else:
    #                 sprite3.setAcc(1.1)


   
    # # cycle through each signal
    # # change the bool list to allow cars to pass
    # # get a time instance
    # now = pygame.time.get_ticks()
    # for sig_single in s_group:
    #     sig_single.updateBoolArray(now)
    #     # access the time array
    #     # if passed make bool true
    # --------------------------------------------

    cf.spawn()
    # cf2.spawn()
    car_group.updateGroup()
    car_group.draw(screen)

    # update screen
    pygame.display.update()
    # fps
    clock.tick(fps)
