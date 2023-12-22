import pygame
import menu_and_options

class Map:
    def __init__(self):
        self.__tileHeight = 0#total heihgt in tiles
        self.__tileWidth = 0#total width in tiles
        self.__tileMap = []#list of lists to contain a 2d map of tileID int numbers
        #e.g. [[0, 0, 0, 0, 0]
        #      [0, 0, 0, 0, 0]
        #      [0, 1, 0, 0, 1]
        #      [1, 1, 1, 1, 1]
        #      [1, 2, 2, 2, 2]] 

        self.__tileImg = []#stores a list of tile images to be drawn. 
        #from the example above, images of tileID 1 and 2 will be loaded inside. 
        #tileID 0 is empty tile

    def tileHeight(self):
        return self.__tileHeight

    def tileHeight(self, tileHeight):
        self.__tileHeight = tileHeight

    def tileWidth(self):
        return self.__tileWidth

    def tileWidth(self, tileWidth):
        self.__tileWidth = tileWidth

    def tileMap(self):
        return self.__tileMap

    def tileMap(self, tileMap):
        self.__tileMap = tileMap

    def tileImages(self):


class OptCharacterTest(menu_and_options.OptionFactory):
    def __init__(self, screen, clock):
        super().__init__()
        self.__screen = screen
        self.__clock = clock

    def action(self):
        pass
        #test character class and sprites and animation and controls and shit

