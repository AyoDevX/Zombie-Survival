import pygame


# ********************************************** MAIN FRAMES ********************************************** #

#                                   ===============  HERO  ===============

# walk #
#==>right
hw_right = [pygame.transform.scale (pygame.image.load("hero/walk/R1.png"), (100,100)),
            pygame.transform.scale (pygame.image.load("hero/walk/R2.png"), (100,100)),
            pygame.transform.scale (pygame.image.load("hero/walk/R3.png"), (100,100)),
            pygame.transform.scale (pygame.image.load("hero/walk/R4.png"), (100,100)),
            pygame.transform.scale (pygame.image.load("hero/walk/R5.png"), (100,100)),
            pygame.transform.scale (pygame.image.load("hero/walk/R6.png"), (100,100)),
            pygame.transform.scale (pygame.image.load("hero/walk/R7.png"), (100,100)),
            pygame.transform.scale (pygame.image.load("hero/walk/R8.png"), (100,100)),
            pygame.transform.scale (pygame.image.load("hero/walk/R9.png"), (100,100)),
            pygame.transform.scale (pygame.image.load("hero/walk/R10.png"), (100,100))]
#==>left
hw_left = [pygame.transform.scale (pygame.image.load("hero/walk/L1.png"),(100,100)),
           pygame.transform.scale (pygame.image.load("hero/walk/L2.png"),(100,100)),
           pygame.transform.scale (pygame.image.load("hero/walk/L3.png"),(100,100)),
           pygame.transform.scale (pygame.image.load("hero/walk/L4.png"),(100,100)),
           pygame.transform.scale (pygame.image.load("hero/walk/L5.png"),(100,100)),
           pygame.transform.scale (pygame.image.load("hero/walk/L6.png"),(100,100)),
           pygame.transform.scale (pygame.image.load("hero/walk/L7.png"),(100,100)),
           pygame.transform.scale (pygame.image.load("hero/walk/L8.png"),(100,100)),
           pygame.transform.scale (pygame.image.load("hero/walk/L9.png"),(100,100)),
           pygame.transform.scale (pygame.image.load("hero/walk/L10.png"),(100,100))]

