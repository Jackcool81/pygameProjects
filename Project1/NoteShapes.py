'''
This file holds information for the Shapes Object which is used to rendering the notes, 
unique shapes use inheritance off of the main Shapes class. 


'''
import pygame
import random
pygame.init()


#Shapes Class 
#Description: Parent class that Intializes important variables 
# used for telling whether or not a midi note is
# on, being held down, the height width and color, and position.
#Params: 
#screen - where to draw the note
#x - where the note actually is 
#ogx - where the ntoe is in relation to camera space
#note - the note number given from midi 
#shapes - the array of all the shapes currently being rendered

class Shapes():
    #Intializing all useful params
    def __init__(self, screen, x, ogx, note, shapes):
        red1 = pygame.Vector3(255, 0, 0)
        yellow1 = pygame.Vector3(255,255,0)
        green1 = pygame.Vector3(0,255,0)
        blue1 = pygame.Vector3(0,0,255)
        self.colors = [red1, yellow1, green1, blue1]
        scale = shapes * screen.get_height() / 30
        difference = random.randint(60, 100)
        self.height = (screen.get_height()/2 - difference) - scale
        self.x = x
        self.screen = screen
        self.spawned = ogx
        self.note = note
        self.on = True
    def move(self,x):
        self.x = self.x + x
    def getX(self):
        return self.x
    def getOgX(self):
        return self.spawned

#Circle class
#Description: Renders a pygame circle that will ovulate depending on if you 
#hold the note down or release it
#inherits from the Shapes class
class Circle(Shapes):
    def __init__(self, screen, x, ogx, note, shapes):
        Shapes.__init__(self, screen, x, ogx, note, shapes)
        self.last = 50
        self.circle = 0
        self.start = 0.0
        self.color2 = False
        self.startSize = 0
        self.i = 0
        self.back = False

    #render function
    #description: Will ovulate the notes size depending on if the note is being held down
    def render(self):
        Circle.changeColorOT(self)
        Circle.changeSizeOT(self, False)
        self.circle = pygame.draw.circle(self.screen, self.color, (self.x, self.height),
        self.last)

    #changeColorOT function
    #Description: Uses lerp to take two colors and cycle through them frame by frame.
    #once it reaches the end of the list of colors it resets
    def changeColorOT(self):
        self.start = self.start + 0.01
        index = (self.i + 1) % 4
        lerpcolor = pygame.math.Vector3.lerp(self.colors[self.i], self.colors[index],
        self.start)
        self.color = (lerpcolor.x, lerpcolor.y, lerpcolor.z)
        if self.start >= 0.9:
            self.start = 0
            self.i = self.i + 1
            if self.i >= 4:
                self.i = 0
    def changeSizeOT(self, ended):
        if ended == False:
            if self.back == False:
                direction = 0.1
                self.startSize = self.startSize + 0.01
                if self.startSize > 1:
                    self.back = True
            else:
                direction = -0.1
                self.startSize = self.startSize - 0.01
                if self.startSize < 0:
                    self.back = False
        else:
            direction = -3
            self.last = self.last + direction

#Square class
#Description: Renders a pygame square that will ovulate color depending on if you 
#hold the note down or release it
#inherits from the Shapes class
class Square(Shapes):
    def __init__(self, screen, x, ogx, note, shapes):
        Shapes.__init__(self, screen, x, ogx, note, shapes)
        self.last = 640 / 6
        self.circle = 0
        self.start = 0.0
        self.color2 = False
        self.startSize = 0
        self.i = 1
        self.back = False
    
    #render function
    #description: Will ovulate the notes size depending on if the note is being held down
    def render(self):
        Square.changeColorOT(self)
        Square.changeSizeOT(self, False)
        self.square = pygame.draw.rect(self.screen, self.color, pygame.Rect(self.x,
        self.height, self.last, self.last))

    #Description: Uses lerp to take two colors and cycle through them frame by frame.
    #once it reaches the end of the list of colors it resets
    def changeColorOT(self):
        self.start = self.start + 0.01
        index = (self.i + 1) % 4
        lerpcolor = pygame.math.Vector3.lerp(self.colors[self.i], self.colors[index],
        self.start)
        self.color = (lerpcolor.x, lerpcolor.y, lerpcolor.z)
        if self.start >= 0.9:
            self.start = 0
            self.i = self.i + 1
            if self.i >= 4:
                self.i = 0

    def changeSizeOT(self, ended):
        if ended == False:
            if self.back == False:
                direction = 0.1
                self.startSize = self.startSize + 0.01
                if self.startSize > 1:
                    self.back = True
            else:
                direction = -0.1
                self.startSize = self.startSize - 0.01
                if self.startSize < 0:
                    self.back = False
        else:
            direction = -3
            self.last = self.last + direction