import pygame
from constants import *

def main():
    # Initialize the game
    pygame.init()

    # Print a startup message
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Initialize the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Create the game loop
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))  # Fill the screen with black
        pygame.display.flip()

if __name__ == "__main__":
    main()