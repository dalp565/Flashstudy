import pygame
import random
#this is for testing right now

BGCOLOR = BRIGHTBLUE = (0, 170, 255)
WINWIDTH = 600
WINHEIGHT = 800
HALFWINWIDTH = int(WINWIDTH/2)
HALFWINHEIGHT = int(WINHEIGHT/2)

# main function that makes the program window for use.
# trying to figure out how to make a textbox and a menu window.

def main():
    pygame.init()
    pygame.display.set_caption("FlashQuiz.py")
    clock = pygame.time.Clock()
    dt = 0
    resolution = (WINHEIGHT,WINWIDTH)
    screen = pygame.display.set_mode(resolution)
    running = True
    #inputrect
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
            # Code reigsters typing input from Keyboard. Prints out key used, reanchored into events.
            if event.type == pygame.TEXTINPUT:
                print(event)
        background = BGCOLOR
        screen.fill(background)
        pygame.key.set_text_input_rect(pygame.rect(0,0,0,0))
        pygame.display.flip()
        dt = clock.tick
    pygame.quit()


if __name__ == "__main__":
    main()