# attacking #
# "ATTACK 1" #
hero_attack_1 = {
    "right" : [pygame.transform.scale (pygame.image.load("hero/attack1/R1.png"),(100,100)),
             pygame.transform.scale (pygame.image.load("hero/attack1/R2.png"),(100,100)),
             pygame.transform.scale (pygame.image.load("hero/attack1/R3.png"),(100,100)),
             pygame.transform.scale (pygame.image.load("hero/attack1/R4.png"),(100,100)),
             pygame.transform.scale (pygame.image.load("hero/attack1/R5.png"),(100,100)),
             pygame.transform.scale (pygame.image.load("hero/attack1/R6.png"),(100,100)),
             pygame.transform.scale (pygame.image.load("hero/attack1/R7.png"),(100,100))],
    "left" : [pygame.transform.scale (pygame.image.load("hero/attack1/L1.png"),(100,100)),
            pygame.transform.scale (pygame.image.load("hero/attack1/L2.png"),(100,100)),
            pygame.transform.scale (pygame.image.load("hero/attack1/L3.png"),(100,100)),
            pygame.transform.scale (pygame.image.load("hero/attack1/L4.png"),(100,100)),
            pygame.transform.scale (pygame.image.load("hero/attack1/L5.png"),(100,100)),
            pygame.transform.scale (pygame.image.load("hero/attack1/L6.png"),(100,100)),
            pygame.transform.scale (pygame.image.load("hero/attack1/L7.png"),(100,100))] 
}
# "ATTACK 2" #
hero_attack_2 = {
    "right" : [pygame.transform.scale (pygame.image.load("hero/attack2/R1.png"),(100,100)),
             pygame.transform.scale (pygame.image.load("hero/attack2/R2.png"),(100,100)),
             pygame.transform.scale (pygame.image.load("hero/attack2/R3.png"),(100,100)),
             pygame.transform.scale (pygame.image.load("hero/attack2/R4.png"),(100,100)),
             pygame.transform.scale (pygame.image.load("hero/attack2/R5.png"),(100,100)),
             pygame.transform.scale (pygame.image.load("hero/attack2/R6.png"),(100,100)),
             pygame.transform.scale (pygame.image.load("hero/attack2/R7.png"),(100,100)),
             pygame.transform.scale (pygame.image.load("hero/attack2/R8.png"),(100,100))],
    "left" : [pygame.transform.scale (pygame.image.load("hero/attack2/L1.png"),(100,100)),
            pygame.transform.scale (pygame.image.load("hero/attack2/L2.png"),(100,100)),
            pygame.transform.scale (pygame.image.load("hero/attack2/L3.png"),(100,100)),
            pygame.transform.scale (pygame.image.load("hero/attack2/L4.png"),(100,100)),
            pygame.transform.scale (pygame.image.load("hero/attack2/L5.png"),(100,100)),
            pygame.transform.scale (pygame.image.load("hero/attack2/L6.png"),(100,100)),
            pygame.transform.scale (pygame.image.load("hero/attack2/L7.png"),(100,100)),
            pygame.transform.scale (pygame.image.load("hero/attack2/L8.png"),(100,100))]
}
# "ATTACK 3" #
hero_attack_3 = {
    "right" : [pygame.transform.scale (pygame.image.load("hero/attack3/R1.png"),(100,100)),
             pygame.transform.scale (pygame.image.load("hero/attack3/R2.png"),(100,100)),
             pygame.transform.scale (pygame.image.load("hero/attack3/R3.png"),(100,100)),
             pygame.transform.scale (pygame.image.load("hero/attack3/R4.png"),(100,100)),
             pygame.transform.scale (pygame.image.load("hero/attack3/R5.png"),(100,100)),
             pygame.transform.scale (pygame.image.load("hero/attack3/R6.png"),(100,100)),
             pygame.transform.scale (pygame.image.load("hero/attack3/R7.png"),(100,100)),
             pygame.transform.scale (pygame.image.load("hero/attack3/R8.png"),(100,100)),
             pygame.transform.scale (pygame.image.load("hero/attack3/R9.png"),(100,100))],
    "left" : [pygame.transform.scale (pygame.image.load("hero/attack3/L1.png"),(100,100)),
            pygame.transform.scale (pygame.image.load("hero/attack3/L2.png"),(100,100)),
            pygame.transform.scale (pygame.image.load("hero/attack3/L3.png"),(100,100)),
            pygame.transform.scale (pygame.image.load("hero/attack3/L4.png"),(100,100)),
            pygame.transform.scale (pygame.image.load("hero/attack3/L5.png"),(100,100)),
            pygame.transform.scale (pygame.image.load("hero/attack3/L6.png"),(100,100)),
            pygame.transform.scale (pygame.image.load("hero/attack3/L7.png"),(100,100)),
            pygame.transform.scale (pygame.image.load("hero/attack3/L8.png"),(100,100)),
            pygame.transform.scale (pygame.image.load("hero/attack3/L9.png"),(100,100))]
}
# die #
hero_die = {
    "right" : [pygame.transform.scale (pygame.image.load("hero/die/R1.png"),(100,100)),
            pygame.transform.scale (pygame.image.load("hero/die/R2.png"),(100,100)),
            pygame.transform.scale (pygame.image.load("hero/die/R3.png"),(100,100)),
            pygame.transform.scale (pygame.image.load("hero/die/R4.png"),(100,100)),
            pygame.transform.scale (pygame.image.load("hero/die/R5.png"),(100,100)),
            pygame.transform.scale (pygame.image.load("hero/die/R6.png"),(100,100)),
            pygame.transform.scale (pygame.image.load("hero/die/R7.png"),(100,100)),
            pygame.transform.scale (pygame.image.load("hero/die/R8.png"),(100,100)),
            pygame.transform.scale (pygame.image.load("hero/die/R9.png"),(100,100)),
            pygame.transform.scale (pygame.image.load("hero/die/R10.png"),(100,100)),
            pygame.transform.scale (pygame.image.load("hero/die/R11.png"),(100,100)),
            pygame.transform.scale (pygame.image.load("hero/die/R12.png"),(100,100)),
            pygame.transform.scale (pygame.image.load("hero/die/R13.png"),(100,100)),
            pygame.transform.scale (pygame.image.load("hero/die/R14.png"),(100,100)),
            pygame.transform.scale (pygame.image.load("hero/die/R15.png"),(100,100)),
            pygame.transform.scale (pygame.image.load("hero/die/R16.png"),(100,100)),
            pygame.transform.scale (pygame.image.load("hero/die/R17.png"),(100,100)),
            pygame.transform.scale (pygame.image.load("hero/die/R18.png"),(100,100))],
    "left" : [pygame.transform.scale (pygame.image.load("hero/die/L1.png"),(100,100)),
           pygame.transform.scale (pygame.image.load("hero/die/L2.png"),(100,100)),
           pygame.transform.scale (pygame.image.load("hero/die/L3.png"),(100,100)),
           pygame.transform.scale (pygame.image.load("hero/die/L4.png"),(100,100)),
           pygame.transform.scale (pygame.image.load("hero/die/L5.png"),(100,100)),
           pygame.transform.scale (pygame.image.load("hero/die/L6.png"),(100,100)),
           pygame.transform.scale (pygame.image.load("hero/die/L7.png"),(100,100)),
           pygame.transform.scale (pygame.image.load("hero/die/L8.png"),(100,100)),
           pygame.transform.scale (pygame.image.load("hero/die/L9.png"),(100,100)),
           pygame.transform.scale (pygame.image.load("hero/die/L10.png"),(100,100)),
           pygame.transform.scale (pygame.image.load("hero/die/L11.png"),(100,100)),
           pygame.transform.scale (pygame.image.load("hero/die/L12.png"),(100,100)),
           pygame.transform.scale (pygame.image.load("hero/die/L13.png"),(100,100)),
           pygame.transform.scale (pygame.image.load("hero/die/L14.png"),(100,100)),
           pygame.transform.scale (pygame.image.load("hero/die/L15.png"),(100,100)),
           pygame.transform.scale (pygame.image.load("hero/die/L16.png"),(100,100)),
           pygame.transform.scale (pygame.image.load("hero/die/L17.png"),(100,100)),
           pygame.transform.scale (pygame.image.load("hero/die/L18.png"),(100,100))]
}
# hurt #
hero_hurt = {
    "right" : [pygame.transform.scale (pygame.image.load("hero/hurt/R1.png"),(100,100)),
            pygame.transform.scale (pygame.image.load("hero/hurt/R2.png"),(100,100)),
            pygame.transform.scale (pygame.image.load("hero/hurt/R3.png"),(100,100))],
    "left" : [pygame.transform.scale (pygame.image.load("hero/hurt/L1.png"),(100,100)),
           pygame.transform.scale (pygame.image.load("hero/hurt/L2.png"),(100,100)),
           pygame.transform.scale (pygame.image.load("hero/hurt/L3.png"),(100,100))]
}

