

class S_Road():
    def __init__(self, p1, p2, angle, name):
        self.p1 = p1
        self.p2 = p2
        self.angle = angle
        self.name = name
        # self.car_list = []


    def getP1(self):
        return self.p1

    def getP1X(self):
        return self.p1[0]

    def getP1Y(self):
        return self.p1[1]

    def getP2X(self):
        return self.p2[0]

    def getP2Y(self):
        return self.p2[1]

    def getAngle(self):
        return self.angle

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other): 
        return self.__dict__ == other.__dict__

    def getName(self):
        return self.name

    # def addCar(self, car):
    #     if car not in self.car_list:
    #         self.car_list.append(car)

    # def removeCar(self, car):
    #     self.car_list.remove(car)

    # def getCarList(self):
    #     return self.car_list