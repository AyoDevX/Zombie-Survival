import pygame

# ********************************************** MAIN FRAMES ********************************************** #

#                                   ===============  HERO  ===============
# ATTACK1 - Sprite Sheet
_attack1_sheet = pygame.image.load("hero/attack_1_sheet.png")
_frame_attack1_count = 7
_frame_attack1_width = _attack1_sheet.get_width() // _frame_attack1_count
_frame_attack1_height = _attack1_sheet.get_height()
hero_attack_1 = {"right" : [], "left" : []}
for i in range(_frame_attack1_count):
    frame_of_attack1 = _attack1_sheet.subsurface(_frame_attack1_width * i, 0 , _frame_attack1_width, _frame_attack1_height)
    frame_of_attack1 = pygame.transform.scale(frame_of_attack1,(100,100))
    hero_attack_1["right"].append(frame_of_attack1)
    hero_attack_1["left"].append(pygame.transform.flip(frame_of_attack1,True,False))
# ATTACK2 - Sprite Sheet
_attack2_sheet = pygame.image.load("hero/attack_2_sheet.png")
_frame_attack2_count = 8
_frame_attack2_width = _attack2_sheet.get_width() // _frame_attack2_count
_frame_attack2_height = _attack2_sheet.get_height()
hero_attack_2 = {"right" : [], "left" : []}
for i in range(_frame_attack2_count):
    frame_of_attack2 = _attack2_sheet.subsurface(_frame_attack2_width * i, 0 , _frame_attack2_width, _frame_attack2_height)
    frame_of_attack2 = pygame.transform.scale(frame_of_attack2,(100,100))
    hero_attack_2["right"].append(frame_of_attack2)
    hero_attack_2["left"].append(pygame.transform.flip(frame_of_attack2,True,False))
# ATTACK3 - Sprite Sheet
_attack3_sheet = pygame.image.load("hero/attack_3_sheet.png")
_frame_attack3_count = 9
_frame_attack3_width = _attack3_sheet.get_width() // _frame_attack3_count
_frame_attack3_height = _attack3_sheet.get_height()
hero_attack_3 = {"right" : [], "left" : []}
for i in range(_frame_attack3_count):
    frame_of_attack3 = _attack3_sheet.subsurface(_frame_attack3_width * i, 0 , _frame_attack3_width, _frame_attack3_height)
    frame_of_attack3 = pygame.transform.scale(frame_of_attack3,(100,100))
    hero_attack_3["right"].append(frame_of_attack3)
    hero_attack_3["left"].append(pygame.transform.flip(frame_of_attack2,True,False))
# WALK - Sprite Sheet
_walk_sheet = pygame.image.load("hero/walk_sheet.png")
_frame_walk_count = 10
_frame_walk_width = _walk_sheet.get_width() // _frame_walk_count
_frame_walk_height = _walk_sheet.get_height()
hero_walk = {"right" : [], "left" : []}
for i in range(_frame_walk_count):
    frame_of_walk = _walk_sheet.subsurface(_frame_walk_width * i, 0 , _frame_walk_width, _frame_walk_height)
    frame_of_walk = pygame.transform.scale(frame_of_walk,(100,100))
    hero_walk["right"].append(frame_of_walk)
    hero_walk["left"].append(pygame.transform.flip(frame_of_walk,True,False))
# DIE - Sprite Sheet
_die_sheet = pygame.image.load("hero/die_sheet.png")
_frame_die_count = 18
_frame_die_width = _die_sheet.get_width() // _frame_die_count
_frame_die_height = _die_sheet.get_height()
hero_die = {"right" : [], "left" : []}
for i in range(_frame_die_count):
    frame_of_die = _die_sheet.subsurface(_frame_die_width * i, 0 , _frame_die_width, _frame_die_height)
    frame_of_die = pygame.transform.scale(frame_of_die,(100,100))
    hero_die["right"].append(frame_of_die)
    hero_die["left"].append(pygame.transform.flip(frame_of_die,True,False))
# JUMP - Sprite Sheet
_jump_sheet = pygame.image.load("hero/jump_sheet.png")
_frame_jump_count = 6
_frame_jump_width = _jump_sheet.get_width() // _frame_jump_count
_frame_jump_height = _jump_sheet.get_height()
hero_jump = {"right": [], "left": []}
for i in range(_frame_jump_count):
    frame_of_jump = _jump_sheet.subsurface((_frame_jump_width * i, 0, _frame_jump_width, _frame_jump_height))
    frame_of_jump = pygame.transform.scale(frame_of_jump, (100, 100))
    hero_jump["right"].append(frame_of_jump)
    hero_jump["left"].append(pygame.transform.flip(frame_of_jump, True, False))
