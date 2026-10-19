import pygame
import math

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("RL Agent Simulation")
clock = pygame.time.Clock()

running = True
font = pygame.font.SysFont("Consolas", 20)

x,y = 400, 300
angle = 0
car_speed = 0
dt = 0

ACCEL = 300
BRAKE = 400
FRICTION = 150
MAX_SPEED = 400
TURN_SPEED = 150

car_image = pygame.Surface((50, 30), pygame.SRCALPHA)
car_image.fill((0, 255, 255))
pygame.draw.rect(car_image, (255, 255, 255), (40, 0, 10, 30))

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
             running = False
             
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] or keys[pygame.K_w]:
        car_speed += ACCEL * dt
    elif keys[pygame.K_DOWN] or keys[pygame.K_s]:    # elif, not if
        car_speed -= BRAKE * dt
    else:
        if car_speed > 0:
            car_speed = max(0, car_speed - FRICTION * dt)
        elif car_speed < 0:
            car_speed = min(0, car_speed + FRICTION * dt)
    
    car_speed = max(-MAX_SPEED / 2, min(car_speed, MAX_SPEED))
    
    turn = TURN_SPEED * dt * (car_speed / MAX_SPEED)
    
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        angle += turn
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        angle -= turn
        
    rad = math.radians(angle)
    x += math.cos(rad) * car_speed * dt
    y -= math.sin(rad) * car_speed * dt
    
    if x > WIDTH: x = 0
    if x < 0: x = WIDTH
    if y > HEIGHT: y = 0
    if y < 0: y = HEIGHT
    
    screen.fill((30, 30, 30))
    
    rotated = pygame.transform.rotate(car_image, angle)
    rect = rotated.get_rect(center=(x, y))
    screen.blit(rotated, rect.topleft)
    
    
    fps_text = font.render(f"FPS: {clock.get_fps():.2f}", True, (255, 255, 255))
    postion_text = font.render(f"Speed: {car_speed:.0f}  Angle: {angle % 360:.0f}", True, (255, 255, 255))
    
    screen.blit(fps_text, (10, 10))
    screen.blit(postion_text, (10, 40))
    
    pygame.display.flip()  

    dt = clock.tick(60) / 1000.0  # Convert milliseconds to seconds  
    
    pygame.display.set_caption(f"RL Agent Simulation - FPS: {clock.get_fps():.2f}")

pygame.quit()