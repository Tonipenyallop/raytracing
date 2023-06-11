from typing import Optional
from Vec3 import Vec3
import math
from Ray import Ray

# image
aspectRatio = 16.0 / 9.0
imageWidth = 400.0
imageHeight = imageWidth / aspectRatio

# camera
viewportHeight = 2.0
viewportWidth = aspectRatio * viewportHeight
focalLength = 1.0

origin = Vec3(0.0, 0.0, 0.0)
horizontal = Vec3(viewportWidth, 0.0, 0.0)
vertical = Vec3(0.0, viewportHeight, 0.0)
forward = Vec3(0.0, 0.0, focalLength)
# camera is center so substruct half of x, y and z
lowerLeftCorner = origin.substruct(horizontal.devide(2.0)).substruct(
    vertical.devide(2.0)).substruct(forward.devide(2.0))


# render

print('P3')
print(math.floor(imageWidth), math.floor(imageHeight))
print('255')
for i in range(math.floor(imageHeight) - 1, -1, -1):
    for j in range(math.floor(imageWidth)):
        heightUnit = j / (imageWidth - 1)
        widthUnit = i / (imageHeight - 1)

        rayDirection = horizontal.multiply(heightUnit).add(lowerLeftCorner).add(
            vertical.multiply(widthUnit).substruct(origin))
        ray = Ray(origin, rayDirection)
        pixelColor = ray.rayColor()
        pixelColor.writeColor()
