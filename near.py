import pygame

# near field
# add speed constraints
# near field
# add speed constraints
class Near(pygame.sprite.Sprite):
    def __init__(self, pos, color=(0,255,0)):
        pygame.sprite.Sprite.__init__(self)
        # self.image = pygame.Surface([3, 10])
        # self.image.fill(color)
        self.image = pygame.Surface([3, 10], pygame.SRCALPHA, 32)
        self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.c = self.image

    def updateRight(self, topleft, angle):
        # self.rect.topleft = topleft
        # c = self.image
        self.image = pygame.transform.rotate(self.c, angle)
        self.rect = self.image.get_rect(topleft=topleft)
        return self.rect.topright


    def updateLeft(self, topleft, angle):
        # self.rect.topleft = topleft
        # c = self.image
        self.image = pygame.transform.rotate(self.c, angle)
        self.rect = self.image.get_rect(topright=topleft)
        return self.rect.topleft
        


    def updateDown(self, topright, angle):
        self.image = pygame.transform.rotate(self.c, angle)
        self.rect = self.image.get_rect(topright=topright)
        return self.rect.bottomright

    def updateUp(self, topright, angle):
        self.image = pygame.transform.rotate(self.c, angle)
        self.rect = self.image.get_rect(bottomright=topright)
        return self.rect.topright  