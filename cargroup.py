
# group that holds all cars
# NOTE: not a pygame.sprite.group instance
# could be changed
class CarGroup():
    def __init__(self):
        self.car_list = []

    def updateGroup(self):        
        for car_single in self.car_list:
            if car_single.shouldKill():                
                self.car_list.remove(car_single)
                # pass
            else:
                car_single.myUpdate()

    def add(self, car):
        self.car_list.append(car)

    def draw(self, screen):
        for car_single in self.car_list:
            car_single.draw(screen)

    def getList(self):
        return self.car_list