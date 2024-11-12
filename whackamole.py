import pygame
import os
import random
dir_path = os.path.dirname(os.path.realpath(__file__))

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        mole_image = pygame.image.load(dir_path + "\mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        mole_x = 0
        mole_y = 0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if x > mole_x and x < mole_x + 32 and y > mole_y and y < mole_y + 32:
                        mole_x = random.randrange(0, 20) * 32
                        mole_y = random.randrange(0, 16) * 32
            screen.fill("light green")
            #drawing grid lines
            for i in range(1, 20):
                pygame.draw.line(screen, "black", (32 * i, 0), (32 * i, 512))
            for i in range(1, 16):
                pygame.draw.line(screen, "black", (0, 32 * i), (640, 32 * i))
            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_x, mole_y)))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