#                                   ===============  ZOMBIES  ===============                                      #
#---------------- ZOMBIE 1 ----------------#

# walk #
zombie_1_walk = {
    "right" : [pygame.image.load("zombie_1/walk/R1.png"),
pygame.image.load("zombie_1/walk/R2.png"),
pygame.image.load("zombie_1/walk/R3.png"),
pygame.image.load("zombie_1/walk/R4.png"),
pygame.image.load("zombie_1/walk/R5.png"),
pygame.image.load("zombie_1/walk/R6.png"),
pygame.image.load("zombie_1/walk/R7.png"),
pygame.image.load("zombie_1/walk/R8.png"),
pygame.image.load("zombie_1/walk/R9.png"),
pygame.image.load("zombie_1/walk/R10.png")],
    "left" : [pygame.image.load("zombie_1/walk/L1.png"),
pygame.image.load("zombie_1/walk/L2.png"),
pygame.image.load("zombie_1/walk/L3.png"),
pygame.image.load("zombie_1/walk/L4.png"),
pygame.image.load("zombie_1/walk/L5.png"),
pygame.image.load("zombie_1/walk/L6.png"),
pygame.image.load("zombie_1/walk/L7.png"),
pygame.image.load("zombie_1/walk/L8.png"),
pygame.image.load("zombie_1/walk/L9.png"),
pygame.image.load("zombie_1/walk/L10.png")]
}

