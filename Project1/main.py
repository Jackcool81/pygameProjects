import pygame
# import pyautogui
from pygame.locals import *
import time
import NoteShapes
import random
from mido import MidiFile
import mido
import rtmidi
import os
directory_path = os.getcwd()
# WIDTH = int(input("Please Enter Screen Width (ex 640) "))
# HEIGHT = int(input("Please Enter Screen Height (ex 480) "))
# NOTE_WIDTH = int(input("Please Enter space between notes (ex 8) "))
WIDTH = 640
HEIGHT = 480
NOTE_WIDTH = 8
print("Do you have a midi device plugged in? Yes (1) No (2)")
midi_in = input("1/2 ")
if (midi_in == "1"):
    inmidi = rtmidi.MidiIn()
    print(inmidi.get_port_name(1))
    portname = inmidi.get_port_name(1)
    port = mido.open_input(portname)
else:
    print("Please plug in Midi Device")
    exit()
red = (255,0,0) 
yellow = (255, 255, 0)
#blue = (0,0,255)
#SCALING
MIDDLE_SCREEN = WIDTH / 2
if WIDTH > 640:
    direction = 1
else:
    direction = 1
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("test")
screen.fill((0,0,0))
red1 = pygame.Vector3(255, 0, 0)
yellow1 = pygame.Vector3(255,255,0)
blue = pygame.Vector3(0,0,255)
lerpcolor = pygame.math.Vector3.lerp(red1, yellow1, 0.5)
color = (lerpcolor.x, lerpcolor.y, lerpcolor.z)
def render(cameraX):
    if bool(shapes) == True and shapes[-1].getX() != MIDDLE_SCREEN:
        screen.fill((0,0,0))
        #blue_back.move(x * -1)
        #if not we need to update camera
        cameraX = cameraX + -x
        #blue_back.render()
        #move background here aswell
        for shape in shapes:
            shape.move(x)
            shape.getX()
            shape.render()
        return cameraX
    else:
        screen.fill((0,0,0))
        #set canera to target note number when we've reached our destination
        if bool(shapes) == True:
            cameraX = shapes[-1].getOgX()
        #blue_back.move(x * -1)
        #blue_back.render()
        for shape in shapes:
            shape.render()
        return cameraX
#circle.changeColor()
shaper = False
shapes = [] #move these opp of eachother
#background_shape = []
#blue_back = BackSquare(screen)
cameraX = MIDDLE_SCREEN
middle = WIDTH - (127 * NOTE_WIDTH) / 2
print(cameraX)
x = 0
target = 0
#blue_back.render()
FPS = 120
clock = pygame.time.Clock()
note = [""] * 127

countextra = 0 
while True:
    for msg in MidiFile('simpl.mid').play():
        if countextra < 2: 
            countextra += 1
           
            continue
    #for msg in port.iter_pending(): #try just in port for playing from midi
        if msg.note <= 70:
            if msg.type == "note_on":
                print("hi")
                notenum = (msg.note * NOTE_WIDTH) - middle
                xCam = notenum - cameraX #this gets the difference between the previous
                #cameraX and the new note
                xreal = xCam + MIDDLE_SCREEN #add the difference to 320,
                if xreal > MIDDLE_SCREEN: #check if we need to move everything right or left
                                         #to get to that new position
                    x = -direction
                else:
                    x = direction
                #shapes.append(Shapes.Circle(screen, xreal, 1100))
                shapes.append(NoteShapes.Circle(screen, xreal, notenum, msg, len(shapes)))
            note[msg.note] = msg.type
        else:
            if msg.type == "note_on":
                notenum = (msg.note * NOTE_WIDTH) - middle
                xCam = notenum - cameraX #this gets the difference between the previous
                #cameraX and the new note
                xreal = xCam + MIDDLE_SCREEN #add the difference to 320,
                if xreal > MIDDLE_SCREEN: #check if we need to move everything right or left
                    #to get to that new position
                    x = -direction
                else:
                    x = direction
                #shapes.append(Shapes.Circle(screen, xreal, 1100))
                shapes.append(NoteShapes.Square(screen, xreal, notenum, msg, len(shapes)))
            note[msg.note] = msg.type
#print(note)
    if bool(shapes) == True and shapes[-1].getX() != MIDDLE_SCREEN:
        screen.fill((0,0,0))
        #blue_back.move(x * -1)
        #if not we need to update camera
        cameraX = cameraX + -x
        #blue_back.render()
        #move background here aswell
        for shape in shapes:
        #print(shape.note.type)
            if note[shape.note.note] == "note_off":
                #shape.changeSizeOT(false)
                shapes.remove(shape)
            else:
                shape.move(x)
                shape.getX()
                shape.render()
    else:
        screen.fill((0,0,0))
        #set canera to target note number when we've reached our destination
        x = 0
        if bool(shapes) == True:
            cameraX = shapes[-1].getOgX()
    #blue_back.move(x * -1)
    #blue_back.render()
        for shape in shapes:
        #print(shape.note.type)
            if note[shape.note.note] == "note_off":
                shapes.remove(shape)
            shape.render()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.display.quit()
                pygame.quit()
                exit()
            if event.key == pygame.K_p:
                random_save = random.randint(0, 10000)
                name = directory_path + "/screenshot" + str(random_save) + ".png"
                #name = "screenshot" + str(random_save) + ".png"
                #pygame.image.save(screen, name)
                #myScreenShot = pyautogui.screenshot()
            
    clock.tick(FPS)
    pygame.display.update()
#pygame.image.save(screen, "drawn.png")
#pygame.display.quit()
#pygame.quit()
#exit()