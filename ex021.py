#faça um programa em python que abra e reproduza um áudio em mp3
import pygame
pygame.init()
pygame.mixer.music.load('nomedoarquivomp3')
pygame.mixer.music.play()
pygame.event.wait()

#esse módulo tem funcionalidades como repoduzir audios e imagens. Os arquivos precisam estar dentro da mesma pasta que o projeto.
