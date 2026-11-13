import pygame
import random
#this is for testing right now

BGCOLOR = BRIGHTBLUE = (0, 170, 255)

# main function that makes the program window for use.
# trying to figure out how to make a textbox and a menu window.

def main():
    pygame.init()
    pygame.display.set_caption("FlashQuiz.py")
    clock = pygame.time.Clock()
    dt = 0
    resolution = (800,600)
    screen = pygame.display.set_mode(resolution)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
            # Code reigsters typing input from Keyboard.
            if event.type == pygame.TEXTINPUT:
                print(event)
        background = BGCOLOR
        screen.fill(background)
        pygame.display.flip()
        dt = clock.tick
    pygame.quit()


if __name__ == "__main__":
    main()