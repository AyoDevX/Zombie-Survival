import pygame
import assets
import random
from hero import Hero
from zombies import Zombie
from damage_text import DamageText
from score import Score
from constants import WHITE, RED, GREEN

pygame.init()


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

GROUND_Y = 365

#MAIN SETTINGS :
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("ZOMBIE SURVIVAL")
bg = pygame.image.load("bg.png")
bg = pygame.transform.scale(bg, (screen_width, screen_height))
menu_bg = pygame.image.load("menu.png")
menu_bg = pygame.transform.scale(menu_bg, (screen_width, screen_height))
gameover_bg = pygame.image.load("game_over.png")
gameover_bg = pygame.transform.scale(gameover_bg, (screen_width, screen_height))
victory_bg = pygame.image.load("victory.png")
victory_bg = pygame.transform.scale(victory_bg, (screen_width, screen_height))
win_bg = pygame.image.load("win.png")
win_bg = pygame.transform.scale(win_bg, (screen_width, screen_height))
aid_kit_img = pygame.image.load("aid_kit.png").convert_alpha()
aid_kit_img = pygame.transform.scale(aid_kit_img, (50, 50))


#FONTS :

font = pygame.font.SysFont("comicsans", 20)
damage_texts = []
pause_font = pygame.font.SysFont("Arial", 40, bold=True)
pause_small_font = pygame.font.SysFont("Arial", 22)

