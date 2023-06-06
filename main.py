import random
import math


print('P3')
print('256 256')
print('255')


class Color:
    def __init__(self):
        self.pixel = []
        self.rainbow = []
        for _ in range(3):
            self.pixel.append(str(math.floor(random.random() * 255)))

        blue = 255
        for green in range(256):
            for red in range(256):
                self.rainbow.append(str(red))
                self.rainbow.append(str(green))
                self.rainbow.append(str(blue))

    def getColor(self):
        return ' '.join(self.pixel)

    def getRainbow(self):
        return ' '.join(self.rainbow)


color = Color()
print(Color().getRainbow())
