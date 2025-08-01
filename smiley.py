from sense_hat import SenseHat


class Smiley:
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
    BLANK = (0, 0, 0)
    BLUE = (0, 0, 255)

    def __init__(self, complexion=None):
     self.sense_hat = SenseHat()
     self.my_complexion = complexion if complexion else self.YELLOW

     Y = self.complexion()
     O = self.BLANK
     self.pixels = [
        O, Y, Y, Y, Y, Y, Y, O,
        Y, Y, Y, Y, Y, Y, Y, Y,
        Y, Y, Y, Y, Y, Y, Y, Y,
        Y, Y, Y, Y, Y, Y, Y, Y,
        Y, Y, Y, Y, Y, Y, Y, Y,
        Y, Y, Y, Y, Y, Y, Y, Y,
        Y, Y, Y, Y, Y, Y, Y, Y,
        O, Y, Y, Y, Y, Y, Y, O,
    ]


    def complexion(self):
     return self.my_complexion


    def dim_display(self, dimmed=True):
        """
        Set the SenseHat's light intensity to low (True) or high (False)
        :param dimmed: Dim the display if True, otherwise don't dim
        """
        self.sense_hat.low_light = dimmed

    def show(self):
        """
        Show the smiley on the screen.
        """
        self.sense_hat.set_pixels(self.pixels)
