
import pygame

class RoadWatcher():
    def __init__(self, screen, color=(116,116,116)):
        self.road_list = []      
        self.car_list = []
        self.screen = screen
        self.color = color

    def add(self, item):
        self.road_list.append(item)

    def getRoads(self):
        return self.road_list

    def drawRoads(self):
        # print(len(road_watcher))    
        for road in self.road_list:
            try:            
                p1x = road.getP1X()
                p1y = road.getP1Y()
                
                p2x = road.getP2X()
                p2y = road.getP2Y()            

                pygame.draw.line(self.screen, self.color, (p1x,p1y), (p2x,p2y), 2)
            except Exception as e:
                print(e)

    def getCarList(self):
        return self.car_list

    def addToCarList(self, car, road):
        if car not in self.car_list:
            self.car_list.append(car)
            for _road in self.road_list:
                _road.addCar(car)

        else:
            # find if road and car are the same
            # in each road
            for _road in self.road_list:
                # get each carlist
                _car_list = _road.getCarList()
                # check if car exists
                if car in _car_list:
                    # if the road is different
                    # remove old
                    # insert new
                    if not _road == road:
                        _road.removeCar(car)
                        road.addCar(car)

    def removeFromCarList(self, car):
        if car in self.car_list:
            self.car_list.remove(car)

        # check each road
        for _road in self.road_list:
            # get each list
            _car_list = _road.getCarList()
            # if car exists in list
            if car in _car_list:
                _road.removeCar(car)