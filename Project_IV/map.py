import pytmx

tmx_data = pytmx.load_pygame("assets/maps/map.tmx")

def draw_map(surface, camera):
    for layer in tmx_data.visible_layers:
        if hasattr(layer, "tiles"):
            for x, y, image in layer.tiles():

                world_x = x * tmx_data.tilewidth 
                world_y = y * tmx_data.tileheight #print the world

                screen_x = world_x - camera.x
                screen_y = world_y - camera.y #print the screen
                
                surface.blit(image,(screen_x, screen_y))