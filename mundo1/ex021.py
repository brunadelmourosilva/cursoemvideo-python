# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.


#instalar o pygame
import pygame
pygame.init() #inicia o pygame
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()
