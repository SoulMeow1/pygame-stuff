import pygame
import json

with open("initSettings.json", "r") as json_file:
    initSettings = json.load(json_file)

class OptionFactory:
    def __init__(self, font = 'font/arial.ttf', fontSize = initSettings["globalFontSize"], text = 'Insert Text Here' , aa = False, colour = 'White', x = 10, y = 10):
        self.__font = font
        self.__fontSize = fontSize
        self.__text = text
        self.__aa = aa
        self.__colour = colour

        self.__pygameFont = pygame.font.Font(self.__font, self.__fontSize)
        self.__pygameRender = self.__pygameFont.render(self.__text, self.__aa, self.__colour)

        self.__x = x
        self.__y = y
        self.__rect = self.__pygameRender.get_rect(center = (self.__x, self.__y))

    # Main responsibility---------------------------------------------------------------------------------
    def action(self):
            pass

    def drawObj(self, screen):
        screen.blit(self.__pygameRender, self.__rect)

    def alignLeft(self, x):
        self.__rect = self.__pygameRender.get_rect(midleft = (x, self.__y))
        self.__x = self.__rect.centerx

    def alignTop(self, y):
        self.__rect = self.__pygameRender.get_rect(midtop = (self.__x, y))
        self.__y = self.__rect.centery

    #getters and setters----------------------------------------------------------------------------------
    def font(self):
        return self.__font

    def font(self, font: str):
        self.__font = font
        self.__pygameFont = pygame.font.Font(self.__font, self.__fontSize)
        self.__pygameRender = self.__pygameFont.render(self.__text, self.__aa, self.__colour)
        self.__rect = self.__pygameRender.get_rect(center = (self.__x, self.__y))

    def fontSize(self):
        return self.__fontSize

    def fontSize(self, fontSize: int):
        self.__fontSize = fontSize
        self.__pygameFont = pygame.font.Font(self.__font, self.__fontSize)
        self.__pygameRender = self.__pygameFont.render(self.__text, self.__aa, self.__colour)
        self.__rect = self.__pygameRender.get_rect(center = (self.__x, self.__y))

    def text(self):
        return self.__text

    def text(self, text: str):
        self.__text = text
        self.__pygameRender = self.__pygameFont.render(self.__text, self.__aa, self.__colour)

    def aa(self):
        return self.__aa

    def aa(self, aa: bool):
        self.__aa = aa
        self.__pygameRender = self.__pygameFont.render(self.__text, self.__aa, self.__colour)

    def colour(self):
        return self.__text

    def colour(self, colour: str):
        self.__colour = colour
        self.__pygameRender = self.__pygameFont.render(self.__text, self.__aa, self.__colour)

    def x(self):
        return self.__x

    def x(self, x: int):
        self.__x = x
        self.__rect = self.__pygameRender.get_rect(center = (self.__x, self.__y))

    def y(self):
        return self.__y

    def y(self, y: int):
        self.__y = y
        self.__rect = self.__pygameRender.get_rect(center = (self.__x, self.__y))

    def rect(self):
        return self.__rect

    def height(self):
        return self.__rect.height

    def width(self):
        return self.__rect.width

class OptExecutePy(OptionFactory):
    def __init__(self, py = None):
        #if py == None: raise TypeError("no python file is given to execute")
        super().__init__()
        self.__pyFile = py

    def action(self):
        if self.__pyfile == None: return
        with(self.__pyfile, "r") as file:
            script_code = file.read()

        exec(script_code)

