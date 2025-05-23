from smiley import Smiley

class Angry(Smiley):
    def __init__(self):
        super().__init__(complexion=self.RED)
        self.draw_mouth()
        self.draw_eyes()

    def draw_mouth(self):
        mouth = [41, 42, 43, 44, 45, 46]
        for pixel in mouth:
            self.pixels[pixel] = self.BLANK

    def draw_eyes(self, wide_open=True):
        eyes = [10, 13, 18, 21]
        for pixel in eyes:
            self.pixels[pixel] = self.RED if wide_open else self.BLANK
