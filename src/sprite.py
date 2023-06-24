import pygame

class Sprite(pygame.sprite.Sprite):
    def __init__(self, file, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(file)
        self.rect = self.image.get_rect()
        self.size = self.image.get_size()
        self.rect[0] = position[0]
        self.rect[1] = position[1]
        self.scale = [1,1]

    def edit_scale(self, scalar_x, scalar_y):
        size_x = self.size[0]
        size_y = self.size[1]
        self.image = pygame.transform.scale(self.image, (int(size_x * scalar_x), int(size_y * scalar_y)))
        self.scale = [self.scale[0]*scalar_x,self.scale[1]*scalar_y]
    
    def move(self, x, y):
        self.rect[0] = x
        self.rect[1] = y

    def render(self,win):
        win.blit(self.image, self.rect)
