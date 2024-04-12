import pygame
import sys

pygame.init()

# Параметры экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Параметры мяча
BALL_SIZE = 50
BALL_RADIUS = BALL_SIZE // 2
ball_x = (SCREEN_WIDTH - BALL_SIZE) // 2
ball_y = (SCREEN_HEIGHT - BALL_SIZE) // 2
BALL_SPEED = 10

# Создание экрана
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Мячик")

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    ball_x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * BALL_SPEED
    ball_y += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * BALL_SPEED

    # Ограничение мяча в пределах экрана
    ball_x = max(0, min(SCREEN_WIDTH - BALL_SIZE, ball_x))
    ball_y = max(0, min(SCREEN_HEIGHT - BALL_SIZE, ball_y))

    # Отрисовка на экране
    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (ball_x + BALL_RADIUS, ball_y + BALL_RADIUS), BALL_RADIUS)

    # Обновление экрана
    pygame.display.flip()

    # Ограничение FPS
    clock.tick(60)

pygame.quit()
sys.exit()
