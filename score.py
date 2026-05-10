import pygame

class Score:
    def __init__(self):
        self.value = 0
        self.flash_timer = 0

    def add(self, amount):
        self.value += amount
        self.flash_timer = 10

    def update(self):
        if self.flash_timer > 0:
            self.flash_timer -= 1

