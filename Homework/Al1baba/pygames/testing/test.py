import pygame

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game!")

WHITE = (255, 255, 255)

FPS = 60
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

POG_IMAGE = pygame.image.load("Pogchamp.png")
POG_IMAGE = pygame.transform.scale(POG_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
TRY_HARD_IMAGE = pygame.image.load("download.png")
TRY_HARD_IMAGE = pygame.transform.rotate(pygame.transform.scale(TRY_HARD_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 180)


def draw_window():
    WIN.fill(WHITE)
    WIN.blit(POG_IMAGE, (300, 100))
    WIN.blit(TRY_HARD_IMAGE, (700, 100))
    pygame.display.update()


def main():

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()

    pygame.quit()


if __name__ == '__main__':
    main()
