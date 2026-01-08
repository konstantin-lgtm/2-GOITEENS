import pygame
import random
import time
import sys

pygame.init()

YourBet = 0
playerColor = "nil"
GameStatus = "menu"
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("horse racing")
clock = pygame.time.Clock()
colors = [(255, 0, 0), (0, 255, 0), (255, 255, 0), (0, 0, 255)]
StartX, StartY, EndX, EndY = 100, 0, 100, 600

def showMenu():
    font = pygame.font.SysFont("Arial", 85)
    menuText = font.render("pres spase too start", True, (0, 0, 0))
    screen.blit(menuText, (50, 250))
    pygame.display.flip()

TextBetVisibol = False
def PlaceYourBet(YourBet, PlayerCash):
    if PlayerCash < YourBet:
        YourBet = PlayerCash
    key = pygame.key.get_pressed()
    font = pygame.font.SysFont("Arial", 85)
    PlaceBet = font.render("place you'r bet", True, (0, 0, 0))
    screen.blit(PlaceBet, (50, 250))

    BetFont = pygame.font.SysFont("Arial", 85)
    BetIsPlased = BetFont.render(f"{YourBet}", True, (0, 0, 0))
    screen.blit(BetIsPlased, (50, 350))
    pygame.display.flip()
    TextBetVisibol = True

#standart 50
cubeDistans = 50
#standart 150
CubeSize = 150
#standart 25, 300
CubeXPos, CubeYPos = 25, 300
def PaintTingChoseColor(cubeXPosition, cubeYPosition, playerColor, CubeSize, cubeDistans):
    cubeXP, cubeYP = cubeXPosition, cubeYPosition

    font = pygame.font.SysFont("Arial", 85)
    ChoseColor = font.render("chose your color", True, (0, 0, 0))
    screen.blit(ChoseColor, (50, 100))

    HorseColor = pygame.font.SysFont("Arial", 85)
    ChoseColor = HorseColor.render(f"your color is {playerColor}", True, (0, 0, 0))
    screen.blit(ChoseColor, (50, 200))
    for color in colors:
        pygame.draw.rect(screen, color, (cubeXP, cubeYP, CubeSize, CubeSize))
        cubeXP += (CubeSize+cubeDistans)

def CheckWhatColorIsClickedOn(ClickPosition, CubeXPosition, CubeYPosition, CubeSize, cubeDistans):
    XPosition = (CubeXPosition+CubeSize)
    YPosition = (CubeYPosition+CubeSize)
    MouseX, MouseY = ClickPosition #pygame.mouse.get_pos()
    if CubeXPosition <= MouseX and CubeYPosition <= MouseY and XPosition >= MouseX and YPosition >= MouseY:
        return "red"
    elif (CubeXPosition+(CubeSize+cubeDistans)) <= MouseX and CubeYPosition <= MouseY and (XPosition+(CubeSize+cubeDistans)) >= MouseX and YPosition >= MouseY:
        return "green"
    elif (CubeXPosition+((CubeSize+cubeDistans)*2)) <= MouseX and CubeYPosition <= MouseY and (XPosition+((CubeSize+cubeDistans)*2)) >= MouseX and YPosition >= MouseY:
        return "yellow"
    elif (CubeXPosition+((CubeSize+cubeDistans)*3)) <= MouseX and CubeYPosition <= MouseY and (XPosition+((CubeSize+cubeDistans)*3)) >= MouseX and YPosition >= MouseY:
        return "blue"
    return "nah"
    pygame.display.flip()

