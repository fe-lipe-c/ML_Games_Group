"""Nash Eliquilibrium test for Rock-Paper-Scissors game."""

import numpy as np


class Player:
    """Player class for Rock-Paper-Scissors game."""

    def __init__(self, name, p):
        self.strategy = name
        self.p = p

    def __str__(self):
        return self.name
