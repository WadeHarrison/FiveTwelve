"""
The game state and logic (model component) of 512, 
a game based on 2048 with a few changes. 
This is the 'model' part of the model-view-controller
construction plan.  It must NOT depend on any
particular view component, but it produces event 
notifications to trigger view updates. 
"""

from game_element import GameElement, GameEvent, EventKind
from typing import List, Tuple, Optional
import random

# Configuration constants
GRID_SIZE = 4

class Vec():
    """A Vec is an (x,y) or (row, column) pair that
    represents distance along two orthogonal axes.
    Interpreted as a position, a Vec represents
    distance from (0,0).  Interpreted as movement,
    it represents distance from another position.
    Thus we can add two Vecs to get a Vec.
    """
    #Fixme:  We need a constructor, and __add__ method, and __eq__.
    
    def __init__(self, x, y):
       self.x = x
       self.y = y
       return None
    
    def __add__(self, vector1, vector2):
        v3.x = vector1.x + vector2.x
        v3.y = vector1.y + vector2.y
        return(vector3.x,vector3.y)

    
    def __eq__(self, vector1, vector2)
        if vector1 == vector2:
            return True
        else:
            return False





class Tile(GameElement):
    """A slidy numbered thing."""

    def __init__(self):
        super().__init__()


class Board(GameElement):
    """The game grid.  Inherits 'add_listener' and 'notify_all'
    methods from game_element.GameElement so that the game
    can be displayed graphically.
    """

    def __init__(self):
        super().__init__()
        self.tiles = [ None, None
                        None,None ]  # FIXME: a grid holds a matrix of tiles

    def has_empty(self) -> bool:
        """Is there at least one grid element without a tile?"""
        
        return False
        # FIXME: Should return True if there is some element with value None

    def place_tile(self):
        """Place a tile on a randomly chosen empty square."""
        return
        #FIXME

    def score(self) -> int:
        """Calculate a score from the board.
        (Differs from classic 1024, which calculates score
        based on sequence of moves rather than state of
        board.
        """
        return 0
        #FIXME


def main():
    v1 = Vec(3,4)
    print(v1)

if __name__ == "__main__":
    main()