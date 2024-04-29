from pygame import *
#from random import randint
#from time import time as timer


img_back = '1.jpg'

#игровая сцена
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))

#флаги, отвечающие за состояние  игры
game = True
finish = False

#таймер
clock = time.Clock()
FPS = 60


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False


class GameSprite(sprite.Sprite):
  # конструктор класса
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # Вызываем конструктор класса (Sprite):
        sprite.Sprite.__init__(self)

        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed

        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

      # сама игра: действия спрайтов, проверка правил игры, перерисовка
    if not finish:
        # обновляем фон
        window.blit(background,(0,0))

    display.update()
    clock.tick(FPS)
