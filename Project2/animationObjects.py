import pygame
# import skel

'''
animation class
Description: This class is designed to implement the animation object
which takes in a list of pygame rendered images, a time to play each frame
and wheter or not it will repeat. 

@params
frames: A list of pygame images
frameTime: A list of how many frames will each pygame image play
repeat: If the animation will repeat or not

'''
class animation():
    
    #intialize function
    def __init__ (self, frames, frameTime, repeat):
        self.frames = frames
        self.frameTime = frameTime
        self.index = 0 #determines which frame/frameTime we are on in the sequence
        self.count = 0 #counts how many times a frame is shown
        self.repeat = repeat
    
    #update holds the main algorithm for which frame will be show on screen
    
    def update(self, screen, rect):
        screen.blit(self.frames[self.index], rect)

        #checks if count has reached the max times this spectfic frame at self.index 
        #is shown
        if self.count == self.frameTime[self.index]:
            if self.repeat == True:
                self.index = (self.index + 1) % len(self.frames) #ensures repeat using wrapping
            else:
                #if not plays the last frame over and over
                self.index = self.index + 1
                if self.index >= len(self.frames):
                    self.index = len(self.frames) - 1
            self.count = 0
        self.count = self.count + 1
    
    #for changing how long each frame will play 
    def changeFrame(self, newTimes):
        self.frameTime = newTimes
        self.index = 0
        self.count = 0
        print(self.frameTime)
        

'''
Player class
Description: This class holds all the animations for the player so that in
main you can easily swap from each animation. 

@params: 
width: the width of the player
'''
class Player():
    #intialization function, sets up all the animations
    def __init__ (self, width):
        #Sets up the idle animation 
        idle1 = pygame.image.load("images\\Naruto\\Idle\\px1080\\idle1.png")
        DEFAULT_IMAGE_SIZE = (idle1.get_height() /2 ,  width * 0.08)
        idle1 = pygame.transform.scale(pygame.image.load("images\\Naruto\\Idle\\px1080\\idle1.png"), DEFAULT_IMAGE_SIZE)
        idle2 = pygame.transform.scale(pygame.image.load("images\\Naruto\\Idle\\px1080\\idle2.png"), DEFAULT_IMAGE_SIZE)
        idle3 = pygame.transform.scale(pygame.image.load("images\\Naruto\\Idle\\px1080\\idle3.png"), DEFAULT_IMAGE_SIZE)
        idle4 = pygame.transform.scale(pygame.image.load("images\\Naruto\\Idle\\px1080\\idle4.png"), DEFAULT_IMAGE_SIZE)
        playerIdleFrames = [idle1, idle2, idle3, idle4]
        # Scale the image to your needed size
        playerIdleTimeFrames = [7, 7, 7, 7]
        self.idle = animation(playerIdleFrames, playerIdleTimeFrames, True)

        #Sets up the running animation
        idle1 = pygame.transform.scale(pygame.image.load("images\\Naruto\\Run\\1.png"), DEFAULT_IMAGE_SIZE)
        idle2 = pygame.transform.scale(pygame.image.load("images\\Naruto\\Run\\2.png"), DEFAULT_IMAGE_SIZE)
        idle3 = pygame.transform.scale(pygame.image.load("images\\Naruto\\Run\\3.png"), DEFAULT_IMAGE_SIZE)
        idle4 = pygame.transform.scale(pygame.image.load("images\\Naruto\\Run\\4.png"), DEFAULT_IMAGE_SIZE)
        idle5 = pygame.transform.scale(pygame.image.load("images\\Naruto\\Run\\5.png"), DEFAULT_IMAGE_SIZE)
        idle6 = pygame.transform.scale(pygame.image.load("images\\Naruto\\Run\\6.png"), DEFAULT_IMAGE_SIZE)
        # Set the size for the image

        playerIdleFrames = [idle1, idle2, idle3, idle4, idle5, idle6]
        for i in range(len(playerIdleFrames)):
            playerIdleFrames[i] = pygame.transform.flip(playerIdleFrames[i], True, False)

        # Scale the image to your needed size 
        playerIdleTimeFrames = [4, 4, 4, 3, 4, 4]
        self.run = animation(playerIdleFrames, playerIdleTimeFrames, True)

        #Sets up the jumping animation
        idle1 = pygame.transform.scale(pygame.image.load("images\\Naruto\\jump\\1.png"), DEFAULT_IMAGE_SIZE)
        idle2 = pygame.transform.scale(pygame.image.load("images\\Naruto\\jump\\2.png"), DEFAULT_IMAGE_SIZE)
        idle1 = pygame.image.load("images\\Naruto\\jump\\1.png")
        DEFAULT_IMAGE_SIZE = (idle1.get_height() /2 ,  idle1.get_width() /2)
        idle1 = pygame.transform.scale(pygame.image.load("images\\Naruto\\jump\\1.png"), DEFAULT_IMAGE_SIZE)
        idle2 = pygame.transform.scale(pygame.image.load("images\\Naruto\\jump\\2.png"), DEFAULT_IMAGE_SIZE)
        playerIdleTimeFrames = [10, 10]
        playerIdleFrames = [idle1, idle2]
        self.jump = animation(playerIdleFrames, playerIdleTimeFrames, False)




    #Update function
    #Description: determines which animation state the player should be in 
    #Params: 
    #rect- where the player is on the screen
    #screen - the object that holds the pygame screen
    #animationNum - which animation to play
    def update(self, screen, rect, animationNum):
        if (animationNum == "run"):
            self.run.update(screen, rect)
        elif (animationNum == "walk"):
            self.idle.update(screen, rect)
        elif (animationNum == "jump"):
            self.jump.update(screen, rect)

    #changeFrameTime 
    #Description Changes the frame time of whatever animation
    #Params:
    #animationNum: which animation to change
    #newTimes: List of numbers indicated how many frames each image should play for
    def changeFrameTime(self, animationNum, newTimes):
        if (animationNum == "run"):
            self.run.changeFrame(newTimes)
        elif (animationNum == "walk"):
            self.idle.changeFrame(newTimes)
        elif (animationNum == "jump"):
            self.jump.changeFrame(newTimes)
        

        
