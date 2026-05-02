import pygame
import assets
import random
from hero import Hero
from zombies import Zombie
from damage_text import DamageText
from score import Score
succ , fail = pygame.init()
print(succ,fail)


#SOUNDS EFECTS :
pygame.mixer.init()
pygame.mixer.music.load("sounds/background_music.mp3")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)
footstep_sound = pygame.mixer.Sound("sounds/footstep_grass2.ogg")
sword_sounds = [
    pygame.mixer.Sound("sounds/sword_slice.wav"),
    pygame.mixer.Sound("sounds/sword_slice2.ogg"),
    pygame.mixer.Sound("sounds/sword_slice3.ogg"),
]
gameover_sound = pygame.mixer.Sound("sounds/game_over.wav")
victory_sound = pygame.mixer.Sound("sounds/victory.wav")
boss_sound = pygame.mixer.Sound("sounds/boss.ogg")
zombie_group_sound = pygame.mixer.Sound("sounds/group_of_zombies.ogg")
zombie_hurt_sound = pygame.mixer.Sound("sounds/zombie_hurt.ogg")
hero_hurt_sound = pygame.mixer.Sound("sounds/hero_hurt.ogg")
win_sound = pygame.mixer.Sound("sounds/win.wav")
hover_sound = pygame.mixer.Sound("sounds/hover.wav")
click_sound = pygame.mixer.Sound("sounds/click.wav")
#Volume : 
footstep_sound.set_volume(0.09)
for s in sword_sounds:
    s.set_volume(0.9)
gameover_sound.set_volume(0.7)
victory_sound.set_volume(0.7)
boss_sound.set_volume(0.8)
zombie_group_sound.set_volume(0.1)
zombie_hurt_sound.set_volume(0.6)
hero_hurt_sound.set_volume(0.6)
win_sound.set_volume(0.7)
hover_sound.set_volume(0.5)
click_sound.set_volume(0.5)

#MAIN VARIABELS :
screen_width = 700
screen_height = 500
clock = pygame.time.Clock()
score = Score()
last_spawn_score = 0

#RGB
BLACK = (0,0,0) 
WHITE = (255,255,255) 
RED = (255,0,0) 
GREEN = (34, 139, 34)

#MAIN SETTINGS :
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("ZOMBIE SURVIVAL")
bg = pygame.image.load("bg.png")
bg = pygame.transform.scale(bg, (screen_width, screen_height))
heart_full = pygame.image.load("heart_full.png").convert_alpha()
heart_empty = pygame.image.load("heart_empty.png")
heart_full = pygame.transform.scale(heart_full, (25, 25))
heart_empty = pygame.transform.scale(heart_empty, (25, 25))
menu_bg = pygame.image.load("menu.png")
menu_bg = pygame.transform.scale(menu_bg, (screen_width, screen_height))
gameover_bg = pygame.image.load("game_over.png")
gameover_bg = pygame.transform.scale(gameover_bg, (screen_width, screen_height))
victory_bg = pygame.image.load("victory.png")
victory_bg = pygame.transform.scale(victory_bg, (screen_width, screen_height))
win_bg = pygame.image.load("win.png")
win_bg = pygame.transform.scale(win_bg, (screen_width, screen_height))


#FONTS :
#damage font
font = pygame.font.SysFont("comicsans", 20)
damage_texts = []
#game over font
game_over_font = pygame.font.SysFont("Arial", 60)
restart_font = pygame.font.SysFont("Arial", 30)


#MAIN CHARACTERS:
hero = Hero(x=579, y=365, width=100, height=100)
hero.footstep_sound = footstep_sound
hero.sword_sounds = sword_sounds
zombies = [Zombie(x=0, y=335, width=100, height=100, end=600)]
# game_state = {
#     "wave": 1,
#     "boss_spawned": False,
#     "in_gameover": False,
#     "in_menu": True,
# }
# MAX_WAVE = 3
game_state = {
    "level": 1,
    "wave": 1,
    "boss_spawned": False,
    "in_gameover": False,
    "in_menu": True,
    "in_victory": False,
    "in_final_victory": False,
    "in_win": False,
}
LEVEL_CONFIG = {
    1: {"max_wave": 5,  "start_zombies": 1, "boss_count": 1, "boss_health": 200},
    2: {"max_wave": 10, "start_zombies": 2, "boss_count": 2, "boss_health": 300},
    3: {"max_wave": 15, "start_zombies": 3, "boss_count": 3, "boss_health": 400},
}
MAX_LEVEL = 3

#BUTTONS :
start_button = pygame.Rect(250,210,167,52)
exit_button = pygame.Rect(250,288,167,52)
retry_button = pygame.Rect(130,430,180,54)
menu_button = pygame.Rect(350,430,200,54)
next_level_button = pygame.Rect(245, 420, 219, 55)
thankyou_button = pygame.Rect(230, 420, 236, 50)