# attack #
zombie_1_attack = {
    "right" : [pygame.image.load("zombie_1/attack/R1.png"),
pygame.image.load("zombie_1/attack/R2.png"),
pygame.image.load("zombie_1/attack/R3.png"),
pygame.image.load("zombie_1/attack/R4.png"),
pygame.image.load("zombie_1/attack/R5.png")],
    "left" : [pygame.image.load("zombie_1/attack/L1.png"),
pygame.image.load("zombie_1/attack/L2.png"),
pygame.image.load("zombie_1/attack/L3.png"),
pygame.image.load("zombie_1/attack/L4.png"),
pygame.image.load("zombie_1/attack/L5.png")]
}

# die #
zombie_1_die = {
    "right" : [pygame.image.load("zombie_1/die/R1.png"),
pygame.image.load("zombie_1/die/R2.png"),
pygame.image.load("zombie_1/die/R3.png"),
pygame.image.load("zombie_1/die/R4.png"),
pygame.image.load("zombie_1/die/R5.png")],
    "left" : [pygame.image.load("zombie_1/die/L1.png"),
pygame.image.load("zombie_1/die/L2.png"),
pygame.image.load("zombie_1/die/L3.png"),
pygame.image.load("zombie_1/die/L4.png"),
pygame.image.load("zombie_1/die/L5.png")]
}

# hurt #
zombie_1_hurt = {
    "right" : [pygame.image.load("zombie_1/hurt/R1.png"),
pygame.image.load("zombie_1/hurt/R2.png"),
pygame.image.load("zombie_1/hurt/R3.png"),
pygame.image.load("zombie_1/hurt/R4.png")],
    "left" : [pygame.image.load("zombie_1/hurt/L1.png"),
pygame.image.load("zombie_1/hurt/L2.png"),
pygame.image.load("zombie_1/hurt/L3.png"),
pygame.image.load("zombie_1/hurt/L4.png")]
}

#---------------- ZOMBIE 2 ---------------- #

# walk #
zombie_2_walk = {
    "right" : [pygame.image.load("zombie_2/walk/R1.png"),
pygame.image.load("zombie_2/walk/R2.png"),
pygame.image.load("zombie_2/walk/R3.png"),
pygame.image.load("zombie_2/walk/R4.png"),
pygame.image.load("zombie_2/walk/R5.png"),
pygame.image.load("zombie_2/walk/R6.png"),
pygame.image.load("zombie_2/walk/R7.png"),
pygame.image.load("zombie_2/walk/R8.png"),
pygame.image.load("zombie_2/walk/R9.png"),
pygame.image.load("zombie_2/walk/R10.png")],
    "left" : [pygame.image.load("zombie_2/walk/L1.png"),
pygame.image.load("zombie_2/walk/L2.png"),
pygame.image.load("zombie_2/walk/L3.png"),
pygame.image.load("zombie_2/walk/L4.png"),
pygame.image.load("zombie_2/walk/L5.png"),
pygame.image.load("zombie_2/walk/L6.png"),
pygame.image.load("zombie_2/walk/L7.png"),
pygame.image.load("zombie_2/walk/L8.png"),
pygame.image.load("zombie_2/walk/L9.png"),
pygame.image.load("zombie_2/walk/L10.png")]
}

# attack #
zombie_2_attack = {
    "right" : [pygame.image.load("zombie_2/attack/R1.png"),
pygame.image.load("zombie_2/attack/R2.png"),
pygame.image.load("zombie_2/attack/R3.png"),
pygame.image.load("zombie_2/attack/R4.png"),
pygame.image.load("zombie_2/attack/R5.png")],
    "left" : [pygame.image.load("zombie_2/attack/L1.png"),
pygame.image.load("zombie_2/attack/L2.png"),
pygame.image.load("zombie_2/attack/L3.png"),
pygame.image.load("zombie_2/attack/L4.png"),
pygame.image.load("zombie_2/attack/L5.png")]
}

