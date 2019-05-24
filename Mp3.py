import pygame
from tkinter import *

file = 'Nome_do_Arquivo.mp3'
janela = Tk()
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play()
janela.mainloop()
