import pygame
import time
import sys

pygame.init()

# Установка размера окна
size = (800, 600)
screen = pygame.display.set_mode(size)

# Загрузка изображений
back = pygame.image.load("C:/Users/alibi\PycharmProjects\pythonProject\lab7\clock/back.jpg")
seconds = pygame.image.load("C:/Users/alibi\PycharmProjects\pythonProject\lab7\clock\seconds.png")
minutes = pygame.image.load("C:/Users/alibi\PycharmProjects\pythonProject\lab7\clock\minutes.png")

done = True
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False

    # Отображение фона
    screen.blit(back, (0, 0))

    # Получение текущего времени
    now = time.localtime()

    # Вычисление угла для минутной стрелки
    minute_angle = 360 - (now.tm_min * 6)
    min_rotate = pygame.transform.rotate(minutes, minute_angle)
    min_pos = ((size[0] - min_rotate.get_width()) / 2, (size[1] - min_rotate.get_height()) / 2)
    screen.blit(min_rotate, min_pos)

    # Вычисление угла для секундной стрелки
    second_angle = 360 - (now.tm_sec * 6)
    sec_rotate = pygame.transform.rotate(seconds, second_angle)
    sec_pos = ((size[0] - sec_rotate.get_width()) / 2, (size[1] - sec_rotate.get_height()) / 2)
    screen.blit(sec_rotate, sec_pos)

    # Обновление экрана
    pygame.display.flip()

pygame.quit()
sys.exit()
