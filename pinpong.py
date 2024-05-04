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


      # сама игра: действия спрайтов, проверка правил игры, перерисовка
    if not finish:
        # обновляем фон
        window.blit(background,(0,0))

    display.update()
    clock.tick(FPS)
