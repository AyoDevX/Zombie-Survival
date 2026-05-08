import pygame
import assets
import random

BLACK = (0,0,0) 
WHITE = (255,255,255) 
RED = (255,0,0) 
GREEN = (34, 139, 34)


class Hero():
    def __init__(self, x, y, width, height):
        self.x =x
        self.y = y
        self.width = width
        self.height = height
        self.step = 5
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.isJumping = False
        self.standing = True
        self.hitbox = (self.x, self.y, self.width, self.height)
        self.isAttacking = False
        self.attackCount = 0
        self.attackType = 0
        self.health = 100
        self.isHurt = False
        self.hurtCount = 0 
        self.hasHit = False
        self.isDying = False
        self.dieCount = 0
        self.hurt_processed = False
        self.footstep_sound = None
        self.sword_sounds = None
        self.lives = 3
        self.max_lives = 3
        self.jumpAnimCount = 0
        
    def draw(self, screen):
        self.update_hitbox()
        if self.isDying:
            if self.right:
                screen.blit(assets.hero_die["right"][self.dieCount // 2], (self.x, self.y))
            else:
                screen.blit(assets.hero_die["left"][self.dieCount // 2], (self.x, self.y))
            self.dieCount += 1
    
            if self.dieCount >= len(assets.hero_die["right"]) * 2:
                self.dieCount = len(assets.hero_die["right"]) * 2 - 1
            return
             
        if self.isHurt:
            if self.right:
                screen.blit(assets.hero_hurt["right"][self.hurtCount // 2], (self.x, self.y))  
            else:
                screen.blit(assets.hero_hurt["left"][self.hurtCount // 2], (self.x, self.y))
        
            self.hurtCount += 1
    
            if self.hurtCount >= len(assets.hero_hurt["right"]) * 2:
                self.hurtCount = 0
                self.isHurt = False
            return
        
        if self.isJumping:
            if self.right:
                screen.blit(assets.hero_jump["right"][self.jumpAnimCount // 2], (self.x, self.y))
            else:
                screen.blit(assets.hero_jump["left"][self.jumpAnimCount // 2], (self.x, self.y))
            self.jumpAnimCount += 1
            if self.jumpAnimCount >= len(assets.hero_jump["right"]) * 2:
                self.jumpAnimCount = 0
            return
        
        if not self.standing:
            if self.right:
                screen.blit(assets.hero_walk["right"][self.walkCount // 2],(self.x, self.y))
                self.walkCount += 1
                if self.walkCount == 20:
                    self.walkCount = 0

            elif self.left:
                screen.blit(assets.hero_walk["left"][self.walkCount // 2], (self.x, self.y))
                self.walkCount += 1
                if self.walkCount == 20:
                    self.walkCount = 0
        else:
            if self.right:
                screen.blit(assets.hero_walk["right"][0], (self.x, self.y))
            else:
                screen.blit(assets.hero_walk["left"][0], (self.x, self.y))
                
    def move(self, keys, screen_width):
        if keys[pygame.K_LEFT] and self.x - self.step >=0 :
            self.x -= self.step
            self.left = True
            self.right = False
            self.standing = False
        elif keys[pygame.K_RIGHT] and self.x + self.width + self.step <= screen_width :
            self.x += self.step
            self.right = True
            self.left = False
            self.standing = False
        else:
            self.standing = True
            self.walkCount = 0
        if not self.standing and not self.isDying :
            if self.walkCount % 10 == 0 and self.footstep_sound:
                self.footstep_sound.play()
                
    def jump(self, keys):
        if not self.isJumping:
            
            if keys[pygame.K_SPACE] :
                self.isJumping = True
        else:
            if self.jumpCount >= -10 :
                neg = 1
                if self.jumpCount < 0:
                 neg = -1
                self.y -= (self.jumpCount ** 2) * 0.20 * neg
                self.jumpCount -= 1
            else:
                self.jumpCount = 10
                self.isJumping = False
                
    def draw_attack(self, screen):
        if self.attackCount == 0 and self.sword_sounds:
            self.sword_sounds[self.attackType].play()
        if self.isAttacking:
            attack = assets.hero_types_attack[self.attackType]
            if self.right:
                screen.blit(attack["right"][self.attackCount // 2], (self.x, self.y))
            else:
                screen.blit(attack["left"][self.attackCount // 2], (self.x, self.y))
            self.attackCount += 1
            # منين تسالي animation
            if self.attackCount >= len(attack["right"]) * 2:
                self.attackCount = 0
                self.isAttacking = False
                self.hasHit = False
                
    def get_attack_hitbox(self):
        attack_w = int(self.width * 0.65)  # عرض منطقة الضربة
        attack_h = int(self.height * 0.55) # ارتفاعها
        offset_y = int(self.height * 0.25) # من أين تبدأ رأسياً
        if self.left:
            return pygame.Rect(
                self.hitbox.left - attack_w,
                self.y + offset_y,
                attack_w,
                attack_h
            )
        else:
            return pygame.Rect(
                self.hitbox.right,
                self.y + offset_y,
                attack_w,
                attack_h
            )
  
    def update_hitbox(self):
            # نأخذ المنتصف الحقيقي للشخصية وندع هامش من كل جهة
        margin_x = int(self.width * 0.30)   # 30% من كل جانب
        margin_top = int(self.height * 0.20) # 20% من فوق
        margin_bot = int(self.height * 0.10) # 10% من تحت
        self.hitbox = pygame.Rect(
            self.x + margin_x,
            self.y + margin_top,
            self.width - margin_x * 2,
            self.height - margin_top - margin_bot
        )
        
        
    

    
            
                
                
                