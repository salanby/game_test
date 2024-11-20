import os
import pygame

def load_sprite(filename, size=None):
    """
    Load a sprite from the assets folder.
    
    Args:
        filename (str): The name of the sprite file.
        size (tuple): The desired size as (width, height), or None to keep original size.
    
    Returns:
        pygame.Surface: The loaded and optionally resized sprite.
    """
    base_path = r"C:\Users\Alyn\OneDrive\Desktop\Code\game_test\assets\sprites"
    sprite_path = os.path.join(base_path, filename)
    sprite = pygame.image.load(sprite_path).convert_alpha()
    
    if size:
        sprite = pygame.transform.scale(sprite, size)
    return sprite
