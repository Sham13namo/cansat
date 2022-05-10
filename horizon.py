
import pygame
import random
import math
pygame.init()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
def rot_center(image, rect, angle):
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = rot_image.get_rect(center=rect.center)
        return rot_image,rot_rect
angle = 0

image = pygame.image.load("2.png")
rect = image.get_rect(center=(400, 300)) 

def rotate(angle):
    surf, r = rot_center(image, rect, angle)
    SCREEN.blit(surf, r)
    pygame.display.flip()
