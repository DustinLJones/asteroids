import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

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
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    # Initialize the clock
    clock = pygame.time.Clock()
    dt = 0

    # Create the game loop
    running = True

    # Instantiate asteroids
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    # Instantiate the player
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    Shot.containers = (shots, updatable, drawable)
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Fill the screen with black
        screen.fill((0, 0, 0))  

        # Update all game objects
        updatable.update(dt)

        # Check for collisions with player
        for asteroid in asteroids:
            if player.check_collision(asteroid):
                print("Game over!")
                running = False
                break                

        # Check for collisions between shots and asteroids
        for asteroid in asteroids:
            for shot in shots:
                if shot.check_collision(asteroid):
                    shot.kill()
                    asteroid.split()


        # Draw all game objects
        for obj in drawable:
            obj.draw(screen)

        # Redraw the screen
        pygame.display.flip()   

        # Limit the frame rate to 60 FPS
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()