# HURT - Sprite Sheet
_hurt_sheet = pygame.image.load("hero/hurt_sheet.png")
_frame_hurt_count = 3
_frame_hurt_width = _hurt_sheet.get_width() // _frame_hurt_count
_frame_hurt_height = _hurt_sheet.get_height()
hero_hurt = {"right" : [] , "left" : []}
for i in range(_frame_hurt_count):
    frame_of_hurt = _hurt_sheet.subsurface(_frame_hurt_width * i , 0 , _frame_hurt_width, _frame_hurt_height)
    frame_of_hurt = pygame.transform.scale(frame_of_hurt,(100,100))
    hero_hurt["right"].append(frame_of_hurt)
    hero_hurt["left"].append(pygame.transform.flip(frame_of_hurt,True,False))
    
    
#                                   ===============  ZOMBIES  ===============                                      #
#---------------- ZOMBIE 1 ----------------#
# WALK - Sprite Sheet
_z1_walksheet = pygame.image.load("zombie_1/walk_sheet.png")
_z1_frame_walk_Count = 10
_z1_walkwidth = _z1_walksheet.get_width() // _z1_frame_walk_Count
_z1_walkheight = _z1_walksheet.get_height()
zombie_1_walk = {"right" : [] , "left" : []}
for i in range(_z1_frame_walk_Count):
    z1_frame_of_walk = _z1_walksheet.subsurface(_z1_walkwidth * i , 0 , _z1_walkwidth, _z1_walkheight)
    zombie_1_walk["right"].append(z1_frame_of_walk)
    zombie_1_walk["left"].append(pygame.transform.flip(z1_frame_of_walk,True,False))
# ATTACK - Sprite Sheet
_z1_attacksheet = pygame.image.load("zombie_1/attack_sheet.png")
_z1_frame_attack_Count = 5
_z1_attackwidth = _z1_attacksheet.get_width() // _z1_frame_attack_Count
_z1_attackheight = _z1_attacksheet.get_height()
zombie_1_attack = {"right" : [] , "left" : []}
for i in range(_z1_frame_attack_Count):
    z1_frame_of_attack = _z1_attacksheet.subsurface(_z1_attackwidth * i , 0 , _z1_attackwidth, _z1_attackheight)
    zombie_1_attack["right"].append(z1_frame_of_attack)
    zombie_1_attack["left"].append(pygame.transform.flip(z1_frame_of_attack,True,False))
# HURT - Sprite Sheet
_z1_hurtsheet = pygame.image.load("zombie_1/hurt_sheet.png")
_z1_frame_hurt_Count = 4
_z1_hurtwidth = _z1_hurtsheet.get_width() // _z1_frame_hurt_Count
_z1_hurtheight = _z1_hurtsheet.get_height()
zombie_1_hurt = {"right" : [] , "left" : []}
for i in range(_z1_frame_hurt_Count):
    z1_frame_of_hurt = _z1_hurtsheet.subsurface(_z1_hurtwidth * i , 0 , _z1_hurtwidth, _z1_hurtheight)
    zombie_1_hurt["right"].append(z1_frame_of_hurt)
    zombie_1_hurt["left"].append(pygame.transform.flip(z1_frame_of_hurt,True,False))
# DIE - Sprite Sheet
_z1_diesheet = pygame.image.load("zombie_1/die_sheet.png")
_z1_frame_die_Count = 5
_z1_diewidth = _z1_diesheet.get_width() // _z1_frame_die_Count
_z1_dieheight = _z1_diesheet.get_height()
zombie_1_die = {"right" : [] , "left" : []}
for i in range(_z1_frame_die_Count):
    z1_frame_of_die = _z1_diesheet.subsurface(_z1_diewidth * i , 0 , _z1_diewidth, _z1_dieheight)
    zombie_1_die["right"].append(z1_frame_of_die)
    zombie_1_die["left"].append(pygame.transform.flip(z1_frame_of_die,True,False))
#---------------- ZOMBIE 2 ----------------#
# WALK - Sprite Sheet
_z2_walksheet = pygame.image.load("zombie_2/walk_sheet.png")
_z2_frame_walk_Count = 10
_z2_walkwidth = _z2_walksheet.get_width() // _z2_frame_walk_Count
_z2_walkheight = _z2_walksheet.get_height()
zombie_2_walk = {"right" : [] , "left" : []}
for i in range(_z2_frame_walk_Count):
    z2_frame_of_walk = _z2_walksheet.subsurface(_z2_walkwidth * i , 0 , _z2_walkwidth, _z2_walkheight)
    zombie_2_walk["right"].append(z2_frame_of_walk)
    zombie_2_walk["left"].append(pygame.transform.flip(z2_frame_of_walk,True,False))
