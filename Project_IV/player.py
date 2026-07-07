import pygame

class Player:
    def __init__(self):

        self.world_x = 600 #World Coordinate
        self.world_y = 338
    
        self.image = pygame.image.load("assets/player/Player(dummy).png")
        self.image = pygame.transform.scale(self.image, (80,80))

        self.rect = self.image.get_rect() #Screen Coordinate
        self.speed = 7
        self.hitbox = pygame.Rect(0, 0, 65, 80)

    
    def player_hitbox(self):
        self.hitbox.center = (self.world_x + self.rect.width // 2, self.world_y + self.rect.height // 2)
        

    def move(self, map_width, map_height):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_w] and self.world_y >=0:
            self.world_y -= self.speed
        if keys[pygame.K_a] and self.world_x >= 0:
            self.world_x -= self.speed
        if keys[pygame.K_s] and self.world_y + self.rect.right <= map_height:
            self.world_y += self.speed
        if keys[pygame.K_d] and self.world_x + self.rect.bottom <= map_width:
            self.world_x += self.speed


    def draw(self, surface, camera):
        surface.blit(self.image, (self.world_x - camera.x, self.world_y - camera.y)) #Draw at world coordinate
