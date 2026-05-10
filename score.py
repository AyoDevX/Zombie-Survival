import pygame

class Score:
    def __init__(self):
        self.value = 0
        self.flash_timer = 0
        self.font = pygame.font.SysFont("Courier New", 15, bold=True)
        self.label_font = pygame.font.SysFont("Courier New", 11, bold=True)

    def add(self, amount):
        self.value += amount
        self.flash_timer = 10

    def update(self):
        if self.flash_timer > 0:
            self.flash_timer -= 1

    def draw(self, screen, value, flash):
        pass
