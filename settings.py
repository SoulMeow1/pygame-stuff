import pygame
import menu_and_options
import json

with open("initSettings.json", "r") as json_file:
    initSettings = json.load(json_file)

class OptExit(menu_and_options.OptionFactory):
    def __init__(self):
        super().__init__()

    def action(self):
        pygame.quit()
        exit()

class OptScreenResolution(menu_and_options.OptionFactory):
    def __init__(self, width: int, height: int):
        super().__init__()
        self.__width = width
        self.__height = height

    def action(self):
        with open("initSettings.json", "r") as json_file:
            initSettings = json.load(json_file)

        initSettings["resolutionWidth"] = self.__width
        initSettings["resolutionHeight"] = self.__height

        with open("initSettings.json", "w") as json_file:
            json.dump(initSettings, json_file)

class OptSettings(menu_and_options.OptionFactory):
    def __init__(self, screen, clock):
        super().__init__()
        self.__screen = screen
        self.__clock = clock

    def action(self):
        surface = pygame.Surface((initSettings["resolutionWidth"],initSettings["resolutionHeight"]))
        surface.fill('Black')

        menu = menu_and_options.Menu()

        #screen resolution as left right menu setup
        dropOpt = menu_and_options.OptLeftRightSelect(self.__screen, self.__clock)
        dropOpt.font('font/arial.ttf')
        dropOpt.text('screen resolution    ')
        dropOpt.aa(False)   
        dropOpt.colour('White')

        option0 = OptScreenResolution(640,480)
        option0.text('640 x 480')
        option0.aa(False)   
        option0.colour('White')
        dropOpt.appendOpt(option0)

        option0 = OptScreenResolution(720, 400)
        option0.text('720 x 400')
        option0.aa(False)   
        option0.colour('White')
        dropOpt.appendOpt(option0)

        option0 = OptScreenResolution(720, 480)
        option0.text('720 x 480')
        option0.aa(False)   
        option0.colour('White')
        dropOpt.appendOpt(option0)

        option0 = OptScreenResolution(720, 576)
        option0.text('720 x 576')
        option0.aa(False)   
        option0.colour('White')
        dropOpt.appendOpt(option0)

        option0 = OptScreenResolution(800,600)
        option0.text('800 x 600')
        option0.aa(False)   
        option0.colour('White')
        dropOpt.appendOpt(option0)

        option0 = OptScreenResolution(1024, 768)
        option0.text('1024 x 768')
        option0.aa(False)   
        option0.colour('White')
        dropOpt.appendOpt(option0)

        option0 = OptScreenResolution(1128, 634)
        option0.text('1128 x 634')
        option0.aa(False)   
        option0.colour('White')
        dropOpt.appendOpt(option0)

        option0 = OptScreenResolution(1280, 720)
        option0.text('1280 x 720')
        option0.aa(False)   
        option0.colour('White')
        dropOpt.appendOpt(option0)

        option0 = OptScreenResolution(1280, 1024)
        option0.text('1280 x 1024')
        option0.aa(False)   
        option0.colour('White')
        dropOpt.appendOpt(option0)

        option0 = OptScreenResolution(1366, 768)
        option0.text('1366 x 768')
        option0.aa(False)   
        option0.colour('White')
        dropOpt.appendOpt(option0)

        option0 = OptScreenResolution(1440, 900)
        option0.text('1440 x 900')
        option0.aa(False)   
        option0.colour('White')
        dropOpt.appendOpt(option0)

        option0 = OptScreenResolution(1600,900)
        option0.text('1600 x 900')
        option0.aa(False)   
        option0.colour('White')
        dropOpt.appendOpt(option0)

        option0 = OptScreenResolution(1680, 1050)
        option0.text('1680 x 1050')
        option0.aa(False)   
        option0.colour('White')
        dropOpt.appendOpt(option0)

        option0 = OptScreenResolution(1760, 990)
        option0.text('1760 x 990')
        option0.aa(False)   
        option0.colour('White')
        dropOpt.appendOpt(option0)

        option0 = OptScreenResolution(1920, 1080)
        option0.text('1920 x 1080')
        option0.aa(False)   
        option0.colour('White')
        dropOpt.appendOpt(option0)

        menu.appendOpt(dropOpt)

        menu.lineUpOptions(10, 10)

        menu.executeMenu(self.__screen, self.__clock)

