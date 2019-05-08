import pygame
# global GameScore
# GameScore = GameFont2.render("0",0,(255,255,255))

button1 = pygame.image.load("graphics/Button2.png")
button2 = pygame.image.load("graphics/Button1.png")
button3 = pygame.image.load("graphics/Button3.png")
button4 = pygame.image.load("graphics/Button4.png")
lives = pygame.image.load("graphics/lives.png")

background = pygame.image.load("graphics/Map2.png")
logo = pygame.image.load("graphics/Logo.png")
readme = pygame.image.load("graphics/Help.png")


bestscore = open("highscore", "r+")
oof = bestscore.readline().splitlines()
# Highscore = GameFont2.render("HIGHSCORE: "+oof[0],0 ,(255,255,255))