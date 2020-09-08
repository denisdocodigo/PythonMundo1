#Faça um programa em Python que abra e reproduza um arquivo em .mp3

import pygame

pygame.mixer.init()
pygame.init()

pygame.mixer_music.load('music.mp3')
pygame.mixer_music.play()
pygame.event.wait()