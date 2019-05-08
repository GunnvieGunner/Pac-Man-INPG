# coding=utf-8

import pygame

class Ghost:

    def __init__(self, name, sprite, velocity):

        self.name = name
        self.sprite = pygame.image.load(sprite)
        self.velocity = velocity

    def move(self):
        pass

    def draw(self):
        pass

