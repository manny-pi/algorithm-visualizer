import pygame 
from pygame import Surface, time
from __components.bar import Bar 

class Renderer: 
    """The Renderer class handles drawing the graphics to the screen."""

    __WINDOW_WIDTH = 1000
    __WINDOW_HEIGHT = 400
    __MAIN_WINDOW = pygame.display.set_mode((__WINDOW_WIDTH, __WINDOW_HEIGHT))

    def __init__(self, processor): 
        self.__processor = processor

        # Initialize pygame
        pygame.init()

        running = True
        while running:
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN: 
                    if event.key == pygame.K_u:
                        print('update frame')
                        self.__updateFrame()
            
            pygame.display.flip()

    def __updateFrame(self): 
        """Continues the processor."""

        self.__processor.cont() # continue to the next step in sorting algorithm
        self.__render()         # render the results of the processor

    def __render(self): 
        """Renders the encoded dataset to the screen."""

        
    def __generateBars(self): 
        """ Returns a list of Bar objects whose colors correspond with the values in the dataset """ 

        # Set the width and height of the bar relative to the window
        size = len(self.__processor.encodedDataset)
        barWidth = Renderer.__WINDOW_WIDTH / size
        barHeight = Renderer.__WINDOW_HEIGHT

        j = 0 
        bars = list() 
        for j in range(size): 
            bar = Bar(value=dataset[j], dim=(barWidth, barHeight), bottomleft=(j * barWidth, barHeight))
            bars.append(bar)

        return bars 


if __name__ == "__main__": 
    Renderer(None)