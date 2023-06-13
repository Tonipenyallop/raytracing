import math
from Vec3 import Vec3


class Ray:
    def __init__(self, origin: Vec3, direction: Vec3):
        self.origin = origin
        self.direction = direction

    def rayColor(self) -> Vec3:
        t = self.hitSphere(Vec3(0.0, 0.0, -1.0), 0.5)
        if t > 0.0:
            N = self.at(t).substruct(Vec3(0.0, 0.0, -1.0))
            return Vec3(N.x + 1.0, N.y + 1.0, N.z + 1.0).multiply(0.5)

        unitDirection = Vec3(
            self.direction.x, self.direction.y, self.direction.z)

        t = 0.5 * (unitDirection.y + 1.0)

        return Vec3(1.0, 1.0, 1.0).multiply(1.0 - t).add(Vec3(0.5, 0.7, 1.0).multiply(t))

    def hitSphere(self, center: Vec3, radious: float) -> float:
        oc = self.origin.substruct(center)
        a = self.direction.square()
        halfB = oc.dot(self.direction)
        c = oc.square() - radious ** 2
        dicriminant = halfB ** 2 - a * c
        if dicriminant < 0:
            return -1.0
        else:
            return (-halfB - math.sqrt(dicriminant)) / a

    def at(self, t: float) -> Vec3:
        return self.origin.add(self.direction.multiply(t))
