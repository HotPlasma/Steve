'''
Program: Steve the Game
Programmer: Egor Kharlamov
Date completed: 24/12/2013
'''

#-------------------------------------------------------------
# Set constant image variables
#-------------------------------------------------------------
File_Name = "Assets\SaveGame.txt"
char="Images\Steve3.png"
charR="Images\Steve3R.png"
bg = "Images\BG.png"
ground = "Images\Ground.png"
MainMenuBG = "Images\MMBG.png"
SUN = "Images\Sun.png"
MMSteve = "Images\SteveMM.png"
Door = "Images\Door.png"
Inst1 = "Images\Instructions1.png"
Inst2 = "Images\Instructions2.png"
Inst3 = "Images\Instructions3.png"
Inst4 = "Images\Instructions4.png"
enemy = "Images\Enemy.png"
Heart = "Images\Heart.png"
Coin = "Images\Coin.png"
Co_Coin = "Images\C_Coin.png"
BGN = "Images\BGNight.png"
fly = "Images\Firefly.png"
Volcano = "Images\BGLava.png"
LM = "Images\LavaMonster.png"
Final = "Images\End Screen.png"
#House keeping
import pygame,sys
from pygame.locals import *
import time
#-------------------------------------------------------------
# Classes
#-------------------------------------------------------------

PLAYERACCEL = 0.2
PLAYERDEACCEL = 1
MAXSPEED = 4
accelX = 0
MAXHEALTH = 3
HP = 3
CoinList = [(650,350), (400,160), (100,100), (0,0)]
CoinList2 = [(650,150),(220,110),(0,0)]
CoinList3 = [(700,500), (680,500), (620,300), (300,450),(250,500), (0,0)]
CoinList4 = [(100,150),(220,110),(0,0)]
CoinList5 = [(650,150),(220,110),(0,0)]
CoinList6 = [(550,400),(500,240),(0,0)]
CoinList7 = [(100,150),(220,110),(0,0)]
CoinList8 = [(650,150),(220,110),(0,0)]
CoinList9 = [(300,500),(150,600),(0,0)]
CoinRectList = []
CoinRectList2 = []
CoinRectList3 = []
CoinRectList4 = []
CoinRectList5 = []
CoinRectList6 = []
CoinRectList7 = []
CoinRectList8 = []
CoinRectList9 = []
GameStarting = True
GamePaused = False

class screen:
    Width = 800
    Height = 550

class Floor:
   bx = 0
   by = 520

class Speed:
    X = 0
    Y = 0

class Level:
    WhichLevel = 1
    WhichScreen = 1
    Coins = 0
    Health = 100
    Pause = "PAUSED"

class Blob:
    X = 700
    X2 = 100
    Y = 460
    MoveX = 1
    MoveY = 1

class Fly:
    X = 400
    Y = 100
    MoveX = 1
    MoveY = 1

class LBlob:
    X = 500
    Y = 500
    X2 = 800
    Y2 = 205
    X3 = 500
    Y3 = 500
    MoveX = 1
    MoveY = 1

jumping = False

LEFT = K_LEFT
RIGHT = K_RIGHT
JUMP = K_UP
#-------------------------------------------------------------
# Initiate pygame and time / general housekeeping
#-------------------------------------------------------------
pygame.init()
pygame.mouse.set_visible(0)
#Clock and screen creation
MainClock = pygame.time.Clock()
#Window = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
Window = pygame.display.set_mode((screen.Width, screen.Height), 0, 32)
#-------------------------------------------------------------
# Declares window name and colours
#-------------------------------------------------------------"
pygame.display.set_caption("Steve")

