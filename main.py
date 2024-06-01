from variables import *

def rotateTank():
    global tank
    global square
    global angle
    player_pos = square.center
    player_rect = tank.get_rect(center=player_pos)
    mx, my = pygame.mouse.get_pos()
    dx, dy = mx - player_rect.centerx, my - player_rect.centery
    angle = math.degrees(math.atan2(-dy, dx))
    rot_image = pygame.transform.rotate(tank, angle)
    rot_image_rect = rot_image.get_rect(center=player_rect.center)
    screen.blit(rot_image, rot_image_rect.topleft)

def drawBullets():
    global bullets
    for bullet in bullets:
        bullet['pos'][0] += bullet['xfactor']
        bullet['pos'][1] += bullet['yfactor']
        screen.blit(bullet['img'], bullet['pos'])
        if bullet['pos'][0] > 1280 or bullet['pos'][0] < 0 or bullet['pos'][1] > 720 or bullet['pos'][1] < 0:
            bullets.remove(bullet)

def rotateBullet(img, angle):
    return pygame.transform.rotate(img, angle-90)

def createBullet(pos, angle):
    global bulletImg
    dx = pos[0] - (square.x + 25)
    dy = pos[1] - (square.y + 25)
    distance = math.sqrt(dx**2 + dy**2)
    unitX = dx / distance
    unitY = dy / distance
    xfactor = unitX * bullet_speed
    yfactor = unitY * bullet_speed
    bullet_pos = [square.x + 25, square.y + 25]
    bullet_img = rotateBullet(bulletImg.copy(), angle)
    bullets.append({'pos': bullet_pos, 'xfactor': xfactor, 'yfactor': yfactor, 'img': bullet_img})

def createEnemies(number, hp):
        
    tank_limit = (square.x, square.y, square.x + 70, square.y + 50)
    enemies_limits.append(tank_limit)
    
    for _ in range(number):
        while True:
            enemy_position = (random.randint(0, 1230), random.randint(0, 670))
            enemy_hitbox = (enemy_position[0], enemy_position[1], enemy_position[0] + 50, enemy_position[1] + 50)
            
            collision = False
            for limit in enemies_limits:
                if enemy_hitbox[2] > limit[0] and enemy_hitbox[0] < limit[2] and enemy_hitbox[3] > limit[1] and enemy_hitbox[1] < limit[3]:
                    collision = True
                    break
            
            if not collision:
                enemies.append({'pos': enemy_position, 'hp': hp})
                enemies_limits.append(enemy_hitbox)
                break
        

def drawEnemies():
    for enemy in enemies:
        screen.blit(enemyImg, enemy['pos'])


createEnemies(10, 1)

pygame.init()
pygame.mouse.set_visible(False)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("#706340")
    mouse_pos = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()

    if keys[pygame.K_s] and square.y <= 720 - 64:
        square.y += tank_speed
    if keys[pygame.K_d] and square.x <= 1280 - 74:
        square.x += tank_speed
    if keys[pygame.K_w] and square.y >= 14:
        square.y -= tank_speed
    if keys[pygame.K_a] and square.x >= 4:
        square.x -= tank_speed

    current_time = time.time()
    if event.type == pygame.MOUSEBUTTONDOWN and current_time - last_shot_time > cooldown:
        createBullet(mouse_pos, angle)
        last_shot_time = current_time

    drawBullets()
    drawEnemies()
    rotateTank()

    screen.blit(cursor, (mouse_pos[0] - 20, mouse_pos[1] - 20))

    pygame.display.flip()
    clock.tick(60)
pygame.quit()
