from typing import List, Dict, Tuple, Optional
import math


class Vec3:
    def __init__(self, x: float, y: float, z: float) -> None:
        self.x = x
        self.y = y
        self.z = z

    def add(self, input: Optional['Vec3']):
        return Vec3(self.x + input.x, self.y + input.y, self.z + input.z)

    def substruct(self, input: Optional['Vec3']):
        return Vec3(self.x - input.x, self.y - input.y, self.z - input.z)

    def multiply(self, input: float):
        return Vec3(self.x * input, self.y * input, self.z * input)

    def devide(self, input: float):
        return self.multiply(1/input)

    def length(self) -> Optional['Vec3']:
        return math.sqrt(self.square())

    def square(self):
        return (self.x ** 2) + (self.y ** 2) + (self.z ** 2)

    def writeColor(self):
        print(math.floor(self.x * 255),
              math.floor(self.y * 255), math.floor(self.z * 255))

    def dot(self, v: Optional['Vec3']) -> float:
        return (self.x * v.x) + (self.y * v.y) + (self.z * v.z)

    def unitVector(self, v: Optional['Vec3']) -> Optional['Vec3']:
        return v/v.length()
