"""
This class will encode the dataset in the way we specify. 

It works in conjunction with the Processor and Renderer classes.
"""

class Encoder: 
    
    @classmethod
    def encodeDataset(cls, dataset, by):
        """Encodes the dataset based on the value of by.
        'height': encode the height of the graphical representation
        'color': encode the color of the graphical representation
        
        returns an array of encoded elements.""" 

        ret = []
        if by == "color":
            for value in dataset:
                ret.append(ColorCoded(value, (255, 0, 0)))
            
        return ret

class ColorCoded: 
    """Represents the components that are used for the visualization."""

    def __init__(self, value, color): 

        self.value = value
        self.color = color

    def __repr__(self): 

        return f"({self.value}, (R={self.color[0]}, G={self.color[1]}, B={self.color[2]}))"

    def __le__(self, other): 

        return self.value <= other.value
    
    def __ge__(self, other): 

        return self.value >= other.value

    def __lt__(self, other): 

        return self.value < other.value

    def __gt__(self, other): 
        
        return self.value > other.value
