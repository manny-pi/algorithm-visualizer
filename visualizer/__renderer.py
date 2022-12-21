import pygame 
from pygame import Surface, time
from __components.bar import Bar 


class Renderer: 
    """The Renderer class handles drawing the graphics to the screen."""

    __WINDOW_WIDTH = 1000
    __WINDOW_HEIGHT = 400
    __MAIN_WINDOW = pygame.display.set_mode((__WINDOW_WIDTH, __WINDOW_HEIGHT))
    __CLOCK = time.Clock()
    __FRAME_RATE = 5

    def __init__(self, processor): 
        self.__processor = processor        # store the processor object used to run the algorithm
        self.__bars = self.__generateBars() # store the bars that are rendered to the screen

        # Initialize pygame
        pygame.init()

        running = True
        while running:
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    running = False
            self.__updateFrame()

    def __updateFrame(self): 
        """Continues the processor."""

        self.__processor.cont()             # continue to the next step in sorting algorithm
        self.__bars = self.__generateBars() # udpate the bars to corresponding with the sorted dataset
        self.__render()                     # render the results of the processor

    def __render(self): 
        """Renders the encoded dataset to the screen."""

        for bar in self.__bars: 
            Renderer.__MAIN_WINDOW.blit(bar.surface, bar.rect)
        pygame.display.flip()
        Renderer.__CLOCK.tick(Renderer.__FRAME_RATE)

    def __generateBars(self): 
        """Returns a list of Bar objects whose colors correspond with the values in the dataset.""" 

        # Set the width and height of the bar relative to the window
        size = len(self.__processor.encodedDataset)
        barWidth = Renderer.__WINDOW_WIDTH / size
        barHeight = Renderer.__WINDOW_HEIGHT
        
        j = 0 
        bars = list() 
        for j in range(size): 
            bar = Bar(
                color=self.__processor.encodedDataset[j].color, 
                dim=(barWidth, barHeight),
                bottomleft=(j * barWidth, barHeight))
            bars.append(bar)

        return bars 

    @classmethod 
    def setFrameRate(cls, frameRate): 
        Renderer.__FRAME_RATE = frameRate

if __name__ == "__main__": 
    Renderer(None)
