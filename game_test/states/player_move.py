# core/player_move.py
import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, sprite, x, y, move_speed, walls):
        super().__init__()
        self.image = sprite
        self.rect = self.image.get_rect()  # This is the sprite's rectangle for rendering
        self.rect.center = (x, y)

        # Create a separate hitbox rectangle for collision detection
        self.hitbox = self.rect.inflate(-20, -4)
        self.hitbox.top += 4  # Shift the hitbox top down by 4 pixels (adjust as needed)

        self.move_speed = move_speed  # Speed at which the player moves
        self.walls = walls  # List of walls to check for collisions

    def move(self, keys):
        # Movement logic with collision detection
        dx = 0
        dy = 0

        # Handle movement
        if keys[pygame.K_LEFT]:
            dx = -self.move_speed
        if keys[pygame.K_RIGHT]:
            dx = self.move_speed
        if keys[pygame.K_UP]:
            dy = -self.move_speed
        if keys[pygame.K_DOWN]:
            dy = self.move_speed

        # Try moving in the x direction (horizontal)
        self.rect.x += dx
        self.hitbox.x += dx  # Move the hitbox along with the sprite

        if self.collides_with_walls():
            self.rect.x -= dx  # Undo the horizontal movement if there was a collision
            self.hitbox.x -= dx  # Undo the hitbox movement too

        # Try moving in the y direction (vertical)
        self.rect.y += dy
        self.hitbox.y += dy  # Move the hitbox along with the sprite

        if self.collides_with_walls():
            self.rect.y -= dy  # Undo the vertical movement if there was a collision
            self.hitbox.y -= dy  # Undo the hitbox movement too

    def collides_with_walls(self):
        # Check for collision with any walls using the hitbox
        for wall in self.walls:
            if self.hitbox.colliderect(wall):  # Use the hitbox for collision detection
                return True
        return False

    def draw(self, screen):
        # Draw the player on the screen (sprite's image)
        screen.blit(self.image, self.rect.topleft)

