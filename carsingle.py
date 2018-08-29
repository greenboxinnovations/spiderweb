import pygame
import math

# class to hold car components
class CarSingle(pygame.sprite.Group):
    def __init__(self):
        pygame.sprite.Group.__init__(self)
        self.should_kill = False

    def myUpdate(self):
        
        try:
            body = self.sprites()[0]
            near = self.sprites()[1]
            far = self.sprites()[2]
        except Exception as e:
            print(e)
        

        body.update()
        if body.shouldKill():
            far.kill()
            near.kill()
            body.kill()
            self.should_kill = True
        else:

            n_pos = body.getTopRight()
            angle = body.getAngle()
            # print(angle)        
            # print(math.degrees(r_angle))

                        

            if angle == 0.0:
                n_pos = body.getTopRight()
                pos = near.updateRight(n_pos, angle)
                far.updateRight(pos, angle)

            elif angle == 90.0:
                n_pos = body.getBottomRight()
                pos = near.updateDown(n_pos, angle)
                far.updateDown(pos, angle)

            elif angle == -90.0:
                n_pos = body.getTopRight()
                pos = near.updateUp(n_pos, angle)            
                far.updateUp(pos, angle)

            elif angle == 180.0:
                n_pos = body.getTopLeft()
                pos = near.updateLeft(n_pos, angle)
                far.updateLeft(pos, angle)       
        
        
    def setCarAcc(self,acc):
        try:
            body = self.sprites()[0]
            body.setAcc(acc)
            # body.setColor(acc)
        except Exception as e:
            pass
            # print(e)
            # raise e

    def setCarColor(self,color):
        try:
            body = self.sprites()[0]
            body.setColor(color)
            # body.setColor(acc)
        except Exception as e:
            print(e)
        

    def shouldKill(self):
        return self.should_kill