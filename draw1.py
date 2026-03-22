import pygame, sys
from pygame.locals import *

pygame.init()

# Настройка окна
DISPLAY_SURF = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Рисование')

# Настройка цветов
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Доработки
YELLOW=(233, 237, 0)
DARK_GRAY=(77,77,77)

# Рисование на объекте поверхности
DISPLAY_SURF.fill(DARK_GRAY)
pygame.draw.polygon(DISPLAY_SURF, YELLOW, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))
pygame.draw.line(DISPLAY_SURF, BLUE, (60, 60), (120, 60), 4)
pygame.draw.line(DISPLAY_SURF, BLUE, (120, 60), (60, 120),10)
pygame.draw.line(DISPLAY_SURF, BLUE, (60, 120), (120, 120), 4)
pygame.draw.circle(DISPLAY_SURF, BLUE, (300, 50), 20, 5)
pygame.draw.ellipse(DISPLAY_SURF, RED, (0, 320, 40, 80), 1)
pygame.draw.rect(DISPLAY_SURF, RED, (400, 0, 100, 50))

# Доработки
pygame.draw.rect(DISPLAY_SURF, RED, (200, 150, 100, 100))
pygame.draw.polygon(DISPLAY_SURF, BLUE, ((264, 0), (292, 277), (236, 277)))

pixObj = pygame.PixelArray(DISPLAY_SURF)


pixObj = pygame.PixelArray(DISPLAY_SURF)
y=290
while y<350:
   y+=10
   x=98
   while x<150:
      x+=2
      pixObj[x][y]=WHITE
del pixObj

pixObj = pygame.PixelArray(DISPLAY_SURF)
x=90
while x<150:
   x+=10
   y=300
   while y<350:
      y+=2
      pixObj[x][y]=WHITE
del pixObj


# Игровой цикл
while True:
   for event in pygame.event.get():
      if event.type == QUIT:
          pygame.quit()
          sys.exit()
   pygame.display.update()

