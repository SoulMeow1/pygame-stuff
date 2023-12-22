import pygame
import menu_and_options
import json
import settings

with open("initSettings.json", "r") as json_file:
    initSettings = json.load(json_file)

pygame.init()
screen = pygame.display.set_mode((initSettings["resolutionWidth"] ,initSettings["resolutionHeight"]))#screen res to be set using variables soon

surface = pygame.Surface((initSettings["resolutionWidth"] ,initSettings["resolutionHeight"]))#to be discarded soon???
surface.fill('Black')

pygame.display.set_caption('I want to be the strongest hololive member')
clock = pygame.time.Clock()

menu = menu_and_options.Menu()

option0 = settings.OptSettings(screen, clock)
option0.text('settings')
option0.aa(True)
option0.colour('White')
menu.appendOpt(option0)

menu.lineUpOptions(400, 300)

menu.executeMenu(screen, clock)