def draw_health_bar(screen, x, y, width, height, current_hp, max_hp):
    # الخلفية (أحمر)
    pygame.draw.rect(screen, (255, 0, 0), (x, y, width, height))
    
    # حساب الصحة الحالية
    ratio = max( 0, current_hp) / max_hp
    pygame.draw.rect(screen, (0, 255, 0), (x, y, width * ratio, height))
    pygame.draw.rect(screen, (255,255,255),(x, y, width, height),2)

def draw_hearts(screen, hero):
    for i in range(hero.max_lives):
        x = 220 + i *20
        y = 17
        if i < hero.lives:
            screen.blit(heart_full, (x, y))
        else:
            screen.blit(heart_empty, (x, y))
        
def drawtheGame():
    screen.blit(bg, (0, 0))
    for zombie in zombies:
        zombie.draw(screen,hero)
    
    if hero.isAttacking:
        hero.draw_attack(screen)
        # attack_box = hero.get_attack_hitbox()
        # pygame.draw.rect(screen,GREEN,attack_box,2)
    else:
        hero.draw(screen)
    draw_health_bar(screen, 20, 20, 200, 20, hero.health, 100)
    draw_hearts(screen, hero)
    
    for text in damage_texts[:]:
        text.draw(screen, font)
        if text.life <= 0:
            damage_texts.remove(text)
              
    score.update()
    score.draw(screen)
        
    pygame.display.update()
    
def draw_menu():
    global hovered_button
    screen.blit(menu_bg, (0,0))
    mouse_pos = pygame.mouse.get_pos()
    curent_hover = None
    if start_button.collidepoint(mouse_pos):
        curent_hover = "start"
    elif exit_button.collidepoint(mouse_pos):
        curent_hover = "exit"
    if curent_hover != hovered_button:
        if curent_hover is not None:
            hover_sound.play()
    hovered_button = curent_hover
    if start_button.collidepoint(mouse_pos) or exit_button.collidepoint(mouse_pos):
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    pygame.display.update()

def draw_gameover_menu():
    global hovered_go_button

    screen.blit(gameover_bg, (0, 0))
    mouse_pos = pygame.mouse.get_pos()
    
    current_hover = None

    if retry_button.collidepoint(mouse_pos):
        current_hover = "retry"
    elif menu_button.collidepoint(mouse_pos):
        current_hover = "menu"

    # sound hover
    if current_hover != hovered_go_button:
        if current_hover is not None:
            hover_sound.play()

    hovered_go_button = current_hover

    # cursor
    if current_hover:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    pygame.display.update()