figur = ["rect1","circle", "polygon", "rect2"]
def TheReicing(color, figur, YPosition):
    if figur == "rect1":
        screen.fill((128, 128, 128))
        pygame.draw.rect(screen, color, (75, YPosition["squer"], 50, 50))
        YPosition["squer"] -= 1
    elif figur == "rect2":
        #screen.fill((128, 128, 128))
        pygame.draw.rect(screen, color, ((75+600), (YPosition["longSquer"]-12.5), 50, 75))
        if random.randint(0,2) == 2:
            YPosition["longSquer"] -= 1
            if random.randint(1, 75) == 1:
                YPosition["squer"] += 150
                if YPosition["squer"] > 600:
                    YPosition["squer"] = 600
                YPosition["tringl"]["point1"] += 150
                YPosition["tringl"]["point2"] += 150
                if YPosition["tringl"]["point1"] > 600:
                    YPosition["tringl"]["point1"] = 600
                    YPosition["tringl"]["point2"] = (600-50)
                YPosition["circle"] += 150
                if YPosition["circle"] > 600:
                    YPosition["circle"] = 600
    elif figur == "polygon":
        #screen.fill((128, 128, 128))
        pygame.draw.polygon(screen, color, ((475, YPosition["tringl"]["point1"]), (500, YPosition["tringl"]["point2"]), (525, YPosition["tringl"]["point1"])))
        if random.randint(0,2) == 2:
            YPosition["tringl"]["point1"] -= 1
            YPosition["tringl"]["point2"] -= 1
            if random.randint(1, 75) == 1:
                dash = random.randint(50, 150)
                YPosition["tringl"]["point1"] -= dash
                YPosition["tringl"]["point2"] -= dash
    elif figur == "circle":
        #screen.fill((128, 128, 128))
        pygame.draw.ellipse(screen, color, ((75 + 200), YPosition["circle"], 50, 50))
        if random.randint(0,3) == 3:
            YPosition["circle"] -= random.randint(1, 5)
    if YPosition["squer"] <= 100:
        font = pygame.font.SysFont("Arial", 65)
        ChoseColor = font.render("THE RED HORSE IS WIN!", True, (0, 0, 0))
        screen.blit(ChoseColor, (0, 0))
        return "red win"
    elif YPosition["longSquer"] <= 100:
        font = pygame.font.SysFont("Arial", 65)
        ChoseColor = font.render("THE BLUE HORSE IS WIN!", True, (0, 0, 0))
        screen.blit(ChoseColor, (0, 0))
        return "blue win"
    elif YPosition["tringl"]["point2"] <= 100:
        font = pygame.font.SysFont("Arial", 55)
        ChoseColor = font.render("THE YELLOW HORSE IS WIN!", True, (0, 0, 0))
        screen.blit(ChoseColor, (0, 0))
        return "yellow win"
    elif YPosition["circle"] <= 100:
        font = pygame.font.SysFont("Arial", 65)
        ChoseColor = font.render("THE GREEN HORSE IS WIN!", True, (0, 0, 0))
        screen.blit(ChoseColor, (0, 0))
        return "green win"

playerMony = 100

