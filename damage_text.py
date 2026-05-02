import pygame

class DamageText:
    def __init__(self, x, y, damage):
        self.x = x
        self.y = y
        self.text = str(damage)
        self.life = 30
        self.vel_y = -1

    def draw(self, screen, font):
        text_surface = font.render(self.text, True, (255, 0, 0))
        screen.blit(text_surface, (self.x, self.y))
        
        self.y += self.vel_y
        self.life -= 1