# die #
zombie_2_die = {
    "right" : [pygame.image.load("zombie_2/die/R1.png"),
pygame.image.load("zombie_2/die/R2.png"),
pygame.image.load("zombie_2/die/R3.png"),
pygame.image.load("zombie_2/die/R4.png"),
pygame.image.load("zombie_2/die/R5.png")],
    "left" : [pygame.image.load("zombie_2/die/L1.png"),
pygame.image.load("zombie_2/die/L2.png"),
pygame.image.load("zombie_2/die/L3.png"),
pygame.image.load("zombie_2/die/L4.png"),
pygame.image.load("zombie_2/die/L5.png")]
}

# hurt #
zombie_2_hurt = {
    "right" : [pygame.image.load("zombie_2/hurt/R1.png"),
pygame.image.load("zombie_2/hurt/R2.png"),
pygame.image.load("zombie_2/hurt/R3.png"),
pygame.image.load("zombie_2/hurt/R4.png")],
    "left" : [pygame.image.load("zombie_2/hurt/L1.png"),
pygame.image.load("zombie_2/hurt/L2.png"),
pygame.image.load("zombie_2/hurt/L3.png"),
pygame.image.load("zombie_2/hurt/L4.png")]
}

#---------------- ZOMBIE 3 ---------------- #

# walk #
zombie_3_walk = {
    "right" : [pygame.image.load("zombie_3/walk/R1.png"),
pygame.image.load("zombie_3/walk/R2.png"),
pygame.image.load("zombie_3/walk/R3.png"),
pygame.image.load("zombie_3/walk/R4.png"),
pygame.image.load("zombie_3/walk/R5.png"),
pygame.image.load("zombie_3/walk/R6.png"),
pygame.image.load("zombie_3/walk/R7.png"),
pygame.image.load("zombie_3/walk/R8.png"),
pygame.image.load("zombie_3/walk/R9.png"),
pygame.image.load("zombie_3/walk/R10.png")],
    "left" : [pygame.image.load("zombie_3/walk/L1.png"),
pygame.image.load("zombie_3/walk/L2.png"),
pygame.image.load("zombie_3/walk/L3.png"),
pygame.image.load("zombie_3/walk/L4.png"),
pygame.image.load("zombie_3/walk/L5.png"),
pygame.image.load("zombie_3/walk/L6.png"),
pygame.image.load("zombie_3/walk/L7.png"),
pygame.image.load("zombie_3/walk/L8.png"),
pygame.image.load("zombie_3/walk/L9.png"),
pygame.image.load("zombie_3/walk/L10.png")]
}

# attack #
zombie_3_attack = {
    "right" : [pygame.image.load("zombie_3/attack/R1.png"),
pygame.image.load("zombie_3/attack/R2.png"),
pygame.image.load("zombie_3/attack/R3.png"),
pygame.image.load("zombie_3/attack/R4.png")],
    "left" : [pygame.image.load("zombie_3/attack/L1.png"),
pygame.image.load("zombie_3/attack/L2.png"),
pygame.image.load("zombie_3/attack/L3.png"),
pygame.image.load("zombie_3/attack/L4.png")]
}

# die #
zombie_3_die = {
    "right" : [pygame.image.load("zombie_3/die/R1.png"),
pygame.image.load("zombie_3/die/R2.png"),
pygame.image.load("zombie_3/die/R3.png"),
pygame.image.load("zombie_3/die/R4.png"),
pygame.image.load("zombie_3/die/R5.png")],
    "left" : [pygame.image.load("zombie_3/die/L1.png"),
pygame.image.load("zombie_3/die/L2.png"),
pygame.image.load("zombie_3/die/L3.png"),
pygame.image.load("zombie_3/die/L4.png"),
pygame.image.load("zombie_3/die/L5.png")]
}

# hurt #
zombie_3_hurt = {
    "right" : [pygame.image.load("zombie_3/hurt/R1.png"),
pygame.image.load("zombie_3/hurt/R2.png"),
pygame.image.load("zombie_3/hurt/R3.png"),
pygame.image.load("zombie_3/hurt/R4.png")],
    "left" : [pygame.image.load("zombie_3/hurt/L1.png"),
pygame.image.load("zombie_3/hurt/L2.png"),
pygame.image.load("zombie_3/hurt/L3.png"),
pygame.image.load("zombie_3/hurt/L4.png")]
}