class Menu:
    def __init__(self):
        self.__optionList = []
        self.__size = 0#size of optionList
        self.__x = 0#these coordinates are the top left position of the menu!
        self.__y = 0
        self.__width = 0
        self.__height = 0
        self.__pointer = 0 #pointer 'points' to option 0. when option 0 is selected, run option's action
        self.__pointerImage = OptionFactory()
        self.__pointerImage.x(30)
        self.__pointerImage.y(30)
        self.__pointerImage.font('font/arial.ttf')
        self.__pointerImage.fontSize(initSettings["globalFontSize"])
        self.__pointerImage.text('>')
        self.__pointerImage.aa(False)
        self.__pointerImage.colour('White')

    def appendOpt(self, opt: OptionFactory):
        self.__optionList.append(opt)
        self.__size += 1
        #calculate rectangle size--------------------------------------------------------------
        optSize = opt.rect()
        if (optSize.width + self.__pointerImage.width()) > self.__width: 
            self.__width = optSize.width + self.__pointerImage.width()
        self.__height += optSize.height

    def popOpt(self, opt: OptionFactory):
        if opt in self.__optionList:
            self.__optionList.remove(opt)
            self.__size -= 1

        else: return
        #calculate rectangle size--------------------------------------------------------------
        self.__width = 0
        self.__height = 0
        for opti in self.__optionList:
            if (opti.width() + self.__pointerImage.width()) > self.__width: 
                self.__width = opti.width() + self.__pointerImage.width()
            self.__height += opti.height()

    
    def optionList(self):
        return self.__optionList

    def lineUpOptions(self, x = 10, y = 10):
        if not isinstance(x, int): raise TypeError("lineUpOptions's input must be an integer")
        if not isinstance(y, int): raise TypeError("lineUpOptions's input must be an integer")
        
        self.__x = x
        self.__y = y

        yMarker = y

        self.__pointerImage.alignLeft(x)

        cnt = 0
        for opt in self.__optionList:
            opt.alignLeft(x + self.__pointerImage.width())
            opt.alignTop(yMarker)
            if cnt == self.__pointer: self.__pointerImage.alignTop(yMarker)
            yMarker += opt.height()
            cnt += 1

    def drawMenu(self, screen):
        self.lineUpOptions(self.__x,self.__y)
        self.__pointerImage.drawObj(screen)
        for opt in self.__optionList:
            opt.drawObj(screen)

    def incPointer(self):
        if self.__pointer + 1 > self.__size: return
        self.__pointer += 1
        
    def decPointer(self):
        if self.__pointer - 1 < 0: return
        self.__pointer -= 1

    def executeOpt(self):
        self.__optionList[self.__pointer].action()

    def executeMenu(self, screen, clock):
        surface = pygame.Surface((initSettings["resolutionWidth"],initSettings["resolutionHeight"]))
        surface.fill('Black')
        #bg is black bg for now, picture implementation to be done later
        self.lineUpOptions(10, 10)
        option0 = OptionFactory()
        option0.text('Return')
        option0.aa(False)   
        option0.colour('White')
        self.appendOpt(option0)

        loop = True
        while loop:
            #event handling-------------------------------------------------------------------------
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_DOWN:
                        self.incPointer()

                    if event.key == pygame.K_UP:
                        self.decPointer()

                    if event.key == pygame.K_RETURN:
                        self.executeOpt()

                    if event.key == pygame.K_RETURN and self.__pointer == self.__size - 1:
                        loop = False
                        self.popOpt(option0)
                        
            #logic----------------------------------------------------------------------------------

            #screen updates-------------------------------------------------------------------------
            screen.blit(surface, (0,0))
            self.drawMenu(screen)

            #any other business---------------------------------------------------------------------
            pygame.display.update()
            clock.tick(60)

class OptToMenu(OptionFactory):
    def __init__(self, screen, clock):
        super().__init__()
        self.__menu = Menu()
        self.__screen = screen
        self.__clock = clock

    def action(self):
        self.__menu.executeMenu(self.__screen, self.__clock)

    def menu(self):
        return self.__menu

    def menu(self, menu: Menu):
        self.__menu = menu
        