# ATTACK - Sprite Sheet
_z2_attacksheet = pygame.image.load("zombie_2/attack_sheet.png")
_z2_frame_attack_Count = 5
_z2_attackwidth = _z2_attacksheet.get_width() // _z2_frame_attack_Count
_z2_attackheight = _z2_attacksheet.get_height()
zombie_2_attack = {"right" : [] , "left" : []}
for i in range(_z2_frame_attack_Count):
    z2_frame_of_attack = _z2_attacksheet.subsurface(_z2_attackwidth * i , 0 , _z2_attackwidth, _z2_attackheight)
    zombie_2_attack["right"].append(z2_frame_of_attack)
    zombie_2_attack["left"].append(pygame.transform.flip(z2_frame_of_attack,True,False))
# HURT - Sprite Sheet
_z2_hurtsheet = pygame.image.load("zombie_2/hurt_sheet.png")
_z2_frame_hurt_Count = 4
_z2_hurtwidth = _z2_hurtsheet.get_width() // _z2_frame_hurt_Count
_z2_hurtheight = _z2_hurtsheet.get_height()
zombie_2_hurt = {"right" : [] , "left" : []}
for i in range(_z2_frame_hurt_Count):
    z2_frame_of_hurt = _z2_hurtsheet.subsurface(_z2_hurtwidth * i , 0 , _z2_hurtwidth, _z2_hurtheight)
    zombie_2_hurt["right"].append(z2_frame_of_hurt)
    zombie_2_hurt["left"].append(pygame.transform.flip(z2_frame_of_hurt,True,False))
# DIE - Sprite Sheet
_z2_diesheet = pygame.image.load("zombie_2/die_sheet.png")
_z2_frame_die_Count = 5
_z2_diewidth = _z2_diesheet.get_width() // _z2_frame_die_Count
_z2_dieheight = _z2_diesheet.get_height()
zombie_2_die = {"right" : [] , "left" : []}
for i in range(_z2_frame_die_Count):
    z2_frame_of_die = _z2_diesheet.subsurface(_z2_diewidth * i , 0 , _z2_diewidth, _z2_dieheight)
    zombie_2_die["right"].append(z2_frame_of_die)
    zombie_2_die["left"].append(pygame.transform.flip(z2_frame_of_die,True,False))
#---------------- ZOMBIE 3 ----------------#
# WALK - Sprite Sheet
_z3_walksheet = pygame.image.load("zombie_3/walk_sheet.png")
_z3_frame_walk_Count = 10
_z3_walkwidth = _z3_walksheet.get_width() // _z3_frame_walk_Count
_z3_walkheight = _z3_walksheet.get_height()
zombie_3_walk = {"right" : [] , "left" : []}
for i in range(_z3_frame_walk_Count):
    z3_frame_of_walk = _z3_walksheet.subsurface(_z3_walkwidth * i , 0 , _z3_walkwidth, _z3_walkheight)
    zombie_3_walk["right"].append(z3_frame_of_walk)
    zombie_3_walk["left"].append(pygame.transform.flip(z3_frame_of_walk,True,False))
# ATTACK - Sprite Sheet
_z3_attacksheet = pygame.image.load("zombie_3/attack_sheet.png")
_z3_frame_attack_Count = 4
_z3_attackwidth = _z3_attacksheet.get_width() // _z3_frame_attack_Count
_z3_attackheight = _z3_attacksheet.get_height()
zombie_3_attack = {"right" : [] , "left" : []}
for i in range(_z3_frame_attack_Count):
    z3_frame_of_attack = _z3_attacksheet.subsurface(_z3_attackwidth * i , 0 , _z3_attackwidth, _z3_attackheight)
    zombie_3_attack["right"].append(z3_frame_of_attack)
    zombie_3_attack["left"].append(pygame.transform.flip(z3_frame_of_attack,True,False))
# HURT - Sprite Sheet
_z3_hurtsheet = pygame.image.load("zombie_3/hurt_sheet.png")
_z3_frame_hurt_Count = 4
_z3_hurtwidth = _z3_hurtsheet.get_width() // _z3_frame_hurt_Count
_z3_hurtheight = _z3_hurtsheet.get_height()
zombie_3_hurt = {"right" : [] , "left" : []}
for i in range(_z3_frame_hurt_Count):
    z3_frame_of_hurt = _z3_hurtsheet.subsurface(_z3_hurtwidth * i , 0 , _z3_hurtwidth, _z3_hurtheight)
    zombie_3_hurt["right"].append(z3_frame_of_hurt)
    zombie_3_hurt["left"].append(pygame.transform.flip(z3_frame_of_hurt,True,False))
