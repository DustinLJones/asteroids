import pygame
from constants import *
from player import Player

def main():
    # Initialize the game
    pygame.init()

    # Print a startup message
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Initialize the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Initialize groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    # Initialize the clock
    clock = pygame.time.Clock()
    dt = 0

    # Create the game loop
    running = True

    # Instantiate the player
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Fill the screen with black
        screen.fill((0, 0, 0))  

        # Update all game objects
        updatable.update(dt)

        # Draw all game objects
        for obj in drawable:
            obj.draw(screen)

        # Redraw the screen
        pygame.display.flip()   

        # Limit the frame rate to 60 FPS
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()