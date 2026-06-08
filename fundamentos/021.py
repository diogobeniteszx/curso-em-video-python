import pygame
import time
from mutagen.mp3 import MP3

caminho_audio = r'C:\Users\Diogo\Music\just.mp3'

audio = MP3(caminho_audio)
duracao = audio.info.length

pygame.mixer.init()
pygame.mixer.music.load(caminho_audio)
pygame.mixer.music.play()

time.sleep(round(duracao))
pygame.mixer.quit()
