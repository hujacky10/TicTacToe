import pygame
import time
# Set up the drawing window
pygame.init()
width = 500
height = 500
screen = pygame.display.set_mode([width, height])
pygame.display.set_caption("Tic Tac Toe")
starting_window = pygame.image.load("modified_cover-100x100.png")
x = pygame.image.load("X_modified-100x100.png")
o = pygame.image.load("o_modified-100x100.png")
starting_window = pygame.transform.scale(starting_window, (width, height-100))
x = pygame.transform.scale(x, (80, 80))
o = pygame.transform.scale(o, (80, 80))
Board = [[None]*3, [None]*3, [None]*3]
symbol = "x"

# Welcome Screen
screen.fill((255, 255, 255))
screen.blit(starting_window, (0, 50))
pygame.display.flip()
time.sleep(1)

# Load the Game Board
screen.fill((255, 255, 255))
pygame.draw.line(screen, (0,0,0), (width / 3, 0), (width / 3, height), 7)
pygame.draw.line(screen, (0,0,0), (width / 3*2, 0), (width / 3*2, height), 7)
pygame.draw.line(screen, (0,0,0), (0, height/3), (width, height/3), 7)
pygame.draw.line(screen, (0,0,0), (0, height/3*2), (width, height/3*2), 7)
pygame.display.update()


def game():
    global symbol
    xaxis, yaxis = pygame.mouse.get_pos()
    if xaxis < 160 and yaxis < 160 and Board[0][0] == None:
        Board[0][0] = symbol
        if symbol == "x":
            screen.blit(x, (50, 50))
            symbol = "o"
        else:
            screen.blit(o, (50, 50))
            symbol = "x"
        pygame.display.update()
    elif 160 < xaxis < 320 and yaxis < 160 and Board[0][1] == None:
        Board[0][1] = symbol
        if symbol == "x":
            screen.blit(x, (210, 50))
            symbol = "o"
        else:
            screen.blit(o, (210, 50))
            symbol = "x"
    elif 320 < xaxis and yaxis < 160 and Board[0][2] == None:
        Board[0][2] = symbol
        if symbol == "x":
            screen.blit(x, (370, 50))
            symbol = "o"
        else:
            screen.blit(o, (370, 50))
            symbol = "x"
    elif xaxis < 160 and 160 < yaxis < 320 and Board[1][0] == None:
        Board[1][0] = symbol
        if symbol == "x":
            screen.blit(x, (50, 210))
            symbol = "o"
        else:
            screen.blit(o, (50, 210))
            symbol = "x"
    elif 160 < xaxis < 320 and 160 < yaxis < 320 and Board[1][1] == None:
        Board[1][1] = symbol
        if symbol == "x":
            screen.blit(x, (210, 210))
            symbol = "o"
        else:
            screen.blit(o, (210, 210))
            symbol = "x"
    elif 320 < xaxis and 160 < yaxis < 320 and Board[1][2] == None:
        Board[1][2] = symbol
        if symbol == "x":
            screen.blit(x, (370, 210))
            symbol = "o"
        else:
            screen.blit(o, (370, 210))
            symbol = "x"
    elif xaxis < 160 and 320 < yaxis and Board[2][0] == None:
        Board[2][0] = symbol
        if symbol == "x":
            screen.blit(x, (50, 370))
            symbol = "o"
        else:
            screen.blit(o, (50, 370))
            symbol = "x"
    elif 160 < xaxis < 320 and 320 < yaxis and Board[2][1] == None:
        Board[2][1] = symbol
        if symbol == "x":
            screen.blit(x, (210, 370))
            symbol = "o"
        else:
            screen.blit(o, (210, 370))
            symbol = "x"
    elif 320 < xaxis and 320 < yaxis and Board[2][2] == None:
        Board[2][2] = symbol
        if symbol == "x":
            screen.blit(x, (370, 370))
            symbol = "o"
        else:
            screen.blit(o, (370, 370))
            symbol = "x"
    pygame.display.update()

    count = 0
    for a in range(0,3):
        for b in range (0,3):
            if Board[a][b] != None:
                count = count + 1
            if Board[a][b] != None and count == 9:
                screen.fill((255, 255, 255))
                text = pygame.font.Font(None, 100).render("Draw", 1, (0, 0, 0))
                screen.blit(text, (50, 50))
                pygame.display.update()
    count = 0
    if Board[0][0] == Board[0][1] == Board[0][2] and Board[0][0] != None:
        screen.fill((255, 255, 255))
        text = pygame.font.Font(None, 100).render(Board[0][0] + " won", 1, (0,0,0))
        screen.blit(text, (50,50))
        pygame.display.update()
    elif Board[1][0] == Board[1][1] == Board[1][2] and Board[1][0] != None:
        screen.fill((255, 255, 255))
        text = pygame.font.Font(None, 100).render(Board[1][0] + " won", 1, (0,0,0))
        screen.blit(text, (50,50))
        pygame.display.update()
    elif Board[2][0] == Board[2][1] == Board[2][2] and Board[2][0] != None:
        screen.fill((255, 255, 255))
        text = pygame.font.Font(None, 100).render(Board[2][0] + " won", 1, (0,0,0))
        screen.blit(text, (50,50))
        pygame.display.update()
    elif Board[0][0] == Board[1][0] == Board[2][0] and Board[0][0] != None:
        screen.fill((255, 255, 255))
        text = pygame.font.Font(None, 100).render(Board[0][0] + " won", 1, (0,0,0))
        screen.blit(text, (50,50))
        pygame.display.update()
    elif Board[0][1] == Board[1][1] == Board[2][1] and Board[0][1] != None:
        screen.fill((255, 255, 255))
        text = pygame.font.Font(None, 100).render(Board[0][1] + " won", 1, (0,0,0))
        screen.blit(text, (50,50))
        pygame.display.update()
    elif Board[0][2] == Board[1][2] == Board[2][2] and Board[0][2] != None:
        screen.fill((255, 255, 255))
        text = pygame.font.Font(None, 100).render(Board[0][2] + " won", 1, (0,0,0))
        screen.blit(text, (50,50))
        pygame.display.update()
    elif Board[0][0] == Board[1][1] == Board[2][2] and Board[0][0] != None:
        screen.fill((255, 255, 255))
        text = pygame.font.Font(None, 100).render(Board[0][0] + " won", 1, (0,0,0))
        screen.blit(text, (50,50))
        pygame.display.update()
    elif Board[0][2] == Board[1][1] == Board[2][0] and Board[0][2] != None:
        screen.fill((255, 255, 255))
        text = pygame.font.Font(None, 100).render(Board[0][2] + " won", 1, (0,0,0))
        screen.blit(text, (50,50))
        pygame.display.update()


# Game Start
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
        elif event.type is pygame.MOUSEBUTTONDOWN:
            game()


