import pygame
import sys

# Initializing the Game
pygame.init()

# Adding background music
pygame.mixer.init()
pygame.mixer.music.load('music1.wav')
pygame.mixer.music.set_volume(0.30)
pygame.mixer.music.play(-1)

# Setting game window
screen_width = 1400
screen_height = 800
gameWindow = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Seating Ideal")
playerIcon = pygame.image.load("playerMain.png")
pygame.display.set_icon(playerIcon)

# Adding Required Images for level 1
ground = pygame.image.load("level 1 bg.png")
ground = pygame.transform.scale(ground, (screen_width, screen_height)).convert_alpha()
level = pygame.image.load("levelbg.png")
level = pygame.transform.scale(level, (screen_width, screen_height)).convert_alpha()
player = pygame.image.load("student.png")
player = pygame.transform.scale(player, (80, 80)).convert_alpha()
homewindow = pygame.image.load("VID_47390127_074649_115_exported_1260_1610952907849 (1).jpg")
homewindow = pygame.transform.scale(homewindow, (screen_width, screen_height)).convert_alpha()
optionswindow = pygame.image.load("PMI_im.png")
optionswindow = pygame.transform.scale(optionswindow, (screen_width, screen_height)).convert_alpha()
result1 = pygame.image.load("level1_answer.png")
result1 = pygame.transform.scale(result1, (screen_width, screen_height)).convert_alpha()

# Setting Font specifications
textsize = 60
font = pygame.font.SysFont(None, textsize)
font2 = pygame.font.SysFont(None, 50)
font3 = pygame.font.SysFont(None, 110)
clock = pygame.time.Clock()


# Function for Showing Text
def screen_text(text, fontx, x, y, color):
    text_screen = fontx.render(text, True, color)
    gameWindow.blit(text_screen, [x, y])

# Main Window loop
def welcome():
    exit_game = False
    while not exit_game:

        gameWindow.fill([0, 255, 255])
        gameWindow.blit(homewindow, (0, 0))

        x, y = pygame.mouse.get_pos()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if 275 < x < 525 and 285 < y < 335:
                    levels()
                if 575 < x < 825 and 285 < y < 345:
                    options()
                if 900 < x < 1100 and 285 < y < 335:
                    exit_game = True
        # pygame.draw.rect(gameWindow, [255, 0, 0], [900, 285, 200, 50])
        pygame.display.update()

    sys.exit()

# Levels loop
def levels():
    exit_game = False

    while not exit_game:
        x, y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if 300 < x < 900 and 150 < y < 250:
                    gameloop1()
                if 300 < x < 900 and 300 < y < 500:
                    gameloop2()
                if 300 < x < 900 and 550 < y < 750:
                    gameloop3()
                if 0 < x < 100 and 0 < y < 100:
                    welcome()

            gameWindow.fill([255, 255, 204])
            gameWindow.blit(level, (0, 0))
            pygame.display.update()

    sys.exit()

# Images for Instructions
inst1 = pygame.image.load("instruction-1.png")
inst1 = pygame.transform.scale(inst1, (screen_width, screen_height)).convert_alpha()
inst2 = pygame.image.load("instruction-2 main.png")
inst2 = pygame.transform.scale(inst2, (screen_width, screen_height)).convert_alpha()
inst3 = pygame.image.load("instruction-3.png")
inst3 = pygame.transform.scale(inst3, (screen_width, screen_height)).convert_alpha()


def options():
    exit_game = False

    while not exit_game:
        x, y = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True

            if event.type == pygame.MOUSEBUTTONDOWN:

                if 500 < x < 1000 and 220 < y < 350:
                    instructions()
                elif 500 < x < 800 and 510 < y < 640:
                    about()
                elif 0 < x < 180 and 0 < y < 100:
                    welcome()

        gameWindow.fill([255, 202, 255])
        gameWindow.blit(optionswindow, (0, 0))
        clock.tick(60)
        pygame.display.update()

    sys.exit()


