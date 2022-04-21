import time
import sys
import pygame

path = "/home/pi/Audio-Alert-System/Audio-Files/Alert-Audio/"
pygame.mixer.init()
speaker_volume = 1 # 100%
pygame.mixer.music.set_volume(speaker_volume)

pygame.mixer.music.load(path + "Overheating-Alert.wav")
pygame.mixer.music.play()
print("Overheating")