Black = (0,0,0)
Red = (255,0,0)
Green = (84,160,46)
White = (255,255,255)
#-------------------------------------------------------------
# Data structures
#-------------------------------------------------------------
#Coverting pictures to usable sprites
BackgroundCloud = pygame.image.load(bg).convert()
Back = pygame.image.load(ground).convert()
SteveImg = pygame.image.load(char).convert_alpha()
MMBG = pygame.image.load(MainMenuBG).convert()
Sun = pygame.image.load(SUN).convert_alpha()
MainMenuSteve = pygame.image.load(MMSteve).convert_alpha()
TDoor = pygame.image.load(Door).convert_alpha()
I1 = pygame.image.load(Inst1).convert()
I2 = pygame.image.load(Inst2).convert()
I3 = pygame.image.load(Inst3).convert()
I4 = pygame.image.load(Inst4).convert()
Enemy1 = pygame.image.load(enemy).convert_alpha()
Health = pygame.image.load(Heart).convert_alpha()
Coin = pygame.image.load(Coin).convert_alpha()
Coins = pygame.image.load(Co_Coin).convert_alpha()
BGNight = pygame.image.load(BGN).convert_alpha()
FireFly = pygame.image.load(fly).convert_alpha()
BG3 = pygame.image.load(Volcano).convert_alpha()
LavaBlob = pygame.image.load(LM).convert_alpha()
EndScreen = pygame.image.load(Final).convert()

#Movement variables

class Player:
    X = 0 # The location of the player on the X axis
    Y = 500 # The location of the player on the Y axis
Jumpmod = 1 # Allows me to control the jump speed more efficiently.

def SteveControls():
    global jumping
    global accelX
    global Jumpmod
    global MaxJumpHeight
    global SteveImg
    #global GamePaused
    for event in pygame.event.get():
        if event.type == QUIT:
            Save()
            pygame.quit()
            sys.exit() #Allows program to be quit safely within Python
        if event.type == KEYDOWN:
            if event.key==K_LEFT:
                SteveImg = pygame.image.load(charR).convert_alpha() # mirrors image of Steve if facing left direction
                if jumping:
                    Player.X+=Speed.X
            elif event.key==K_RIGHT:
                SteveImg = pygame.image.load(char).convert_alpha()
                if jumping:
                    Player.X+=Speed.X
            elif event.key == K_SPACE and not jumping:
                MaxJumpHeight = Player.Y - 200
                jumping = True
                if Jumpmod == 1:
                    MaxJumpHeight = Player.Y - 200
                    Jumpmod = 2
            elif event.key == K_ESCAPE:
                #Pauses Game
                while 1:
                    event = pygame.event.wait()
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        break
        if event.type == KEYUP:
            if event.key==K_LEFT:
                Speed.X=0
            elif event.key==K_RIGHT:
                Speed.X =0
            elif event.key == K_SPACE and not jumping:
                jumping = False

def DrawMainMenu():
        pygame.mouse.set_visible(1) # Makes mouse visable
        BasicFont = pygame.font.Font(None, 80)
        Options = ("New Game", "Continue", "Instructions", "Exit")
        MenuText(Options, BasicFont, Black, 400, 100, 100)
        MainClock.tick(300)
        pygame.display.update()
        while True:
            Window.blit(MMBG, (0,0))
            Window.blit(Sun, (-35, -25))
            Window.blit(MainMenuSteve, (550,350))
            MenuText(Options, BasicFont, Black, 400, 100, 100)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key==K_1:
                        DrawGame()
                        return
                    if event.key == K_2:
                        #DrawGame()
                        print (Level.WhichScreen,Level.WhichLevel)
                        DrawGame()
                        Load()
                        ScreenCounter()
                        return
                        print (Level.WhichScreen,Level.WhichLevel)
                        #return
                    if event.key==K_3:
                        DrawInstructions()
                    if event.key == K_4:
                        pygame.quit()

def DrawGame():
    #Draw everything that has been built
    if Level.WhichLevel == 1:
        Window.blit(BackgroundCloud, (0,0))
        Window.blit(Back,(Floor.bx,Floor.by))
    elif Level.WhichLevel == 2:
        Window.blit(BGNight, (0,0))
    elif Level.WhichLevel == 3:
        Window.blit(BG3, (0,0))
    Window.blit(SteveImg,(Player.X,Player.Y))
    Enemies()
    CoinsHUD()
    CoinsLoad()
    CoinDraw()
    Platforms()
    LoadHealthMeter()
    #Limit updates to once every 300 miliseconds for stability
    MainClock.tick(300)
    pygame.display.update()
               
