import pygame
import time
import random

pygame.init()
display_width = 800
display_height = 600
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('A Bit Racey')
clock = pygame.time.Clock()
carImg = pygame.image.load('mcqueen.png')

def scoreboard(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Score: " + str(count), True, black)
    gameDisplay.blit(text, (0, 0))
    
def message_display(text):
    sText = pygame.font.Font('freesansbold.ttf', 115)
    textSurf, textRect = text_objects(text, sText)
    textRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(textSurf, textRect)
    pygame.display.update()
    time.sleep(2)
    game_loop()

def text_objects(text, font):
    textSurf = font.render(text, True, red)
    return textSurf, textSurf.get_rect()

def obstacles(x, y, width, height, color):
    pygame.draw.rect(gameDisplay, color, [x, y, width, height])

def car(x, y):
    gameDisplay.blit(carImg, (x, y))

def crash():
    message_display('You crashed')

def game_loop():
    x = display_width * 0.45
    y = display_height * 0.8
    x_change = 0
    obstacle_x = random.randrange(0, display_width)
    obstacle_y = -600
    obstacle_w = 100
    obstacle_h = 100
    obstacle_speed = 7
    dodged = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
        x += x_change
        gameDisplay.fill(white)
        obstacles(obstacle_x, obstacle_y, obstacle_w, obstacle_h, blue)
        obstacle_y += obstacle_speed
        car(x, y)
        scoreboard(dodged)
        if x > display_width or x < 0:
            crash()
        if obstacle_y > display_height:
            obstacle_y = 0 - obstacle_h
            obstacle_x = random.randrange(0, display_width)
            dodged += 1
            obstacle_speed += 1
        if y < obstacle_y + obstacle_h:
            if x > obstacle_x and x < obstacle_x + obstacle_w:
                crash()
        pygame.display.update()
        clock.tick(60)

game_loop()