colorForLinia = [(255, 0, 0), (0, 255, 0), (255, 255, 0)]
is_stavka=False
EnterPresd = False
ChosenBet = False
PlayerColorChosen = False
runing = True
screen.fill((128, 128, 128))
horsesYPosition = {"squer":525, "longSquer":525, "tringl":{"point1":575,"point2":525}, "circle":525}
horsesStartYPosition = {"squer":525, "longSquer":525, "tringl":{"point1":575,"point2":525}, "circle":525}
while runing:
    StartX, StartY, EndX, EndY = 200, 0, 200, 600
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            runing = False
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if GameStatus == "menu":
                    GameStatus = "Bet"
                    EnterPresd = True
                elif GameStatus == "Bet":
                    playerMony -= YourBet
                    EnterPresd = "IsDontWhatWeeNeed"
                    ChosenBet = True
                    GameStatus = "Horse color"
                elif GameStatus == "Horse color":
                    if playerColor == "nil" or playerColor == "nah":
                        playerColor = "nah"
                    else:
                        ChosenBet = "IsDontWhatWeeNeed"
                        PlayerColorChosen = True
                        GameStatus = "Horse racing"
                elif GameStatus == "player win" or GameStatus == "player lose":
                    PlayerColorChosen = "IsDontWhatWeeNeed"
                    horsesYPosition["tringl"]["point1"] = horsesStartYPosition["tringl"]["point1"]
                    horsesYPosition["tringl"]["point2"] = horsesStartYPosition["tringl"]["point2"]
                    horsesYPosition["squer"] = horsesStartYPosition["squer"]
                    horsesYPosition["longSquer"] = horsesStartYPosition["longSquer"]
                    horsesYPosition["circle"] = horsesStartYPosition["circle"]
                    playerColor = "nil"
                    YourBet = 0
                    GameStatus = "Bet"
                    EnterPresd = True
                screen.fill((128, 128, 128))
            elif event.key == pygame.K_1 and EnterPresd:
                screen.fill((128, 128, 128))
                YourBet += 1
            elif event.key == pygame.K_2 and EnterPresd:
                screen.fill((128, 128, 128))
                YourBet += 2
            elif event.key == pygame.K_3 and EnterPresd:
                screen.fill((128, 128, 128))
                YourBet += 3
            elif event.key == pygame.K_4 and EnterPresd:
                screen.fill((128, 128, 128))
                YourBet += 4
            elif event.key == pygame.K_5 and EnterPresd:
                screen.fill((128, 128, 128))
                YourBet += 5
            elif event.key == pygame.K_6 and EnterPresd:
                screen.fill((128, 128, 128))
                YourBet += 6
            elif event.key == pygame.K_7 and EnterPresd:
                screen.fill((128, 128, 128))
                YourBet += 7
            elif event.key == pygame.K_8 and EnterPresd:
                screen.fill((128, 128, 128))
                YourBet += 8
            elif event.key == pygame.K_9 and EnterPresd:
                screen.fill((128, 128, 128))
                YourBet += 9
            elif event.key == pygame.K_BACKSPACE and EnterPresd:
                screen.fill((128, 128, 128))
                YourBet = 0
            if YourBet > playerMony:
                YourBet = playerMony
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if GameStatus == "Horse color":
                    playerColor = CheckWhatColorIsClickedOn(event.pos, CubeXPos, CubeYPos, CubeSize, cubeDistans)
                    screen.fill((128, 128, 128))
    if not EnterPresd:
        showMenu()
    if EnterPresd == True:
        PlaceYourBet(YourBet, playerMony)
    if ChosenBet == True:
        PaintTingChoseColor(CubeXPos, CubeYPos, playerColor, CubeSize, cubeDistans)
    if PlayerColorChosen == True:
        for i in range(4):
            Reising = TheReicing(colors[i], figur[i], horsesYPosition)
            if Reising:
                if Reising == "red win" and playerColor == "red":
                    playerMony += (YourBet*2)
                    PlayerColorChosen = False
                    GameStatus = "player win"
                elif Reising == "blue win" and playerColor == "blue":
                    playerMony += (YourBet*2)
                    PlayerColorChosen = False
                    GameStatus = "player win"
                elif Reising == "yellow win" and playerColor == "yellow":
                    playerMony += (YourBet*2)
                    PlayerColorChosen = False
                    GameStatus = "player win"
                elif Reising == "green win" and playerColor == "green":
                    playerMony += (YourBet*2)
                    PlayerColorChosen = False
                    GameStatus = "player win"
                else:
                    PlayerColorChosen = False
                    GameStatus = "player lose"
    pygame.draw.line(screen, (0, 0, 0), (0, 100), (800, 100), 5)
    pygame.draw.line(screen, (255, 255, 255), (0, 500), (800, 500), 5)
    font = pygame.font.SysFont("Arial", 20)
    textSurface = font.render(f"{playerMony}", True, (0, 0, 0))
    screen.blit(textSurface, (0, 50))
    for color in colorForLinia:
        pygame.draw.line(screen, color, (StartX, StartY), (EndX, EndY), 5)
        StartX += 200
        EndX += 200
    if playerMony <= 0 and GameStatus == "Bet":
        runing = False
        sys.exit()

    pygame.display.flip()
    clock.tick(45)
    pygame.time.delay(10)