def Enemies():
    # Get global coordinates of Steve's location
    global SteveHitBox
    # Get coordinates of each enemy type
    BlobRect = Enemy1.get_rect(center =(Blob.X2, Blob.Y))
    SteveHitBox = SteveImg.get_rect(center =(Player.X - 15,Player.Y - 15))
    FlyRect = FireFly.get_rect(center = (Fly.X,Fly.Y))
    LBlobRect = LavaBlob.get_rect(center = (LBlob.X, LBlob.Y))
    #First Blob enemy sighting on Level 1, Screen 2.
    if Level.WhichLevel == 1:
        if Level.WhichScreen == 2:
            #Blob runs away to the right.
            Blob.X += Blob.MoveX
            if Blob.X == 600:
                Blob.X -= Blob.MoveX
            Window.blit(Enemy1, (Blob.X,Blob.Y))
            #Second Blob seen on Level 1, Level 3.
        elif Level.WhichScreen == 3:
            Window.blit(Enemy1, (Blob.X2,460))
            if BlobRect.colliderect(SteveHitBox):
                HealthChange(1) # damage taken if contact is made.
                pygame.display.update()
                #Runs left and right and blocks player from getting coins
            if Blob.X2< 100:
                Blob.MoveX = 1
            if Blob.X2 > 400:
                Blob.MoveX = -1
            Blob .X2 += Blob.MoveX
            #Firefly enemy on the 3rd screen of the second level.
    if Level.WhichLevel == 2:
        if Level.WhichScreen == 3:
            Window.blit(FireFly, (Fly.X,Fly.Y))
            Fly.Y += Fly.MoveY
            if FlyRect.colliderect(SteveHitBox):
                HealthChange(1)
                pygame.display.update()
                #Flys up and down and makes it difficult to reach the door.
            if Fly.Y < 100:
                Fly.MoveY = 1
            if Fly.Y > 500:
                Fly.MoveY = -1
    # 2 Lava Blob enemies on Level 3, Screen 1.
    if Level.WhichLevel == 3:
        if Level.WhichScreen == 1:
            Window.blit(LavaBlob, (LBlob.X,LBlob.Y))
            if LBlobRect.colliderect(SteveHitBox):
                HealthChange(1)
                pygame.display.update()
                #Both run left and right but one runs on platform.
            if LBlob.X< 100:
                LBlob.MoveX = 1
            if LBlob.X > 500:
                LBlob.MoveX = -1
            LBlob.X += LBlob.MoveX
            Window.blit(LavaBlob, (LBlob.X2,LBlob.Y2))
            LBlob.X2 += LBlob.MoveX
        if Level.WhichScreen == 2:
            #Another Lava Blob enenmy
            Window.blit(LavaBlob, (LBlob.X,LBlob.Y))
            if LBlobRect.colliderect(SteveHitBox):
                HealthChange(1)
                pygame.display.update()
            if LBlob.X< 100:
                LBlob.MoveX = 1
            if LBlob.X > 500:
                LBlob.MoveX = -1
            LBlob.X += LBlob.MoveX
        if Level.WhichScreen == 3:
            #A mash of enemies from previous and current levels on the final screen.
            Window.blit(FireFly, (Fly.X,Fly.Y))
            Fly.Y += Fly.MoveY
            if FlyRect.colliderect(SteveHitBox):
                HealthChange(1)
                pygame.display.update()
            if Fly.Y < 100:
                Fly.MoveY = 1
            if Fly.Y > 500:
                Fly.MoveY = -1
            Window.blit(Enemy1, (Blob.X2,480))
            if BlobRect.colliderect(SteveHitBox):
                HealthChange(1)
                pygame.display.update()
            if Blob.X2< 100:
                Blob.MoveX = 1
            if Blob.X2 > 400:
                Blob.MoveX = -1
            Blob.X2 += Blob.MoveX
            
            

