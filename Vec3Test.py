import unittest
from Vec3 import Vec3


class Vec3Test(unittest.TestCase):
    def testAdd(self):
        a = Vec3(1, 2, 3)
        b = Vec3(4, 5, 6)
        c = a.add(b)
        self.assertEqual(c.x, 5)
        self.assertEqual(c.y, 7)
        self.assertEqual(c.z, 9)

    def testsubstruct(self):
        a = Vec3(1, 2, 3)
        b = Vec3(4, 5, 6)
        c = a.substruct(b)
        self.assertEqual(c.x, -3)
        self.assertEqual(c.y, -3)
        self.assertEqual(c.z, -3)

    def testMultiply(self):
        a = Vec3(1, 2, 3)
        b = 10
        c = a.multiply(b)
        self.assertEqual(c.x, 10)
        self.assertEqual(c.y, 20)
        self.assertEqual(c.z, 30)

    def testDevide(self):
        a = Vec3(1, 2, 3)
        b = 10
        c = a.devide(b)
        self.assertAlmostEqual(c.x, 0.1)
        self.assertAlmostEqual(c.y, 0.2)
        self.assertAlmostEqual(c.z, 0.3)

    def testLength(self):
        a = Vec3(3, 4, 0)
        b = a.length()
        self.assertEqual(b, 5)

    def testSquare(self):
        a = Vec3(3, 4, 1)
        b = a.square()
        self.assertEqual(b, 26)


if __name__ == '__main__':
    unittest.main()
