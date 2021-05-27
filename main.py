# Importação das bibliotecas
import pygame
from pygame.locals import *
pygame.init()
from sys import exit

x = 512
y = 334
velocidade = 10
background = pygame.image.load('data/background.png')
character = pygame.image.load('data/character.png')
enemy = pygame.image.load('data/enemy.png')


# Criação da Janela principal do jogo
resX = 1600
resY = 900

janela = pygame.display.set_mode((resX,resY))
pygame.display.set_caption("Testing Room - Circle game")


while True:
    pygame.time.delay(30)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    janela.blit(background, (0, 0))


    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_w]:
        y -= velocidade
    if comandos[pygame.K_s]:
        y += velocidade
    if comandos[pygame.K_a]:
        x -= velocidade
    if comandos[pygame.K_d]:
        x += velocidade

    janela.blit(character, (x, y))
    janela.blit(enemy, (600, 600))
    pygame.display.update()









