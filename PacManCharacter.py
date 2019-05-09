# coding=utf-8

import pygame as pg

class PacMan:

    def __init__(self, sprite, velocity):
        self.sprite = pg.image.load(sprite)
        self.velocity = velocity