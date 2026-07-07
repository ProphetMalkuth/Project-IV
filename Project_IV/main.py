import pygame
import pytmx
pygame.init()
from camera import Camera

SCREEN_W = 1280
SCREEN_H = 720
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
screen_rect = screen.get_rect()

tmx_data = pytmx.load_pygame("assets/maps/map.tmx")

from map import draw_map
from player import Player
pygame.display.set_caption("Project IV")
clock = pygame.time.Clock()

#Constants
FPS = 60
WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)

map_width = tmx_data.width * tmx_data.tilewidth
map_height = tmx_data.height * tmx_data.tileheight

player = Player()
camera = Camera(map_width, map_height, SCREEN_W, SCREEN_H)

#Screen Display
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.move(map_width, map_height)
    player.player_hitbox()

    #Graphics Render
    screen.fill(WHITE)
    draw_map(screen, camera)
    camera.camera_update(player)
    player.draw(screen, camera)


    # Debug Hitbox
    debug_hitbox = player.hitbox.copy()
    debug_hitbox.x -= camera.x
    debug_hitbox.y -= camera.y
    pygame.draw.rect(screen, GREEN, debug_hitbox, 3)

    pygame.display.update()
    clock.tick(FPS)
pygame.quit()