class OptDropDownMenu(OptionFactory):#dont know how to select the drop down options logic
    def __init__(self, screen, clock):
        super().__init__()
        self.__optionList = []
        self.__screen = screen
        self.__clock = clock
        self.__drop = False
        self.__optionListHeight = 0
        self.__optionListWidth = 0
        self.__size = 0

    def action(self):
        if not self.__drop:
            self.__drop = True

        else:
            self.__drop = False

    def appendOpt(self, opt: OptionFactory):
        self.__optionList.append(opt)
        self.__size += 1
        self.__optionListHeight += opt.height()
        if self.__optionListWidth < opt.width():
            self.__optionListWidth = opt.width()

        print("option List height = ", self.__optionListHeight)

    def popOpt(self, opt: OptionFactory):
        if opt in self.__optionList:
            self.__optionList.pop(opt)
            self.__size -= 1

        else: return
        self.__optionListHeight -= opt.height()
        self.__optionListWidth = 0
        for opti in self.__optionList:
            if opti.width > self.__optionListWidth: 
                self.__optionListWidth = opti.width()

    def drawObj(self, screen):
        super().drawObj(screen)
        if self.__drop == True:
            xMarker = super().rect().left + 10
            yMarker = super().rect().bottom

            for opt in self.__optionList:
                opt.alignLeft(xMarker)
                opt.alignTop(yMarker)
                opt.drawObj(screen)
                yMarker += opt.height()


    def height(self):
        if self.__drop:
            h = super().height() + self.__optionListHeight
            return h

        else: return super().height()


    def width(self):
        if self.__drop:
            w = super().width() + self.__optionListWidth
            return w

        else: return super().width()
        
class OptLeftRightSelect(OptionFactory):
    def __init__(self, screen, clock):
        super().__init__()
        self.__optionList = []
        self.__size = 0
        self.__screen = screen
        self.__clock = clock
        self.__pointer = 0
        self.__maxWidth = 0

        option0 = OptionFactory()#this option is meant to do nothing
        option0.font('font/arial.ttf')
        option0.fontSize(initSettings["globalFontSize"])
        option0.text('select an option')
        option0.aa(False)
        option0.colour('White')
        self.__optionList.append(option0)
        self.__size += 1
        self.maxWidth = option0.rect().width

    def action(self):
        w = super().rect().width + self.__maxWidth
        h = super().rect().height
        surface = pygame.Surface((w, h))
        surface.fill('Red')

        loop = True
        while loop:
            #event handling-------------------------------------------------------------------------
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        if self.__pointer == 0:
                            self.__pointer = self.__size - 1

                        else: 
                            self.__pointer -= 1

                    if event.key == pygame.K_RIGHT:
                        if self.__pointer == self.__size - 1:
                            self.__pointer = 0

                        else: 
                            self.__pointer += 1

                    if event.key == pygame.K_RETURN:
                        self.__optionList[self.__pointer].action()
                        return
                        
            #logic----------------------------------------------------------------------------------

            #screen updates-------------------------------------------------------------------------
            x = super().rect().left
            y = super().rect().top
            self.__screen.blit(surface, (x, y))
            self.drawObj(self.__screen)

            #any other business---------------------------------------------------------------------
            pygame.display.update()
            self.__clock.tick(60)

    def appendOpt(self, opt: OptionFactory):
        self.__optionList.append(opt)
        self.__size += 1
        if self.__maxWidth < opt.width():
            self.__maxWidth = opt.width()

    def popOpt(self, opt: OptionFactory):
        if opt in self.__optionList:
            self.__optionList.pop(opt)
            self.__size -= 1

            self.__maxWidth = 0
            for opti in self.__optionList:
                if self.__maxWidth < opt.width():
                    self.__maxWidth = opt.width()

        else: return

    def drawObj(self, screen):
        super().drawObj(screen)
        r = super().rect().right
        self.__optionList[self.__pointer].alignLeft(r)
        t = super().rect().top
        self.__optionList[self.__pointer].alignTop(t)
        self.__optionList[self.__pointer].drawObj(screen)
        









