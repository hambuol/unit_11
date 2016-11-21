import pygame,sys
from pygame.locals import *
import brick
import paddle
import ball


def main():
    pygame.init()
    #Constants that will be used in the program
    APPLICATION_WIDTH = 400
    APPLICATION_HEIGHT = 600
    PADDLE_Y_OFFSET = 30
    BRICKS_PER_ROW = 10
    BRICK_SEP = 4 #The space between each brick
    BRICK_Y_OFFSET = 70
    BRICK_WIDTH =  (APPLICATION_WIDTH - (BRICKS_PER_ROW + 1) * BRICK_SEP) / BRICKS_PER_ROW
    NUM_TURNS = 3
    num_rows = 1

    #Sets up the colors
    RED = (255, 0, 0)
    ORANGE = (255, 165, 0)
    YELLOW = (255, 255, 0)
    GREEN =(0, 255, 0)
    CYAN = (0, 255, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    colors = [RED, ORANGE, YELLOW, GREEN, CYAN,]
    mainsurface = pygame.display.set_mode((APPLICATION_WIDTH, APPLICATION_HEIGHT), 0, 32)
    pygame.display.set_caption("Breakout")
    mainsurface.fill(WHITE)
    bricksGroup = pygame.sprite.Group()
    padGroup = pygame.sprite.Group()
    xpos = BRICK_SEP
    ypos = BRICK_Y_OFFSET
    def brik(xpos, ypos):
        for color in colors:
                for q in range(num_rows):
                    for x in range(BRICKS_PER_ROW):
                        mybrick = brick.Brick(BRICK_WIDTH, color)
                        mybrick.rect.topleft = (xpos, ypos)
                        bricksGroup.add(mybrick)
                        mainsurface.blit(mybrick.image,mybrick.rect)
                        xpos += BRICK_WIDTH + BRICK_SEP
                    ypos += BRICK_SEP * 3
                    xpos = BRICK_SEP
    brik(xpos,ypos)
    mypaddle = paddle.Paddle(BLACK)
    padGroup.add(mypaddle)
    myball = ball.Ball(mainsurface, BLACK)
    myball.rect.topleft = (125 ,400)
    end_it = False
    score = 0
    # this loops adds a start screen and begins game when clicked
    # code retreved from http://stackoverflow.com/questions/20356307/how-would-i-add-a-start-screen-to-this-pygame-python-code
    while (end_it == False):
        mainsurface.fill(BLACK)
        myfont = pygame.font.SysFont("Britannic Bold", 40)
        nlabel = myfont.render("Click to start", 1, (255, 0, 0))
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                end_it = True
        mainsurface.blit(nlabel, (100, 200))
        pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # framerate
        clock = pygame.time.Clock()
        clock.tick(50)
        mainsurface.fill(WHITE)
        ppos = pygame.mouse.get_pos()

        # scoreboard
        scorefont = pygame.font.SysFont("Britannic Bold", 40)
        scorelable = scorefont.render("Score {0}".format(score), 1, RED)
        mainsurface.blit(scorelable, (10, 10))
        score = 0

        # removes brick from brick group/screen if ball hits brick
        if myball.collide(bricksGroup):
            bricksGroup.remove()

        # adds a row to bricks for "next level"
        if len(bricksGroup) == 0:
            myball.rect.topleft = (125, 400)
            num_rows += 1
            brik(xpos,ypos)

        for apad in padGroup:
            myball.collide2(padGroup)
            padGroup.update(apad)

        mypaddle.rect.topleft = (ppos[0], 550)

        # makes is so the paddle stays o the screen(a little buggy)
        if ppos[0] >= 340:
            mypaddle.rect.topleft = (340, 550)

        padGroup.update()
        myball.update()
        for mybrick in bricksGroup:
            mainsurface.blit(mybrick.image, mybrick.rect)

        if myball.rect.bottom > mainsurface.get_height():
            NUM_TURNS -= 1
            myball.rect.topleft = (125, 400)

        if NUM_TURNS == 0:
            pygame.quit()
            sys.exit()

        mainsurface.blit(mypaddle.image, mypaddle.rect)
        mainsurface.blit(myball.image, myball.rect)
        pygame.display.update()
main()
