import pygame

# far field
# might have to add more
class Far(pygame.sprite.Sprite):
    def __init__(self, pos, color=(255,255,255)):
        pygame.sprite.Sprite.__init__(self)
        # self.image = pygame.Surface([5, 10])
        # self.image.fill(color)
        self.image = pygame.Surface([5, 10], pygame.SRCALPHA, 32)
        self.image.convert_alpha()        
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.c = self.image

    def update(self, topleft):
        self.rect.topleft = topleft

    def updateRight(self, pos, angle):
        self.image = pygame.transform.rotate(self.c, angle)
        self.rect = self.image.get_rect(topleft=pos)

    def updateLeft(self, pos, angle):
        self.image = pygame.transform.rotate(self.c, angle)
        self.rect = self.image.get_rect(topright=pos)

    def updateDown(self, pos, angle):
        self.image = pygame.transform.rotate(self.c, angle)
        self.rect = self.image.get_rect(topright=pos)

    def updateUp(self, pos, angle):
        self.image = pygame.transform.rotate(self.c, angle)
        self.rect = self.image.get_rect(bottomright=pos)

    def setColor(self, color):
        self.image.fill(color)