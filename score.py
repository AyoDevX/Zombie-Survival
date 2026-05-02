import pygame

class Score:
    def __init__(self):
        self.value = 0
        self.font = pygame.font.Font(None, 40)

        # animation
        self.scale = 1
        self.target_scale = 1

        # color effect
        self.color = (255, 255, 255)
        self.flash_timer = 0

    def add(self, amount):
        self.value += amount

        # effect ديال التكبير
        self.target_scale = 1.5

        # effect ديال اللون
        self.color = (255, 215, 0)  # ذهبي
        self.flash_timer = 10

    def update(self):
        # smooth scale animation
        self.scale += (self.target_scale - self.scale) * 0.2
        self.target_scale = 1

        # رجوع اللون
        if self.flash_timer > 0:
            self.flash_timer -= 1
        else:
            self.color = (255, 255, 255)

    def draw(self, screen):
        text = f"SCORE: {self.value}"
        text_surface = self.font.render(text, True, self.color)

        # scaling
        size = text_surface.get_size()
        text_surface = pygame.transform.scale(
            text_surface,
            (int(size[0] * self.scale), int(size[1] * self.scale))
        )

        # background box
        x, y = 530, 20
        padding = 10
        box_rect = pygame.Rect(
            x - padding,
            y - padding,
            text_surface.get_width() + padding * 2,
            text_surface.get_height() + padding * 2
        )

        pygame.draw.rect(screen, (30, 30, 30), box_rect, border_radius=10)
        pygame.draw.rect(screen, (255, 215, 0), box_rect, 2, border_radius=10)

        screen.blit(text_surface, (x, y))