def CoinsHUD():
    #Draws the heads up display which shows number of coins collected.
    Window.blit(Coin, (160,1)) # Location of coin image.
    font = pygame.font.Font(None, 36) # Font picker
    text = font.render(str(Level.Coins), 1, (10, 10, 10))
    #Text is equal to number of coins collected
    textpos = (215, 15) # Location of text.
    Window.blit(text, textpos) # Draws text to screen.

def CoinsLoad():
    #Reads Coins lists and converts them into CoinRectLists.
    if Level.WhichLevel == 1:
        if Level.WhichScreen == 1:
            for i in range(len(CoinList)):
                c = CoinList[i]
                abc = Coins.get_rect()
                abc.x = c[0]
                abc.y = c[1]
                CoinRectList.append(abc)

        if Level.WhichScreen == 2:
            for i in range(len(CoinList2)):
                c = CoinList2[i]
                abc = Coins.get_rect()
                abc.x = c[0]
                abc.y = c[1]
                CoinRectList2.append(abc)
            
        if Level.WhichScreen == 3:
            for i in range(len(CoinList3)):
                c = CoinList3[i]
                abc = Coins.get_rect()
                abc.x = c[0]
                abc.y = c[1]
                CoinRectList3.append(abc)

    if Level.WhichLevel == 2:
        if Level.WhichScreen == 1:
            for i in range(len(CoinList4)):
                c = CoinList4[i]
                abc = Coins.get_rect()
                abc.x = c[0]
                abc.y = c[1]
                CoinRectList4.append(abc)

        if Level.WhichScreen == 2:
            for i in range(len(CoinList5)):
                c = CoinList5[i]
                abc = Coins.get_rect()
                abc.x = c[0]
                abc.y = c[1]
                CoinRectList5.append(abc)

        if Level.WhichScreen == 3:
            for i in range(len(CoinList6)):
                c = CoinList6[i]
                abc = Coins.get_rect()
                abc.x = c[0]
                abc.y = c[1]
                CoinRectList6.append(abc)

    if Level.WhichLevel == 3:
        if Level.WhichScreen == 1:
            for i in range(len(CoinList7)):
                c = CoinList7[i]
                abc = Coins.get_rect()
                abc.x = c[0]
                abc.y = c[1]
                CoinRectList7.append(abc)

        if Level.WhichScreen == 2:
            for i in range(len(CoinList8)):
                c = CoinList8[i]
                abc = Coins.get_rect()
                abc.x = c[0]
                abc.y = c[1]
                CoinRectList8.append(abc)

        if Level.WhichScreen == 3:
            for i in range(len(CoinList9)):
                c = CoinList9[i]
                abc = Coins.get_rect()
                abc.x = c[0]
                abc.y = c[1]
                CoinRectList9.append(abc)
            

