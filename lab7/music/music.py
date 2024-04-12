import pygame
import sys
import os

pygame.init()
clock = pygame.time.Clock()

# Установка окна
size = (450, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Spotify')

# Загрузка изображений
background_img = pygame.image.load("C:/Users/alibi\PycharmProjects\pythonProject\lab7\music\image/2.png")
image = pygame.image.load("C:/Users/alibi\PycharmProjects\pythonProject\lab7\music\image/1.png")

# Загрузка музыки (поиск всех mp3 файлов в текущей папке)
music = [f.name for f in os.scandir('.') if f.is_file() and f.name.endswith('.mp3')]

# Основной цикл программы
playing = False
index = 0
volume = 1.0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                # Начать воспроизведение выбранной музыки
                pygame.mixer.music.load(music[index])
                pygame.mixer.music.play()
                playing = True

            elif event.key == pygame.K_SPACE:
                # Пауза / Возобновление воспроизведения
                if playing:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
                playing = not playing

            elif event.key == pygame.K_RIGHT:
                # Следующий трек
                index = (index + 1) % len(music)
                pygame.mixer.music.load(music[index])
                pygame.mixer.music.play()
                playing = True

            elif event.key == pygame.K_LEFT:
                # Предыдущий трек
                index = (index - 1) % len(music)
                pygame.mixer.music.load(music[index])
                pygame.mixer.music.play()
                playing = True

            elif event.key == pygame.K_UP:
                # Увеличить громкость
                volume = min(volume + 0.1, 1.0)
                pygame.mixer.music.set_volume(volume)

            elif event.key == pygame.K_DOWN:
                # Уменьшить громкость
                volume = max(volume - 0.1, 0.0)
                pygame.mixer.music.set_volume(volume)

    # Отображение на экране
    screen.blit(background_img, (0, 0))
    screen.blit(image, (0, 0))

    # Отображение информации о текущем треке
    font = pygame.font.SysFont('Tahoma', 19, True)
    track_name = music[index][:-4] if music else "No music found"
    text_surface = font.render(track_name, True, pygame.Color('white'))
    screen.blit(text_surface, (78, 405))

    # Обновление экрана
    pygame.display.flip()

    # Ограничение частоты кадров
    clock.tick(10)
