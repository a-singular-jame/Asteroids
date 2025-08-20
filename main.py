import pygame
from asteroid import Asteroid
from constants import *
from player import *
from asteroidfield import *

def main():
    # ------- Initialization ------- #

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # ------------------------------ #
    
    # ----------- Groups ----------- #

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    # ------------------------------- #

    # ---------- Variables ---------- #

    dt = 0
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    asteroid_field = AsteroidField()

    # ------------------------------- #

    # -------- Start-up text -------- #

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # ------------------------------- #

    # ----- Running code begins ----- #

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        for asteroid in asteroids:
            for bullet in shots:
                if bullet.collision(asteroid):
                    asteroid.split()
                    bullet.kill()
            if asteroid.collision(player):
                print("Game over!")
                return
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000
    
    # ------------------------------- #

if __name__ == "__main__":
    main()



