import pygame
import sprite

def collison(obj1,obj2):
     if obj1[1] < (obj2.rect[1] + obj2.rect[3]):
 
      if ((obj1[0] < obj2.rect[0]
           and obj1[0] < (obj2.rect[0] + obj2.rect[2]))
          or ((obj1[0] + obj2.rect[2]) > obj2.rect[0]
           and (obj1[0] + obj2.rect[2]) < (obj1[0] + obj2.rect[2]))):
              return True
      else:
          return False
class Grid:
    def __init__(self):
        self.all_sprites = pygame.sprite.Group()
        self.gridmm = sprite.Sprite("res/grid.png", [320, 240])
        self.all_sprites.add(self.gridmm)
        self.gridml = sprite.Sprite("res/grid.png", [240, 240])
        self.all_sprites.add(self.gridml)
        self.gridmr = sprite.Sprite("res/grid.png", [400, 240])
        self.all_sprites.add(self.gridmr)
        self.gridum = sprite.Sprite("res/grid.png", [320, 169])
        self.all_sprites.add(self.gridum)
        self.gridul = sprite.Sprite("res/grid.png", [240, 169])
        self.all_sprites.add(self.gridul)
        self.gridur = sprite.Sprite("res/grid.png", [400, 169])
        self.all_sprites.add(self.gridur)
        self.griddm = sprite.Sprite("res/grid.png", [320, 311])
        self.all_sprites.add(self.griddm)
        self.griddl = sprite.Sprite("res/grid.png", [240, 311])
        self.all_sprites.add(self.griddl)
        self.griddr = sprite.Sprite("res/grid.png", [400, 311])
        self.all_sprites.add(self.griddr)
    def show(self,window):
        for i in self.all_sprites:
               i.render(window)
    def place(self,window):
        crosses = pygame.sprite.Group()
        cross = sprite.Sprite("res/cross.png", (0,0))
        cross.edit_scale(0.1,0.1)
        circle = sprite.Sprite("res/circle.png", (0,0))
        cursor = pygame.mouse.get_pos()

        for i in self.all_sprites:
            if collison(cursor, i):
                cross.move(i.rect[0] - i.rect[2]/1.5 , i.rect[0] - i.rect[2]/1.5)
                cross.render(window)
                pygame.display.update()
            else:
                cross.move(1000,1000)