# DIE - Sprite Sheet
_z3_diesheet = pygame.image.load("zombie_3/die_sheet.png")
_z3_frame_die_Count = 5
_z3_diewidth = _z3_diesheet.get_width() // _z3_frame_die_Count
_z3_dieheight = _z3_diesheet.get_height()
zombie_3_die = {"right" : [] , "left" : []}
for i in range(_z3_frame_die_Count):
    z3_frame_of_die = _z3_diesheet.subsurface(_z3_diewidth * i , 0 , _z3_diewidth, _z3_dieheight)
    zombie_3_die["right"].append(z3_frame_of_die)
    zombie_3_die["left"].append(pygame.transform.flip(z3_frame_of_die,True,False))
#---------------- ZOMBIE BOSS ----------------#
# WALK - Sprite Sheet
_zb_walksheet = pygame.image.load("zombie_boss/walk_sheet.png")
_zb_frame_walk_Count = 12
_zb_walkwidth = _zb_walksheet.get_width() // _zb_frame_walk_Count
_zb_walkheight = _zb_walksheet.get_height()
zombie_boss_walk = {"right" : [] , "left" : []}
for i in range(_zb_frame_walk_Count):
    zb_frame_of_walk = _zb_walksheet.subsurface(_zb_walkwidth * i , 0 , _zb_walkwidth, _zb_walkheight)
    zb_frame_of_walk = pygame.transform.scale(zb_frame_of_walk,(200,200))
    zombie_boss_walk["right"].append(zb_frame_of_walk)
    zombie_boss_walk["left"].append(pygame.transform.flip(zb_frame_of_walk,True,False))
# ATTACK - Sprite Sheet
_zb_attacksheet = pygame.image.load("zombie_boss/attack_sheet.png")
_zb_frame_attack_Count = 10
_zb_attackwidth = _zb_attacksheet.get_width() // _zb_frame_attack_Count
_zb_attackheight = _zb_attacksheet.get_height()
zombie_boss_attack = {"right" : [] , "left" : []}
for i in range(_zb_frame_attack_Count):
    zb_frame_of_attack = _zb_attacksheet.subsurface(_zb_attackwidth * i , 0 , _zb_attackwidth, _zb_attackheight)
    zb_frame_of_attack = pygame.transform.scale(zb_frame_of_attack,(200,200))
    zombie_boss_attack["right"].append(zb_frame_of_attack)
    zombie_boss_attack["left"].append(pygame.transform.flip(zb_frame_of_attack,True,False))
# HURT - Sprite Sheet
_zb_hurtsheet = pygame.image.load("zombie_boss/hurt_sheet.png")
_zb_frame_hurt_Count = 4
_zb_hurtwidth = _zb_hurtsheet.get_width() // _zb_frame_hurt_Count
_zb_hurtheight = _zb_hurtsheet.get_height()
zombie_boss_hurt = {"right" : [] , "left" : []}
for i in range(_zb_frame_hurt_Count):
    zb_frame_of_hurt = _zb_hurtsheet.subsurface(_zb_hurtwidth * i , 0 , _zb_hurtwidth, _zb_hurtheight)
    zb_frame_of_hurt = pygame.transform.scale(zb_frame_of_hurt,(200,200))
    zombie_boss_hurt["right"].append(zb_frame_of_hurt)
    zombie_boss_hurt["left"].append(pygame.transform.flip(zb_frame_of_hurt,True,False))
# DIE - Sprite Sheet
_zb_diesheet = pygame.image.load("zombie_boss/die_sheet.png")
_zb_frame_die_Count = 5
_zb_diewidth = _zb_diesheet.get_width() // _zb_frame_die_Count
_zb_dieheight = _zb_diesheet.get_height()
zombie_boss_die = {"right" : [] , "left" : []}
for i in range(_zb_frame_die_Count):
    zb_frame_of_die = _zb_diesheet.subsurface(_zb_diewidth * i , 0 , _zb_diewidth, _zb_dieheight)
    zb_frame_of_die = pygame.transform.scale(zb_frame_of_die,(200,200))
    zombie_boss_die["right"].append(zb_frame_of_die)
    zombie_boss_die["left"].append(pygame.transform.flip(zb_frame_of_die,True,False))
    
    
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