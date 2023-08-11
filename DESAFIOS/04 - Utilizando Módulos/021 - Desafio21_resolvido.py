'''
    Faça um programa que abra e reproduza um arquivo de áudio MP3
'''
import pygame
pygame.init()
pygame.mixer.music.load("021 - Asa_Branca.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play()
pygame.event.wait()

# Obs: Abrir pelo IDLE(Python 3.10) para tocar a música pois não toca no Terminal do VScode nem pelo CMD