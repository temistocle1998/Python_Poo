import math
class Vecteur:
    """La valsse va representer un vecteur"""
    def __init__(self, a, b):
        self.x = a
        self.y = b
    def norme(self):
        return math.sqrt(self.x**2 + self.y**2)
