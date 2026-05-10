import pygame

def load_sheet(path, frame_count, size=None):
    sheet = pygame.image.load(path)
    fw = sheet.get_width() // frame_count
    fh = sheet.get_height()
    result = {"right": [], "left": []}
    for i in range(frame_count):
        frame = sheet.subsurface(fw * i, 0, fw, fh)
        if size:
            frame = pygame.transform.scale(frame, size)
        result["right"].append(frame)
        result["left"].append(pygame.transform.flip(frame, True, False))
        
    return result

# ********************************************** MAIN FRAMES ********************************************** #
# ===== HERO =====

hero_attack_1 = load_sheet("hero/attack_1_sheet.png", 7, (100, 100))
hero_attack_2 = load_sheet("hero/attack_2_sheet.png", 8, (100, 100))
hero_attack_3 = load_sheet("hero/attack_3_sheet.png", 9, (100, 100))
hero_walk     = load_sheet("hero/walk_sheet.png",     10, (100, 100))
hero_die      = load_sheet("hero/die_sheet.png",      18, (100, 100))
hero_jump     = load_sheet("hero/jump_sheet.png",      6, (100, 100))
hero_hurt     = load_sheet("hero/hurt_sheet.png",      3, (100, 100))

# ===== ZOMBIE 1 =====
zombie_1_walk   = load_sheet("zombie_1/walk_sheet.png",   10)
zombie_1_attack = load_sheet("zombie_1/attack_sheet.png",  5)
zombie_1_hurt   = load_sheet("zombie_1/hurt_sheet.png",    4)
zombie_1_die    = load_sheet("zombie_1/die_sheet.png",     5)

# ===== ZOMBIE 2 =====
zombie_2_walk   = load_sheet("zombie_2/walk_sheet.png",   10)
zombie_2_attack = load_sheet("zombie_2/attack_sheet.png",  5)
zombie_2_hurt   = load_sheet("zombie_2/hurt_sheet.png",    4)
zombie_2_die    = load_sheet("zombie_2/die_sheet.png",     5)

# ===== ZOMBIE 3 =====
zombie_3_walk   = load_sheet("zombie_3/walk_sheet.png",   10)
zombie_3_attack = load_sheet("zombie_3/attack_sheet.png",  4)
zombie_3_hurt   = load_sheet("zombie_3/hurt_sheet.png",    4)
zombie_3_die    = load_sheet("zombie_3/die_sheet.png",     5)

# ===== ZOMBIE BOSS =====
zombie_boss_walk   = load_sheet("zombie_boss/walk_sheet.png",   12, (200, 200))
zombie_boss_attack = load_sheet("zombie_boss/attack_sheet.png", 10, (200, 200))
zombie_boss_hurt   = load_sheet("zombie_boss/hurt_sheet.png",    4, (200, 200))
zombie_boss_die    = load_sheet("zombie_boss/die_sheet.png",     5, (200, 200))

# ********************************************** MAIN LISTS ********************************************** #
#Hero lists:
hero_types_attack = [hero_attack_1, hero_attack_2, hero_attack_3]

#Zombie lists:
zombies_types_walk = [zombie_1_walk, zombie_2_walk, zombie_3_walk]
zombies_types_attack = [zombie_1_attack, zombie_2_attack, zombie_3_attack]
zombies_types_die = [zombie_1_die, zombie_2_die, zombie_3_die]
zombies_types_hurt = [zombie_1_hurt, zombie_2_hurt, zombie_3_hurt]

#zombie boss :
boss_types_walk = [zombie_boss_walk]
boss_types_attack = [zombie_boss_attack]
boss_types_die = [zombie_boss_die]
boss_types_hurt = [zombie_boss_hurt]