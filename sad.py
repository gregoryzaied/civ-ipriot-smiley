from smiley import Smiley
import time  # Make sure this is at the top

class Sad(Smiley):
    def __init__(self):
        super().__init__(complexion=self.BLUE)  # Now Sad will be blue
        self.draw_mouth()
        self.draw_eyes()

    def draw_mouth(self):
        mouth = [49, 54, 42, 43, 44, 45]
        for pixel in mouth:
            self.pixels[pixel] = self.BLANK

    def draw_eyes(self, wide_open=True):
        eyes = [10, 13, 18, 21]
        for pixel in eyes:
            if wide_open:
                self.pixels[pixel] = self.BLANK
            else:
                self.pixels[pixel] = self.YELLOW

    def blink(self, delay=0.25):
        self.draw_eyes(wide_open=False)
        self.show()
        time.sleep(delay)
        self.draw_eyes(wide_open=True)
        self.show()