def CoinDraw():
    #Uses coin locations to put coins in the correct locations.
    if Level.WhichLevel == 1:
        if Level.WhichScreen == 1:
            for i in range(len(CoinList)-1):
                Window.blit(Coins,(CoinRectList[i].x, CoinRectList[i].y))
                if SteveHitBox.colliderect(CoinRectList[i]): # if Steve collides with a coin
                    del CoinList[i] # delete the coin
                    del CoinRectList[i] # delete the coins rectangular position.
                    Level.Coins += 1

        if Level.WhichScreen == 2:
            for i in range(len(CoinList2)-1):
                Window.blit(Coins,(CoinRectList2[i].x, CoinRectList2[i].y))
                if SteveHitBox.colliderect(CoinRectList2[i]):
                    del CoinList2[i]
                    del CoinRectList2[i]
                    Level.Coins += 1

        if Level.WhichScreen == 3:
            for i in range(len(CoinList3)-1):
                Window.blit(Coins,(CoinRectList3[i].x, CoinRectList3[i].y))
                if SteveHitBox.colliderect(CoinRectList3[i]):
                    del CoinList3[i]
                    del CoinRectList3[i]
                    Level.Coins += 1

    if Level.WhichLevel == 2:
        if Level.WhichScreen == 1:
                for i in range(len(CoinList4)-1):
                    Window.blit(Coins,(CoinRectList4[i].x, CoinRectList4[i].y))
                    if SteveHitBox.colliderect(CoinRectList4[i]):
                        del CoinList4[i]
                        del CoinRectList4[i]
                        Level.Coins += 1

        if Level.WhichScreen == 2:
            #if Level.CoinsLoaded == True
            for i in range(len(CoinList5)-1):
                Window.blit(Coins,(CoinRectList5[i].x, CoinRectList5[i].y))
                if SteveHitBox.colliderect(CoinRectList5[i]):
                    del CoinList5[i]
                    del CoinRectList5[i]
                    Level.Coins += 1

        if Level.WhichScreen == 3:
            for i in range(len(CoinList6)-1):
                Window.blit(Coins,(CoinRectList6[i].x, CoinRectList6[i].y))
                if SteveHitBox.colliderect(CoinRectList6[i]):
                    del CoinList6[i]
                    del CoinRectList6[i]
                    Level.Coins += 1

    if Level.WhichLevel == 3:
        if Level.WhichScreen == 1:
                for i in range(len(CoinList7)-1):
                    Window.blit(Coins,(CoinRectList7[i].x, CoinRectList7[i].y))
                    if SteveHitBox.colliderect(CoinRectList7[i]):
                        del CoinList7[i]
                        del CoinRectList7[i]
                        Level.Coins += 1

        if Level.WhichScreen == 2:
            for i in range(len(CoinList8)-1):
                Window.blit(Coins,(CoinRectList8[i].x, CoinRectList8[i].y))
                if SteveHitBox.colliderect(CoinRectList5[i]):
                    del CoinList8[i]
                    del CoinRectList8[i]
                    Level.Coins += 1

        if Level.WhichScreen == 3:
            for i in range(len(CoinList9)-1):
                Window.blit(Coins,(CoinRectList9[i].x, CoinRectList9[i].y))
                if SteveHitBox.colliderect(CoinRectList9[i]):
                    del CoinList9[i]
                    del CoinRectList9[i]
                    Level.Coins += 1
            

def LoadHealthMeter():
    #Makes the health bar functions.
    global HP
    # if 0 life no hearts
    if HP > 0:
        Window.blit(Health,(0,0))
    if HP > 1:
        Window.blit(Health, (50,0))
    if HP > 2:
        Window.blit(Health, (100,0))
    if HP < 1:
    #Number of hearts depends of HP.
        HP = 3
        #returns player to the first screen of the level.
        Level.WhichScreen = 1
    
def HealthChange(Change):
    #if health changes return player to save location
    global HP
    Player.X = 0
    Player.Y = 500
    #Change health.
    HP -= Change

def ScreenCounter():
    #Counts which screen Steve is on.
    if Level.WhichScreen < 1:
        Level.WhichScreen = 1
    if Level.WhichScreen > 3:
        Level.WhichScreen = 3
    #Stops screen number from going below 1 or over 3.

