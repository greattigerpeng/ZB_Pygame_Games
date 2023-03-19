# --- Setup --- #
import pygame
import random
pygame.init()


def make_easy_button(window: pygame.Surface, buttonX, buttonY):
    button = pygame.Rect(buttonX, buttonY, 100, 100)
    pygame.draw.rect(window, (255, 75, 75), button)


def make_medium_button(window: pygame.Surface, buttonX, buttonY):
    button = pygame.Rect(buttonX, buttonY, 50, 50)
    pygame.draw.rect(window, (255, 75, 75), button)


def make_hard_button(window: pygame.Surface, buttonX, buttonY):
    button = pygame.Rect(buttonX, buttonY, 10, 10)
    pygame.draw.rect(window, (255, 75, 75), button)
