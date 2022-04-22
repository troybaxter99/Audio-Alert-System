import time
import sys
import pygame

sys.path.insert(1,"/home/pi/Audio-Alert-System/Code")
import audio

path = "/home/pi/Audio-Alert-System/Audio-Files/Tech-Interface-Audio/"

test = audio.AUDIO(path)
test.set_volume(15) # Set audio to 15%
test.play_audio("startup.wav")

time.sleep(5)

test.set_volume(15)
test.play_audio("button_press.wav")

time.sleep(1)

test.set_volume(15)
test.play_audio("shutdown.wav")