def Platforms():
    #Creates platforms with collision detection
    global jumping
    global MaxJumpHeight
    global SteveLoc
    SteveLoc = SteveImg.get_rect(center =(Player.X + 25,Player.Y + 25))
    if Level.WhichLevel == 1:
            if Level.WhichScreen == 1:
                #List of first screen platforms
                B1 = pygame.draw.rect(Window, Green, (620,400,180,20), 0)
                B2 = pygame.draw.rect(Window,Green, (350, 230, 200, 20), 0)
                B3 = pygame.draw.rect(Window,Green, (100, 200, 200, 40), 0)
                B4 = pygame.draw.rect(Window,Green,(200, 150, 170, 60), 0)

                if SteveLoc.colliderect(B1):
                    #Collision detection and jumping intergration.
                    SteveLoc.bottom = B1.top
                    Speed.Y = 0
                    jumping = False
                    MaxJumpHeight = Player.Y - 200
                
                elif SteveLoc.colliderect(B2):
                    SteveLoc.bottom = B2.top
                    Speed.Y = 0
                    jumping = False
                    MaxJumpHeight = Player.Y - 200

                elif SteveLoc.colliderect(B3):
                    SteveLoc.bottom = B3.top
                    Speed.Y = 0
                    jumping = False
                    MaxJumpHeight = Player.Y - 200
    
                elif SteveLoc.colliderect(B4):
                    SteveLoc.bottom = B4.top
                    Speed.Y = 0
                    jumping = False
                    MaxJumpHeight = Player.Y - 200
                else:
                    Speed.Y = 2

            elif Level.WhichScreen == 2:
                B5 = pygame.draw.rect(Window, Green, (130,400,400,400), 0)
                B6 = pygame.draw.rect(Window, Green, (200, 150,170, 60), 0)
                B7 = pygame.draw.rect(Window, Green, (550, 200, 180, 60),0)

                if SteveLoc.colliderect(B5):
                    SteveLoc.bottom = B5.top
                    Speed.Y = 0
                    jumping = False
                    MaxJumpHeight = Player.Y - 200

                elif SteveLoc.colliderect(B6):
                    SteveLoc.bottom = B5.top
                    Speed.Y = 0
                    jumping = False
                    MaxJumpHeight = Player.Y - 200

                elif SteveLoc.colliderect(B7):
                    SteveLoc.bottom = B7.top
                    Speed.Y = 0
                    jumping = False
                    MaxJumpHeight = Player.Y - 200
                else:
                    Speed.Y = 2

            elif Level.WhichScreen == 3:
                B8 = pygame.draw.rect(Window, Green, (500, 400, 80, 60),0)
                B9 = pygame.draw.rect(Window, Green, (559, 400, 40, 30), 0)
                Window.blit(TDoor, (530,270))
                DoorRect = TDoor.get_rect(center = (530,270))

                if SteveLoc.colliderect(B8):
                    SteveLoc.bottom = B8.top
                    Speed.Y = 0
                    jumping = False
                    MaxJumpHeight = Player.Y - 200

                else:
                    Speed.Y = 2

                if SteveLoc.colliderect(DoorRect):
                    Level.WhichLevel = 2
                    Level.WhichScreen = 1
                    Player.X = 0
                    Player.Y = 500

                

    if Level.WhichLevel == 2:
        if Level.WhichScreen == 1:
            B10 = pygame.draw.rect(Window, Green, (50, 420, 40, 30), 0)
            B11 = pygame.draw.rect(Window, Green, (120, 300, 150, 50), 0)
            B12 = pygame.draw.rect(Window, Green, (300, 260, 500, 50), 0)

            if SteveLoc.colliderect(B10):
                    SteveLoc.bottom = B10.top
                    Speed.Y = 0
                    jumping = False
                    MaxJumpHeight = Player.Y - 200

            elif SteveLoc.colliderect(B11):
                    SteveLoc.bottom = B11.top
                    Speed.Y = 0
                    jumping = False
                    MaxJumpHeight = Player.Y - 200

            elif SteveLoc.colliderect(B11):
                    SteveLoc.bottom = B11.top
                    Speed.Y = 0
                    jumping = False
                    MaxJumpHeight = Player.Y - 200

            elif SteveLoc.colliderect(B12):
                    SteveLoc.bottom = B12.top
                    Speed.Y = 0
                    jumping = False
                    MaxJumpHeight = Player.Y - 200
            else:
                    Speed.Y = 2

        if Level.WhichScreen == 2:
            B13 = pygame.draw.rect(Window, Green, (250,350, 300, 75), 0)

            if SteveLoc.colliderect(B13):
                    SteveLoc.bottom = B13.top
                    Speed.Y = 0
                    jumping = False
                    MaxJumpHeight = Player.Y - 200
            else:
                    Speed.Y = 2

        if Level.WhichScreen == 3:
            Window.blit(TDoor, (650,410))
            DoorRect2 = TDoor.get_rect(center = (650,410))

            if SteveLoc.colliderect(DoorRect2):
                Level.WhichLevel = 3
                Level.WhichScreen = 1
                Player.X = 0
                Player. Y = 500
                
    if Level.WhichLevel == 3:
        if Level.WhichScreen ==1:
            B13 = pygame.draw.rect(Window, Green, (200, 300, 40, 30), 0)
            B14 = pygame.draw.rect(Window, Green, (320, 400, 150, 50), 0)
            B15 = pygame.draw.rect(Window, Green, (300, 260, 500, 50), 0)

            if SteveLoc.colliderect(B13):
                    SteveLoc.bottom = B13.top
                    Speed.Y = 0
                    jumping = False
                    MaxJumpHeight = Player.Y - 200

            elif SteveLoc.colliderect(B14):
                    SteveLoc.bottom = B14.top
                    Speed.Y = 0
                    jumping = False
                    MaxJumpHeight = Player.Y - 200

            elif SteveLoc.colliderect(B15):
                    SteveLoc.bottom = B15.top
                    Speed.Y = 0
                    jumping = False
                    MaxJumpHeight = Player.Y - 200

            else:
                Speed.Y = 2

        elif Level.WhichScreen == 2:
            B16= pygame.draw.rect(Window, Green, (200, 300, 400, 30), 0)
            B17= pygame.draw.rect(Window, Green, (150, 150, 200, 50), 0)
            
            if SteveLoc.colliderect(B16):
                SteveLoc.bottom = B16.top
                Speed.Y = 0
                jumping = False
                MaxJumpHeight = Player.Y - 200

            elif SteveLoc.colliderect(B17):
                    SteveLoc.bottom = B17.top
                    Speed.Y = 0
                    jumping = False
                    MaxJumpHeight = Player.Y - 200

            else:
                    Speed.Y = 2

        elif Level.WhichScreen == 3:
            #Creates door
            Window.blit(TDoor, (650,410))
            DoorRect = TDoor.get_rect(center = (600,410))
            if SteveLoc.colliderect(DoorRect):
                #Creates end screen
                Window.blit(EndScreen,(0,0))
                CoinsHUD()
                pygame.display.update()
                time.sleep(5)

