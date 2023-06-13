import unittest

from Ray import Ray
from Vec3 import Vec3


class RayTest(unittest.TestCase):
    def testHitSphere(self):
        origin = Vec3(0.0, 0.0, 0.0)
        direction = Vec3(1.0, 1.0, 1.0)
        ray = Ray(origin, direction)

        center = Vec3(0.0, 0.0, 1.0)
        self.assertEqual(ray.hitSphere(center, 0.0), False)
        self.assertEqual(ray.hitSphere(center, 0.5), False)
        self.assertEqual(ray.hitSphere(center, 1.0), True)
        self.assertEqual(ray.hitSphere(center, 2.0), True)


if __name__ == '__main__':
    unittest.main()