#MAIN CHARACTERS:
hero = Hero(x=579, y=365, width=100, height=100)
hero.footstep_sound = footstep_sound
hero.sword_sounds = sword_sounds
zombies = [Zombie(x=0, y=335, width=100, height=100, end=600)]
game_state = {
    "level": 1,
    "wave": 1,
    "boss_spawned": False,
    "in_gameover": False,
    "in_menu": True,
    "in_victory": False,
    "in_win": False,
    "paused": False,
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

def draw_pause_screen():
    overlay = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 150))
    screen.blit(overlay, (0, 0))
    pause_text = pause_font.render("PAUSE", True, WHITE)
    resume_text = pause_small_font.render("Press ESC to Resume", True, WHITE)
    screen.blit(pause_text, (screen_width // 2 - pause_text.get_width() // 2, 180))
    screen.blit(resume_text, (screen_width // 2 - resume_text.get_width() // 2, 260))
    pygame.display.update()

hud_font  = pygame.font.SysFont("Courier New", 11, bold=True)
val_font  = pygame.font.SysFont("Courier New", 13, bold=True)
def draw_hud(screen, hero, score, game_state):
    config = LEVEL_CONFIG[game_state["level"]]

    # خلفية الـ HUD
    hud_surface = pygame.Surface((screen_width, 32), pygame.SRCALPHA)
    hud_surface.fill((0, 0, 0, 170))
    screen.blit(hud_surface, (0, 0))
    pygame.draw.line(screen, (58, 58, 42), (0, 32), (screen_width, 32), 1)


    # ===== HP =====
    x = 10
    lbl = hud_font.render("HP", True, (138, 170, 85))
    screen.blit(lbl, (x, 10))
    x += lbl.get_width() + 6
    pygame.draw.rect(screen, (42, 26, 26), (x, 11, 100, 10))
    pygame.draw.rect(screen, (90, 42, 42), (x, 11, 100, 10), 1)
    hp_w = int(max(0, hero.health) / 100 * 100)
    hp_color = (204, 51, 51) if hero.health > 30 else (255, 100, 0)
    pygame.draw.rect(screen, hp_color, (x, 11, hp_w, 10))
    x += 106
    hp_txt = val_font.render(str(hero.health), True, (204, 85, 85))
    screen.blit(hp_txt, (x, 9))
    x += hp_txt.get_width() + 14

    # ===== LIVES =====
    lbl2 = hud_font.render("LIVES", True, (138, 170, 85))
    screen.blit(lbl2, (x, 10))
    x += lbl2.get_width() + 6
    for i in range(hero.max_lives):
        color = (204, 51, 51) if i < hero.lives else (51, 51, 51)

        heart_pts = [
            (x + 0,  13), (x + 2,  10), (x + 5,  10),
            (x + 7,  13), (x + 9,  10), (x + 12, 10),
            (x + 14, 13), (x + 14, 16), (x + 7,  22),
            (x + 0,  16)
        ]
        pygame.draw.polygon(screen, color, heart_pts)
        x += 18
    x += 10

    # ===== WAVE =====
    lbl3 = hud_font.render("WAVE", True, (138, 170, 85))
    screen.blit(lbl3, (x, 10))
    x += lbl3.get_width() + 6
    wave_txt = val_font.render(
        f"{game_state['wave']}/{config['max_wave']}",
        True, (221, 204, 136)
    )
    screen.blit(wave_txt, (x, 9))
    
    # ===== SCORE =====
    score_lbl = hud_font.render("SCORE", True, (138, 170, 85))
    score_color = (255, 255, 68) if score.flash_timer > 0 else (255, 221, 68)
    score_val = val_font.render(str(score.value).zfill(5), True, score_color)
    sx = screen_width - score_val.get_width() - 10
    slx = sx - score_lbl.get_width() - 6
    screen.blit(score_lbl, (slx, 10))
    screen.blit(score_val, (sx, 9))

    # ===== LEVEL =====
    level_lbl = hud_font.render(
        f"LEVEL {game_state['level']}",
        True, (136, 187, 221)
    )
    lx = screen_width // 2 - level_lbl.get_width() // 2 + 30
    screen.blit(level_lbl, (lx, 10))
    
    # ===== DESCRIPTION ======
    bottom_surface = pygame.Surface((screen_width, 20), pygame.SRCALPHA)
    bottom_surface.fill((0, 0, 0, 150))
    screen.blit(bottom_surface, (0, screen_height - 20))
    ctrl_txt = hud_font.render("ESC: Pause      Space: Jump     <-- -->: Move      A: Attack", True, (80, 100, 70))
    screen.blit(ctrl_txt, (screen_width // 2 - ctrl_txt.get_width() // 2, screen_height - 16))

def drawtheGame():
    screen.blit(bg, (0, 0))
    for zombie in zombies:
        zombie.draw(screen,hero)
    
    if hero.isAttacking:
        hero.draw_attack(screen)
    else:
        hero.draw(screen)

    for text in damage_texts[:]:
        text.draw(screen, font)
        if text.life <= 0:
            damage_texts.remove(text)
              
    if aid_kit:
        screen.blit(aid_kit_img, (aid_kit["x"], aid_kit["y"]))
    draw_hud(screen, hero, score, game_state)   
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
    
final_font = pygame.font.SysFont("Arial", 28, bold=True)

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
        
        final_text = final_font.render("Press any key to return to Menu", True, WHITE)
        screen.blit(final_text, (screen_width // 2 - final_text.get_width() // 2, 460))
    pygame.display.update()

def draw_win_screen():
    global hovered_win_button
    screen.blit(win_bg, (0, 0))
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
aid_kit = None
next_aid_score = 400
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
                    aid_kit = None
                    next_aid_score = 400
                   
                    
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
            import sys
            sys.exit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_state["paused"] = not game_state["paused"]
            
    keys = pygame.key.get_pressed()
    if game_state["paused"]:
        draw_pause_screen()
        continue
    
    # ====================================== HERO ACTIONS ======================================
    if not hero.isDying:
        hero.move(keys,screen_width)
        hero.jump(keys)
        
        current_time = pygame.time.get_ticks()
        for zombie in zombies:
            zombie.check_attack(hero)
            
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
        
    # ====== AID KIT ======
    if score.value >= next_aid_score and aid_kit is None:
        aid_kit = {"x": random.randint(50, 600), "y": 370}
        next_aid_score += 400

    if aid_kit:
        aid_rect = pygame.Rect(aid_kit["x"], aid_kit["y"], 50, 50)
        hero_rect = pygame.Rect(hero.x, hero.y, hero.width, hero.height)
        if aid_rect.colliderect(hero_rect):
            hero.health = 100
            aid_kit = None
        
    score.update()
    drawtheGame()