def MenuText(Text, Font, Colour, x , y, spacing):
    #Writes out multiple line text onto the screen when given the appropriate parameters
        for line in Text:
        #Defines the text to be rendered
            Render = Font.render(line, True, Colour)

            #Defines the position the text will go
            Position = Render.get_rect()
            Position.centery = (Text.index(line) * spacing) + y
            Position.centerx = x
        
            #Draws text to the screen
            Window.blit(Render, Position)

def Save():
    #Saves data to SaveGame File.
    SaveFiles = [Level.WhichLevel, Level.WhichScreen]
    ItemsStore = ""
    File = open("Assets\SaveGame.txt", "w")
    for items in SaveFiles:
        ItemsStore = str(items) + "\n"
        File.write(ItemsStore)
    File.close

def Load():
    #Loads data from Load SaveGame File.
    File = open("Assets\SaveGame.txt", "r")
    LoadLevel = (File.readline())
    Level.WhichLevel = LoadLevel
    LoadScreen = (File.readline())
    Level.WhichScreen = LoadScreen
    File.close
        
def DrawInstructions():
    InstructionScreen = 1
    while True:
        #Show instructions
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key==LEFT:
                    InstructionScreen -= 1
                elif event.key==RIGHT:
                    InstructionScreen += 1
                elif event.key == K_ESCAPE:
                    return
        #Draw instructions
                #Changes screen depending on what variable is.
            if InstructionScreen == 1:
                 Window.blit(I1,(0,0))
            elif InstructionScreen == 2:
                Window.blit(I2,(0,0))
            elif InstructionScreen == 3:
                Window.blit(I3, (0,0))
            elif InstructionScreen == 4:
                Window.blit(I4, (0,0))
                
        #Stops variable from becoming to high.
        if InstructionScreen >4:
            InstructionScreen = 4
        elif InstructionScreen <1:
            InstructionScreen = 1
        MainClock.tick(300)
        pygame.display.update()
    
