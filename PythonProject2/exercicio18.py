# Faça um programa em python que abra e reproduza um audio em mp3
import pygame
pygame.init()
pygame.mixer.music.load('ex21.mp3')
pygame.mixer.music.play()
pygame.event.wait()