#---------------- ZOMBIE BOSS ---------------- #

# walk #
zombie_boss_walk = {
    "right" : [pygame.transform.scale (pygame.image.load("zombie_boss/walk/R1.png"),(200,200)),
pygame.transform.scale (pygame.image.load("zombie_boss/walk/R2.png"),(200,200)),
pygame.transform.scale (pygame.image.load("zombie_boss/walk/R3.png"),(200,200)),
pygame.transform.scale (pygame.image.load("zombie_boss/walk/R4.png"),(200,200)),
pygame.transform.scale (pygame.image.load("zombie_boss/walk/R5.png"),(200,200)),
pygame.transform.scale (pygame.image.load("zombie_boss/walk/R6.png"),(200,200)),
pygame.transform.scale (pygame.image.load("zombie_boss/walk/R7.png"),(200,200)),
pygame.transform.scale (pygame.image.load("zombie_boss/walk/R8.png"),(200,200)),
pygame.transform.scale (pygame.image.load("zombie_boss/walk/R9.png"),(200,200)),
pygame.transform.scale (pygame.image.load("zombie_boss/walk/R10.png"),(200,200)),
pygame.transform.scale (pygame.image.load("zombie_boss/walk/R11.png"),(200,200)),
pygame.transform.scale (pygame.image.load("zombie_boss/walk/R12.png"),(200,200))],
    "left" : [pygame.transform.scale (pygame.image.load("zombie_boss/walk/L1.png"),(200,200)),
pygame.transform.scale (pygame.image.load("zombie_boss/walk/L2.png"),(200,200)),
pygame.transform.scale (pygame.image.load("zombie_boss/walk/L3.png"),(200,200)),
pygame.transform.scale (pygame.image.load("zombie_boss/walk/L4.png"),(200,200)),
pygame.transform.scale (pygame.image.load("zombie_boss/walk/L5.png"),(200,200)),
pygame.transform.scale (pygame.image.load("zombie_boss/walk/L6.png"),(200,200)),
pygame.transform.scale (pygame.image.load("zombie_boss/walk/L7.png"),(200,200)),
pygame.transform.scale (pygame.image.load("zombie_boss/walk/L8.png"),(200,200)),
pygame.transform.scale (pygame.image.load("zombie_boss/walk/L9.png"),(200,200)),
pygame.transform.scale (pygame.image.load("zombie_boss/walk/L10.png"),(200,200)),
pygame.transform.scale (pygame.image.load("zombie_boss/walk/L11.png"),(200,200)),
pygame.transform.scale (pygame.image.load("zombie_boss/walk/L12.png"),(200,200))]
}

# attack #
zombie_boss_attack = {
    "right" : [pygame.transform.scale (pygame.image.load("zombie_boss/attack/R1.png"),(200,200)),
    pygame.transform.scale (pygame.image.load("zombie_boss/attack/R2.png"),(200,200)),
    pygame.transform.scale (pygame.image.load("zombie_boss/attack/R3.png"),(200,200)),
    pygame.transform.scale (pygame.image.load("zombie_boss/attack/R4.png"),(200,200)),
    pygame.transform.scale (pygame.image.load("zombie_boss/attack/R5.png"),(200,200)),
    pygame.transform.scale (pygame.image.load("zombie_boss/attack/R6.png"),(200,200)),
    pygame.transform.scale (pygame.image.load("zombie_boss/attack/R7.png"),(200,200)),
    pygame.transform.scale (pygame.image.load("zombie_boss/attack/R8.png"),(200,200)),
    pygame.transform.scale (pygame.image.load("zombie_boss/attack/R9.png"),(200,200)),
    pygame.transform.scale (pygame.image.load("zombie_boss/attack/R10.png"),(200,200))],
    "left" : [pygame.transform.scale (pygame.image.load("zombie_boss/attack/L1.png"),(200,200)),
    pygame.transform.scale (pygame.image.load("zombie_boss/attack/L2.png"),(200,200)),
    pygame.transform.scale (pygame.image.load("zombie_boss/attack/L3.png"),(200,200)),
    pygame.transform.scale (pygame.image.load("zombie_boss/attack/L4.png"),(200,200)),
    pygame.transform.scale (pygame.image.load("zombie_boss/attack/L5.png"),(200,200)),
    pygame.transform.scale (pygame.image.load("zombie_boss/attack/L6.png"),(200,200)),
    pygame.transform.scale (pygame.image.load("zombie_boss/attack/L7.png"),(200,200)),
    pygame.transform.scale (pygame.image.load("zombie_boss/attack/L8.png"),(200,200)),
    pygame.transform.scale (pygame.image.load("zombie_boss/attack/L9.png"),(200,200)),
    pygame.transform.scale (pygame.image.load("zombie_boss/attack/L10.png"),(200,200))]
}

