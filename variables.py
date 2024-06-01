import pygame
import math
import time
import random

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Tanks Annihilation')

clock = pygame.time.Clock()
running = True

bullet_speed = 10
tank_speed = 2

square = pygame.Rect(1280/2-70, 720/2-50, 70, 50)
tank_source = pygame.image.load('images/tank.png').convert_alpha()
tank = pygame.transform.smoothscale(tank_source, (square.width, square.height))

tankIcon = pygame.image.load('images/tankIcon.png').convert_alpha()
tankIcon = pygame.transform.scale(tankIcon, (50, 50))

pygame.display.set_icon(tankIcon)

cursor_source = pygame.image.load('images/target.png').convert_alpha()
cursor = pygame.transform.scale(cursor_source, (40, 40))

bulletImg = pygame.image.load("images/tank_ammo.png")
bulletImg = pygame.transform.scale(bulletImg, (10, 27.24))

bullets = []
enemies = []
enemies_limits = []


enemyImg = pygame.image.load('images/enemyTank.png').convert_alpha()
enemyImg = pygame.transform.scale(enemyImg, (50, 50))

last_shot_time = 0
cooldown = 0.5 

pointsEarn = True
end = False
points = 0
enemyIsAlive = True
enemyHit = False

mouse_pos = pygame.mouse.get_pos()
keys = pygame.key.get_pressed()

squareCenterX = square.x + 25
squareCenterY = square.y + 25
angle = 0