def draw_victory_screen(is_final=False):
    global hovered_victory_button
    screen.blit(victory_bg, (0, 0))
    mouse_pos = pygame.mouse.get_pos()
    if not is_final:
        current_hover = None
        if next_level_button.collidepoint(mouse_pos):
            current_hover = "next"
        if current_hover != hovered_victory_button:
            if current_hover is not None:
                hover_sound.play()
        hovered_victory_button = current_hover
        if current_hover:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
    else:
        final_font = pygame.font.SysFont("Arial", 28, bold=True)
        final_text = final_font.render("Press any key to return to Menu", True, WHITE)
        screen.blit(final_text, (screen_width // 2 - final_text.get_width() // 2, 460))
    pygame.display.update()

def draw_win_screen():
    global hovered_win_button
    screen.blit(win_bg, (0, 0))
    pygame.draw.rect(screen,(0,255,0),thankyou_button,2)
    mouse_pos = pygame.mouse.get_pos()
    current_hover = None
    if thankyou_button.collidepoint(mouse_pos):
        current_hover = "thankyou"
    if current_hover != hovered_win_button:
        if current_hover is not None:
            hover_sound.play()
    hovered_win_button = current_hover
    if current_hover:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
    pygame.display.update()

hovered_button = None
hovered_go_button = None
hovered_victory_button = None
hovered_win_button = None
last_zombie_hurt_sound = 0
last_hero_hurt_sound = 0
#MAIN LOOP :
run = True
while run:
    clock.tick(30)
    
    # ====================================== MENU ======================================
    if game_state["in_menu"]:
        pygame.mixer.music.set_volume(0.07)
        draw_menu()       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if start_button.collidepoint(mouse_pos):
                    click_sound.play()
                    game_state["in_menu"] = False
                    pygame.mixer.music.set_volume(0.5)
                    
                if exit_button.collidepoint(mouse_pos):
                    click_sound.play()
                    run = False
        continue
    # ====================================== VICTORY ======================================
    if game_state["in_victory"]:
        pygame.mixer.music.stop()
        draw_victory_screen(is_final=False)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if next_level_button.collidepoint(mouse_pos):
                    click_sound.play()
                    victory_sound.stop()
                    game_state["level"] += 1
                    pygame.mixer.music.play(-1)
                    pygame.mixer.music.set_volume(0.5)
                    game_state["wave"] = 1
                    game_state["boss_spawned"] = False
                    game_state["in_victory"] = False
                    config = LEVEL_CONFIG[game_state["level"]]
                    zombies.clear()
                    for i in range(config["start_zombies"]):
                        zombies.append(Zombie(x=random.randint(0,600), y=335, width=100, height=100, end=600))
                    hero = Hero(x=579, y=365, width=100, height=100)
                    hero.footstep_sound = footstep_sound
                    hero.sword_sounds = sword_sounds
        continue
    
    # ====================================== WIN SCREEN ======================================
    if game_state["in_win"]:
        pygame.mixer.music.stop()
        draw_win_screen()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if thankyou_button.collidepoint(mouse_pos):
                    click_sound.play()
                    win_sound.stop()
                    game_state["in_win"] = False
                    game_state["in_menu"] = True
                    game_state["level"] = 1
                    game_state["wave"] = 1
                    game_state["boss_spawned"] = False
        continue

    # ====================================== GAME OVER ======================================
    if game_state["in_gameover"]:
        draw_gameover_menu()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                
                # RETRY
                if retry_button.collidepoint(mouse_pos):
                    click_sound.play()
                    hero = Hero(x=579, y=365, width=100, height=100)
                    hero.footstep_sound = footstep_sound
                    hero.sword_sounds = sword_sounds
                    zombies = [Zombie(x=0, y=335, width=100, height=100, end=600)]
                    score = Score()
                    game_state["wave"] = 1
                    game_state["boss_spawned"] = False
                    game_state["in_gameover"] = False
                    game_state["in_victory"] = False
                    game_state["in_win"] = False
                   
                    
                # MAIN MENU
                if menu_button.collidepoint(mouse_pos):
                    click_sound.play()
                    game_state["in_gameover"] = False
                    game_state["in_menu"] = True

        continue        
    
    # ====================================== GAME ======================================
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            
    keys = pygame.key.get_pressed()
    
    # ====================================== HERO ACTIONS ======================================
    if not hero.isDying:
        hero.move(keys,screen_width)
        hero.jump(keys)
        
        for zombie in zombies:
            zombie.check_attack(hero)
            current_time = pygame.time.get_ticks()
        if hero.isHurt:
            if current_time - last_hero_hurt_sound > 600:
                hero_hurt_sound.play()
                last_hero_hurt_sound = current_time
        
        if keys[pygame.K_a] and not hero.isAttacking:
            hero.isAttacking = True
            hero.attackType = random.randint(0,2)
            
    # ====================================== ATTACK SYSTEM ======================================        
    if hero.isAttacking and hero.attackCount < 10 and not hero.isDying:
        attack_rect = hero.get_attack_hitbox()
        for zombie in zombies[:]:
            zombie_rect = zombie.hitbox
            if attack_rect.colliderect(zombie_rect):
                if not hero.hasHit:
                    zombie.health -= 10
                    zombie.isHurt = True
                    zombie.isAttacking = False
                    hero.hasHit = True
                    damage_texts.append(DamageText(zombie.x + 40, zombie.y, "-10"))
                    current_time = pygame.time.get_ticks()
                    if current_time - last_zombie_hurt_sound > 500:
                        zombie_hurt_sound.play()
                        last_zombie_hurt_sound = current_time
                    if zombie.health <= 0 and not zombie.counted:
                        zombie.isDying = True
                        score.add(10)
                        zombie.counted = True
                        
    # ====================================== REMOVE DEAD ZOMBIES ======================================                    
    for zombie in zombies[:]:
        if not zombie.isAlive:
            zombies.remove(zombie)
            
    # ====================================== SPAWN SYSTEM ======================================  
    config = LEVEL_CONFIG[game_state["level"]]
    if len(zombies) == 0:
        GROUND_Y = 365
        if game_state["wave"] >= config["max_wave"] and not game_state["boss_spawned"]:
            # spawn البوسات
            positions = [100, 300, 500]
            for i in range(config["boss_count"]):
                boss_height = 200
                boss = Zombie(x=positions[i], y=GROUND_Y-(boss_height-100), width=200, height=200, end=600)
                boss.health = config["boss_health"]
                boss.max_health = config["boss_health"]
                boss.damage = 5 + (game_state["level"] - 1) * 2
                boss.step = 2
                zombies.append(boss)
            game_state["boss_spawned"] = True
            boss_sound.play()
            zombie_group_sound.stop()
        elif game_state["boss_spawned"]:
            # قُتل كل البوسات
            if game_state["level"] < MAX_LEVEL:
                game_state["in_victory"] = True
                victory_sound.play()
                boss_sound.stop()
                zombie_group_sound.stop()
            else:
                game_state["in_win"] = True
                win_sound.play()
                boss_sound.stop()
                zombie_group_sound.stop()
                
        elif game_state["wave"] < config["max_wave"]:
            game_state["wave"] += 1
            for i in range(game_state["wave"]):
                zombies.append(Zombie(x=random.randint(0,600), y=335, width=100, height=100, end=600)) 
                zombie_group_sound.play()
                
    # ====================================== GAME OVER CHECK ======================================
    if hero.lives <= 0 and not hero.isDying :
        hero.isDying = True
        pygame.mixer.music.stop()
        hero.isHurt = False
        gameover_sound.play()
        game_state["in_gameover"] = True
        

        

    drawtheGame()