# die #
zombie_boss_die = {
    "right" : [pygame.transform.scale (pygame.image.load("zombie_boss/die/R1.png"),(200,200)),
               pygame.transform.scale (pygame.image.load("zombie_boss/die/R2.png"),(200,200)),
               pygame.transform.scale (pygame.image.load("zombie_boss/die/R3.png"),(200,200)),
               pygame.transform.scale (pygame.image.load("zombie_boss/die/R4.png"),(200,200)),
               pygame.transform.scale (pygame.image.load("zombie_boss/die/R5.png"),(200,200))],
    "left" : [pygame.transform.scale (pygame.image.load("zombie_boss/die/L1.png"),(200,200)),
               pygame.transform.scale (pygame.image.load("zombie_boss/die/L2.png"),(200,200)),
               pygame.transform.scale (pygame.image.load("zombie_boss/die/L3.png"),(200,200)),
               pygame.transform.scale (pygame.image.load("zombie_boss/die/L4.png"),(200,200)),
               pygame.transform.scale (pygame.image.load("zombie_boss/die/L5.png"),(200,200))]
}

# hurt # 
zombie_boss_hurt = {
    "right" : [pygame.transform.scale (pygame.image.load("zombie_boss/hurt/R1.png"),(200,200)),
               pygame.transform.scale (pygame.image.load("zombie_boss/hurt/R2.png"),(200,200)),
               pygame.transform.scale (pygame.image.load("zombie_boss/hurt/R3.png"),(200,200)),
               pygame.transform.scale (pygame.image.load("zombie_boss/hurt/R4.png"),(200,200))],
    "left" : [pygame.transform.scale (pygame.image.load("zombie_boss/hurt/L1.png"),(200,200)),
               pygame.transform.scale (pygame.image.load("zombie_boss/hurt/L2.png"),(200,200)),
               pygame.transform.scale (pygame.image.load("zombie_boss/hurt/L3.png"),(200,200)),
               pygame.transform.scale (pygame.image.load("zombie_boss/hurt/L4.png"),(200,200))]
}
               


# ********************************************** MAIN LISTS ********************************************** #
#Hero lists:
hero_types_attack = [hero_attack_1, hero_attack_2, hero_attack_3]
#Zombie lists:
zombies_types_walk = [zombie_1_walk, zombie_2_walk, zombie_3_walk]
zombies_types_attack = [zombie_1_attack, zombie_2_attack, zombie_3_attack]
zombies_types_die = [zombie_1_die, zombie_2_die, zombie_3_die]
zombies_types_hurt = [zombie_1_hurt, zombie_2_hurt, zombie_3_hurt]
boss_types_walk = [zombie_boss_walk]
boss_types_attack = [zombie_boss_attack]
boss_types_die = [zombie_boss_die]
boss_types_hurt = [zombie_boss_hurt]



    
# JUMP - Sprite Sheet
_jump_sheet = pygame.image.load("hero/jump_sheet.png")
_frame_count = 6
_frame_w = _jump_sheet.get_width() // _frame_count
_frame_h = _jump_sheet.get_height()
hero_jump = {"right": [], "left": []}
for i in range(_frame_count):
    frame = _jump_sheet.subsurface((_frame_w * i, 0, _frame_w, _frame_h))
    frame = pygame.transform.scale(frame, (100, 100))
    hero_jump["right"].append(frame)
    hero_jump["left"].append(pygame.transform.flip(frame, True, False))