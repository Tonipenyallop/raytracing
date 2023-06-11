from Vec3 import Vec3


class Ray:
    def __init__(self, origin: Vec3, direction: Vec3):
        self.origin = origin
        self.direction = direction

    def rayColor(self) -> Vec3:
        unitDirection = Vec3(
            self.direction.x, self.direction.y, self.direction.z)
        # What the t stands for?
        t = 0.5 * (unitDirection.y + 1.0)
        return Vec3(1.0, 1.0, 1.0).multiply(1.0 - t).add(Vec3(0.5, 0.7, 1.0).multiply(t))
