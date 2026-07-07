class Camera:
    def __init__(self, map_w, map_h, screen_w, screen_h):
        self.x = 0
        self.y = 0
        self.map_w = map_w
        self.map_h = map_h
        self.screen_w = screen_w
        self.screen_h = screen_h


    def camera_update(self, player):

        self.x = player.world_x - self.screen_w // 2
        self.y = player.world_y - self.screen_h // 2
    
        if self.x <= 0:
            self.x = 0
        elif self.x >= self.map_w - self.screen_w:
            self.x = self.map_w - self.screen_w
        else:
            self.x = player.world_x - self.screen_w // 2

        
        if self.y <= 0:
            self.y = 0
        elif self.y >= self.map_h - self.screen_h:
            self.y = self.map_h - self.screen_h
        else:
            self.y = player.world_y - self.screen_h // 2
            


        