def instructions():
    exit_game = False
    while not exit_game:
        x, y = pygame.mouse.get_pos()
        gameWindow.blit(inst1, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 1050 < x < 1280 and 30 < y < 110:
                    inst_2()

        pygame.display.update()

    sys.exit()


def inst_2():
    exit_game = False
    while not exit_game:
        x, y = pygame.mouse.get_pos()
        gameWindow.blit(inst2, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 1050 < x < 1280 and 30 < y < 110:
                    inst_3()

        pygame.display.update()

    sys.exit()


def inst_3():
    exit_game = False
    while not exit_game:
        x, y = pygame.mouse.get_pos()
        gameWindow.blit(inst3, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 1050 < x < 1280 and 30 < y < 110:
                    options()

        pygame.display.update()

    sys.exit()


aboutbg = pygame.image.load("About1.png")
aboutbg = pygame.transform.scale(aboutbg, (screen_width, screen_height)).convert_alpha()


def about():
    exit_game = False
    while not exit_game:
        x, y = pygame.mouse.get_pos()
        gameWindow.blit(aboutbg, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 0 < x < 180 and 0 < y < 100:
                    options()

        pygame.display.update()

    sys.exit()

# Major Game loops
def gameloop1():
    exit_game = False
    user_text = ''
    answer1 = '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24'
    answer2 = '24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1'
    answer3 = '1 7 13 19 2 8 14 20 3 9 15 21 4 10 16 22 5 11 17 23 6 12 18 24'
    answer4 = '1 2 3 4 24 23 22 21 5 6 7 8 20 19 18 17 9 10 11 12 16 14 15 13'
    cheat = 'a'
    flag = False
    while not exit_game:
        mx, my = pygame.mouse.get_pos()

        gameWindow.fill([255, 0, 255])
        gameWindow.blit(ground, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True

            if event.type == pygame.KEYDOWN and flag == False:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                elif event.key == pygame.K_RETURN:
                    flag = True
                    break
                else:
                    user_text += event.unicode

            if event.type == pygame.MOUSEBUTTONDOWN:
                if 750 < mx < 1050 and 0 < my < 40:
                    welcome()

        if len(user_text) <= 30:
            user_text1 = user_text[:31]
            text_surface = font2.render(user_text1, True, [255, 0, 0])
            gameWindow.blit(text_surface, (700, 500))
        else:
            user_text2 = user_text[30:]
            text_surface2 = font2.render(user_text2, True, [255, 0, 0])
            gameWindow.blit(text_surface, (700, 500))
            gameWindow.blit(text_surface2, (700, 560))

        pygame.draw.rect(gameWindow, [255, 0, 0], [685, 475, 600, 200], 10)
        pygame.draw.rect(gameWindow, [255, 121, 255], [760, 0, 300, 40])
        back_text = font.render('Main Menu', True, [0, 0, 0])
        gameWindow.blit(back_text, (800, 0))
        if ((
                user_text == answer1 or user_text == answer2 or user_text == answer3 or user_text == answer4 or user_text == cheat) and flag == True):
            flag = True
            # pygame.time.wait(2000)
            gameWindow.blit(result1, (0, 0))
            x, y = pygame.mouse.get_pos()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if 750 < x < 950 and 500 < y < 650:
                    gameloop1()
                elif 1020 < x < 1290 and 500 < y < 650:
                    gameloop2()
        elif ((
                      user_text != answer1 or user_text != answer2 or user_text != answer3 or user_text != answer4 or user_text != cheat) and flag == True):
            game_over()

        clock.tick(30)
        pygame.display.update()

    sys.exit()


level2bg = pygame.image.load("level2 bg.png")
level2bg = pygame.transform.scale(level2bg, (screen_width, screen_height)).convert_alpha()
level2_answer1 = pygame.image.load('level2 answers 5 13 21 main.png')
level2_answer1 = pygame.transform.scale(level2_answer1, (screen_width, screen_height)).convert_alpha()
level2_answer2 = pygame.image.load('level2answer2.png')
level2_answer2 = pygame.transform.scale(level2_answer2, (screen_width, screen_height)).convert_alpha()
level2_answer3 = pygame.image.load('level2answer3.png')
level2_answer3 = pygame.transform.scale(level2_answer3, (screen_width, screen_height)).convert_alpha()
level2_answer4 = pygame.image.load('level2answer4.png')
level2_answer4 = pygame.transform.scale(level2_answer4, (screen_width, screen_height)).convert_alpha()


def gameloop2():
    exit_game = False
    user_text = ''
    answer1 = '1 2 3 4 5 21 7 8 9 10 11 12 13 14 15 16 17 18 19 20 6 22 23 24'
    answer2 = '1 2 3 4 5 11 7 8 9 10 6 12 13 14 15 16 17 18 19 20 21 22 23 24'
    answer3 = '1 2 3 4 5 15 7 8 9 10 11 12 13 14 6 16 17 18 19 20 21 22 23 24'
    answer4 = '1 2 3 4 5 24 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 6'
    cheat = 'm'
    flag = False
    while not exit_game:
        mx, my = pygame.mouse.get_pos()

        gameWindow.fill([255, 0, 255])
        gameWindow.blit(level2bg, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True

            if event.type == pygame.KEYDOWN and flag == False:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                elif event.key == pygame.K_RETURN:
                    flag = True
                    break
                else:
                    user_text += event.unicode

            if event.type == pygame.MOUSEBUTTONDOWN:
                if 750 < mx < 1050 and 0 < my < 40:
                    welcome()

        if len(user_text) <= 30:
            user_text1 = user_text[:31]
            text_surface = font2.render(user_text1, True, [255, 0, 0])
            gameWindow.blit(text_surface, (700, 500))
        else:
            user_text2 = user_text[30:]
            text_surface2 = font2.render(user_text2, True, [255, 0, 0])
            gameWindow.blit(text_surface, (700, 500))
            gameWindow.blit(text_surface2, (700, 560))

        pygame.draw.rect(gameWindow, [255, 0, 0], [685, 475, 600, 200], 10)
        pygame.draw.rect(gameWindow, [255, 121, 255], [760, 0, 300, 40])
        back_text = font.render('Main Menu', True, [0, 0, 0])
        gameWindow.blit(back_text, (800, 0))
        if (
                user_text == answer1 or user_text == answer2 or user_text == answer3 or user_text == answer4 or user_text == cheat) and flag == True:
            flag = True
            # pygame.time.wait(2000)
            if user_text == answer1 or user_text == cheat:
                gameWindow.blit(level2_answer1, (0, 0))
            elif user_text == answer2:
                gameWindow.blit(level2_answer2, (0, 0))
            elif user_text == answer3:
                gameWindow.blit(level2_answer3, (0, 0))
            elif user_text == answer4:
                gameWindow.blit(level2_answer4, (0, 0))
            x, y = pygame.mouse.get_pos()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if 750 < x < 950 and 500 < y < 650:
                    gameloop2()
                elif 1020 < x < 1290 and 500 < y < 650:
                    gameloop3()
        elif ((
                      user_text != answer1 or user_text != answer2 or user_text != answer3 or user_text != answer4) and flag == True):
            game_over()

        clock.tick(30)
        pygame.display.update()

    sys.exit()


level3bg = pygame.image.load('level3bg_m.png')
level3bg = pygame.transform.scale(level3bg, (screen_width, screen_height)).convert_alpha()
level3_answer1 = pygame.image.load('level3_ans1.png')
level3_answer1 = pygame.transform.scale(level3_answer1, (screen_width, screen_height)).convert_alpha()
level3_answer2 = pygame.image.load('level3_ans2.png')
level3_answer2 = pygame.transform.scale(level3_answer2, (screen_width, screen_height)).convert_alpha()


def gameloop3():
    exit_game = False
    user_text = ''
    answer1 = "z"
    answer2 = '1 7 10 19 2 8 14 20 3 9 15 21 4 13 12 22 5 11 17 23 6 16 18 24'
    answer3 = '1 2 3 4 5 20 7 8 9 10 11 12 13 14 15 16 17 18 19 6 21 22 23 24'
    flag = False
    while not exit_game:
        mx, my = pygame.mouse.get_pos()

        gameWindow.fill([255, 0, 255])
        gameWindow.blit(level3bg, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True

            if event.type == pygame.KEYDOWN and flag == False:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                elif event.key == pygame.K_RETURN:
                    flag = True
                    break
                else:
                    user_text += event.unicode

            if event.type == pygame.MOUSEBUTTONDOWN:
                if 750 < mx < 1050 and 0 < my < 40:
                    welcome()

        if len(user_text) <= 30:
            user_text1 = user_text[:31]
            text_surface = font2.render(user_text1, True, [255, 0, 0])
            gameWindow.blit(text_surface, (700, 500))
        else:
            user_text2 = user_text[30:]
            text_surface2 = font2.render(user_text2, True, [255, 0, 0])
            gameWindow.blit(text_surface, (700, 500))
            gameWindow.blit(text_surface2, (700, 560))

        pygame.draw.rect(gameWindow, [255, 0, 0], [685, 475, 600, 200], 10)
        pygame.draw.rect(gameWindow, [255, 121, 255], [760, 0, 300, 40])
        back_text = font.render('Main Menu', True, [0, 0, 0])
        gameWindow.blit(back_text, (800, 0))
        if (user_text == answer1 or user_text == answer2 or user_text == answer3) and flag == True:
            flag = True
            # pygame.time.wait(2000)
            if user_text == answer2 or user_text == answer1:
                gameWindow.blit(level3_answer1, (0, 0))

            elif user_text == answer3:
                gameWindow.blit(level3_answer2, (0, 0))
            x, y = pygame.mouse.get_pos()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if 730 < x < 930 and 450 < y < 550:
                    welcome()
                elif 1080 < x < 1280 and 450 < y < 550:
                    exit_game = True
                elif 830 < x < 1050 and 300 < y < 400:
                    gameloop1()
            # pygame.draw.rect(gameWindow, [0, 0, 0], [850, 300, 200, 100], 5)
        elif ((user_text != answer1 or user_text != answer2 or user_text != answer3) and flag == True):
            game_over()

        clock.tick(30)
        pygame.display.update()

    sys.exit()


gameover = pygame.image.load("gameover.jpg")
gameover = pygame.transform.scale(gameover, (screen_width, screen_height)).convert_alpha()


def game_over():
    exit_game = False
    # x, y = pygame.mouse.get_pos()
    gameWindow.blit(gameover, (0, 0))

    while not exit_game:
        x, y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True

            if event.type == pygame.MOUSEBUTTONDOWN:

                if 150 < x < 550 and 410 < y < 550:
                    levels()
                if 820 < x < 1220 and 410 < y < 550:
                    welcome()
                if 530 < x < 850 and 590 < y < 710:
                    exit_game = True
                    pygame.display.update()

        pygame.display.update()
    sys.exit()

# Calling the game
welcome()
