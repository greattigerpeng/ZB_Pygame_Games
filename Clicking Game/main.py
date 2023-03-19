import pygame
import functions
import random
import time
import sys
pygame.init()
window = pygame.display.set_mode((800, 800))
window.fill((0, 216, 43))
difficulty = input("Which difficulty level (easy, medium, hard): ")

if difficulty == "easy":
    print("Okay! Let's get started!")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)

    drawing = True
    clicked = False
    time = 1000

    while True:
        if drawing:
            buttonX = random.randint(0, 700)
            buttonY = random.randint(0, 700)
            window.fill((0, 216, 43))
            functions.make_easy_button(window, buttonX, buttonY)
            pygame.display.flip()
            drawing = not drawing
        pygame.time.wait(2)
        time -= 1
        if time <= 0:
            print("Took too long!")
            drawing = False
            sys.exit()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                drawing = False
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if buttonX < x < buttonX + 100 and buttonY < y < buttonY + 100:
                    print("Hit!")
                    clicked = True
                    time = 1000
                else:
                    print("Misclicked!")
                    drawing = False
                    sys.exit()
                pygame.display.flip()
                if time >= 0 and clicked:
                    drawing = True
                clicked = False

if difficulty == "medium":
    print("Okay! Let's get started!")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    drawing = True
    clicked = False
    time = 1000

    while True:
        if drawing:
            buttonX = random.randint(0, 750)
            buttonY = random.randint(0, 750)
            window.fill((0, 216, 43))
            functions.make_medium_button(window, buttonX, buttonY)
            pygame.display.flip()
            drawing = not drawing
        pygame.time.wait(4)
        time -= 3
        if time <= 0:
            print("Took too long!")
            drawing = False
            sys.exit()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                drawing = False
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if buttonX < x < buttonX + 50 and buttonY < y < buttonY + 50:
                    print("Hit!")
                    clicked = True
                    time = 1000
                else:
                    print("Misclicked!")
                    drawing = False
                    sys.exit()
                pygame.display.flip()
                if time >= 0 and clicked:
                    drawing = True
                clicked = False

if difficulty == "hard":
    print("Okay! Let's get started!")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    drawing = True
    clicked = False
    time = 1000

    while True:
        if drawing:
            buttonX = random.randint(0, 700)
            buttonY = random.randint(0, 700)
            window.fill((0, 216, 43))
            functions.make_hard_button(window, buttonX, buttonY)
            pygame.display.flip()
            drawing = not drawing
        pygame.time.wait(3)
        time -= 1
        if time <= 0:
            print("Took too long!")
            drawing = False
            sys.exit()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                drawing = False
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if buttonX < x < buttonX + 10 and buttonY < y < buttonY + 10:
                    print("Hit!")
                    clicked = True
                    time = 1000
                else:
                    print("Misclicked!")
                    drawing = False
                    sys.exit()
                pygame.display.flip()
                if time >= 0 and clicked:
                    drawing = True
                clicked = False
