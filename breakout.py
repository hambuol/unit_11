# import's nedded moduels and classes
import pygame,sys
from pygame.locals import *
import brick
import paddle
import ball


def main():
    pygame.init()
    # Constants that will be used in the program
    APPLICATION_WIDTH = 400
    APPLICATION_HEIGHT = 600
    BRICKS_PER_ROW = 10
    BRICK_SEP = 4 #The space between each brick
    BRICK_Y_OFFSET = 70
    BRICK_WIDTH =  (APPLICATION_WIDTH - (BRICKS_PER_ROW + 1) * BRICK_SEP) / BRICKS_PER_ROW
    NUM_TURNS = 3
    num_rows = 1

    # Sets up the colors
    RED = (255, 0, 0)
    ORANGE = (255, 165, 0)
    YELLOW = (255, 255, 0)
    GREEN =(0, 255, 0)
    CYAN = (0, 255, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    colors = [RED, ORANGE, YELLOW, GREEN, CYAN,]
    # sets the main screen for the game
    mainsurface = pygame.display.set_mode((APPLICATION_WIDTH, APPLICATION_HEIGHT), 0, 32)
    # sets the caption of the game
    pygame.display.set_caption("Breakout")
    # creates sprite group for the bricks
    bricksGroup = pygame.sprite.Group()
    # creates sprite goup for the paddle
    padGroup = pygame.sprite.Group()
    # sets the x-position  and y-position to start drawing bricks
    xpos = BRICK_SEP
    ypos = BRICK_Y_OFFSET
    # function is a series of loops creates the bricks in the proper formation and color

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

    brik(xpos, ypos)
    # defines mypaddle
    mypaddle = paddle.Paddle(BLACK)
    # adds paddle to paddle sprite group
    padGroup.add(mypaddle)
    # defines myball
    myball = ball.Ball(mainsurface, BLACK)
    # sets position where ball will be pu on screen
    myball.rect.topleft = (125, 400)
    # defines end_it for start screen while loop
    end_it = False
    level = 1
    # this loops adds a start screen and begins game when clicked
    # code retreved from
    # http://stackoverflow.com/questions/20356307/how-would-i-add-a-start-screen-to-this-pygame-python-code

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

        # sets the framerate of the game
        clock = pygame.time.Clock()
        clock.tick(50)
        # makes the mainsurface white
        mainsurface.fill(WHITE)
        # makess ppos equal to the mouse position
        ppos = pygame.mouse.get_pos()

        # creates level counter and puts it on the screen
        scorefont = pygame.font.SysFont("Britannic Bold", 40)
        scorelable = scorefont.render("Level: {0}".format(level), 1, BLACK)
        mainsurface.blit(scorelable, (10, 10))

        # creates lives counter and puts it on the screen
        liveslable = scorefont.render("Lives: {0}" .format(NUM_TURNS), 1, BLACK)
        mainsurface.blit(liveslable, (290, 10))

        # removes brick from brick group/screen if ball hits brick
        if myball.collide(bricksGroup):
            bricksGroup.remove()

        # does nesesary action for next level
        if len(bricksGroup) == 0:
            myball.rect.topleft = (125, 400)
            myball.speedx = 6
            myball.speedy = 4
            num_rows += 1
            level += 1
            NUM_TURNS += 3
            brik(xpos, ypos)

        for apad in padGroup:
            myball.collide2(padGroup)
            padGroup.update(apad)

        # makes paddle follow x cordinate of the mouse position
        mypaddle.rect.topleft = (ppos[0], 550)

        # makes is so the paddle stays o the screen
        if ppos[0] >= 340:
            mypaddle.rect.topleft = (340, 550)
        # updates paddle
        padGroup.update()
        # updates ball
        myball.update()
        # blits brick on to mainsurface
        for mybrick in bricksGroup:
            mainsurface.blit(mybrick.image, mybrick.rect)
        # takes away a turn if the ball hits the bottom of the screen, and resets the ball position and speed
        if myball.rect.bottom > mainsurface.get_height():
            NUM_TURNS -= 1
            myball.rect.topleft = (125, 400)
            myball.speedx = 6
            myball.speedy = 4
        # quits the game if you ran out of lives
        if NUM_TURNS == 0:
            pygame.quit()
            sys.exit()
        # blits paddle on mainscreen
        mainsurface.blit(mypaddle.image, mypaddle.rect)
        # blits ball on mainscreen
        mainsurface.blit(myball.image, myball.rect)
        # updates display
        pygame.display.update()
main()
