import pygame
import assets
import random
from constants import WHITE, RED, GREEN

class Zombie():
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.start = x
        self.end = end
        self.walkCount = 0
        self.step = 3
        # 👇 check واش boss ولا لا
        if width > 100:
            self.type = assets.boss_types_walk[0]
            self.attack_type = assets.boss_types_attack[0]
            self.hurt_type = assets.boss_types_hurt[0]
            self.die_type = assets.boss_types_die[0]
        else:
            self.zombieIndex = random.randint(0, 2)
            self.type = assets.zombies_types_walk[self.zombieIndex]
            self.attack_type = assets.zombies_types_attack[self.zombieIndex]
            self.hurt_type = assets.zombies_types_hurt[self.zombieIndex]
            self.die_type = assets.zombies_types_die[self.zombieIndex]
        
        if width > 100:
            self.hitbox = (self.x + 60, self.y + 60, self.width - 120, self.height - 80)
        else:
            self.hitbox = (self.x + 35, self.y + 35, self.width - 70, self.height - 30)
        
        self.health = 50
        self.isAlive = True
        self.damage = 1
        self.attack_range = 60
        self.isAttacking = False
        self.attackCount = 0
        self.last_attack_time = 0
        self.attack_cooldown = 1000
        self.isHurt = False
        self.hurtCount = 0
        self.dieCount = 0
        self.isDying = False
        self.counted = False
        self.max_health = self.health
        
    def draw(self, screen, hero):
        self.update_hitbox()
        if not self.isAlive:
            return
        if not self.isAttacking and not self.isHurt and not self.isDying:
            self.move()
        

    # اتجاه
        if self.step < 0:
            direction = "left"
        else:
            direction = "right"

    # 💀 dying (الأولوية)
        if self.isDying:
            screen.blit(self.die_type[direction][self.dieCount // 2], (self.x, self.y))
            self.dieCount += 1
            if self.dieCount >= len(self.die_type[direction]) * 2:
                self.isAlive = False
            self.draw_health_bar(screen)
            return

    # 🤕 hurt
        if self.isHurt:
            if self.hurtCount < len(self.hurt_type[direction]) * 2:
                screen.blit(self.hurt_type[direction][self.hurtCount // 2], (self.x, self.y))
                self.hurtCount += 1
            else:
                self.hurtCount = 0
                self.isHurt = False
            self.draw_health_bar(screen)
            return

    # ⚔️ attack
        if self.isAttacking:
            screen.blit(self.attack_type[direction][self.attackCount // 2], (self.x, self.y))
            self.attackCount += 1
            if self.attackCount >= len(self.attack_type[direction]) * 2:
                self.attackCount = 0
            self.draw_health_bar(screen)
            return

    # 🚶 walk
        screen.blit(self.type[direction][self.walkCount // 2], (self.x, self.y))
        self.walkCount += 1

        if self.walkCount >= len(self.type[direction]) * 2:
            self.walkCount = 0
        self.draw_health_bar(screen)

    def move(self):
       
        if self.step > 0:
            if self.x + self.step > self.end:
                self.step *= -1
            else:
                self.x += self.step
        else:
            if self.x <= self.start:
                self.step *= -1
            else:
                self.x += self.step
                
    def check_attack(self, hero):
        if not self.isAlive or self.isDying:
            return
        self.update_hitbox()    
        hero.update_hitbox() 
        current_time = pygame.time.get_ticks()

    # استخدم الـ hitbox بدل self.x
        if self.hitbox.colliderect(hero.hitbox) and not hero.isDying:
            self.isAttacking = True
            if current_time - self.last_attack_time > self.attack_cooldown:
                hero.health -= self.damage
                if hero.health <= 0 and hero.lives > 0:
                    hero.lives -= 1
                    hero.health = 100
                hero.isHurt = True
                hero.hurtCount = 0
                self.last_attack_time = current_time

        else:
            self.isAttacking = False           

    def draw_health_bar(self, screen):
         # ❤️ Zombie Health Bar
        bar_width = 60
        bar_height = 8
        bar_x = self.x + (self.width // 2) - (bar_width // 2)
        bar_y = self.y + 30

    # الأحمر
        pygame.draw.rect(screen, (255, 0, 0), (bar_x, bar_y, bar_width, bar_height))
    # الأخضر
        ratio = max(0, self.health) / self.max_health
        pygame.draw.rect(screen, (0, 255, 0), (bar_x, bar_y, bar_width * ratio, bar_height))
    # border
        pygame.draw.rect(screen, (255, 255, 255), (bar_x, bar_y, bar_width, bar_height), 1)
        
    def update_hitbox(self):
        if self.width > 100:  # Boss
            margin_x = int(self.width * 0.30)
            margin_top = int(self.height * 0.25)
            margin_bot = int(self.height * 0.10)
        else:  # زومبي عادي
            margin_x = int(self.width * 0.32)
            margin_top = int(self.height * 0.30)
            margin_bot = int(self.height * 0.10)

        self.hitbox = pygame.Rect(
            self.x + margin_x,
            self.y + margin_top,
            self.width - margin_x * 2,
            self.height - margin_top - margin_bot
        )