def SteveMovement():
    global jumping
    global accelX
    global Jumpmod
    global PLAYERACCEL
    global Xkeys
    #Lets the player move left or right.
    Xkeys = pygame.key.get_pressed()
    if not jumping:
        accelX = (Xkeys[RIGHT] - Xkeys[LEFT]) * PLAYERACCEL
    elif jumping:
        accelX = (Xkeys[RIGHT] - Xkeys[LEFT]) * PLAYERACCEL


    # Accelerate the player towards the maximum speed
    if accelX != 0:
        if Speed.X <= MAXSPEED and Speed.X >= -MAXSPEED:
            Speed.X += accelX
            if Speed.X > MAXSPEED:
                Speed.X = MAXSPEED
            if Speed.X < -MAXSPEED:
                Speed.X = -MAXSPEED
    
    # Deaccelerate the player when no keys are pressed
    if accelX == 0:
        if Speed.X > 0:
            Speed.X -= PLAYERDEACCEL
            if Speed.X < 0:
                Speed.X = 0
        if Speed.X < 0:
            Speed.X += PLAYERDEACCEL
            if Speed.X > 0:
                Speed.X = 0
#-------------------------------------------------------------
# THE GAME LOOP
#-------------------------------------------------------------
DrawMainMenu()
#Draws menu before game starts.
while True:
    SteveControls()
    SteveMovement()
    #Jumping mechanics 
    if jumping == True:
        Speed.Y = 2
        if Player.Y >= MaxJumpHeight:
            while Player.Y >= MaxJumpHeight and Player.Y +30 <= Floor.by:
                Player.Y -= Speed.Y + 1 #Allows movement accross the y axis
                SteveControls()
                SteveMovement()
                Player.X+=Speed.X #Allows movement accross the x axis
                #Use correct background
                if Level.WhichLevel == 1:
                    Window.blit(BackgroundCloud, (0,0))
                    Window.blit(Back,(Floor.bx,Floor.by))
                elif Level.WhichLevel == 2:
                    Window.blit(BGNight, (0,0))
                elif Level.WhichLevel == 3:
                    Window.blit(BG3, (0,0))
                #Run all subroutines.
                Window.blit(SteveImg,(Player.X,Player.Y))
                Platforms()
                Enemies()
                CoinsHUD()
                CoinsLoad()
                CoinDraw()
                LoadHealthMeter()
                #Update game.
                MainClock.tick(300)
                pygame.display.update()
                if Player.Y <= MaxJumpHeight:
                    jumping = False
        if Player.Y + 30 >= Floor.by :
            jumping = False
    elif Player.Y +30 <= Floor.by and jumping == False:
        Player.Y += Speed.Y

    #Makes floor stop falling.
    if Player.Y + 30 > Floor.by:
        Player.Y = Floor.by - 33

    #Screen change system 
    if screen.Width < Player.X + 100:
        if Level.WhichScreen == 3:
            Player.X = 700
        else:
            Player.X = 0
            Player.Y = 500
            Level.WhichScreen += 1
            ScreenCounter()
        
    if 0 > Player.X :
        Player.X = 700
        Player.Y = 500
        if Level.WhichScreen == 1:
            Player.X=0
        Level.WhichScreen -= 1
        ScreenCounter()

    #Stops player from going above screen.    
    if Player.Y < 0:
        Player.Y = 0
        playerSpeedY = 0

    Player.X+=Speed.X #Allows movement accross the x axis
    Player.Y+=Speed.Y #Allows movement accross the y axis

    Platforms()
    DrawGame()
