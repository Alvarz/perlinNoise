#!/usr/bin/env python

# pip install noise
# pip install pyglet
# noise2(x, y, octaves=1, persistence=0.5, lacunarity=2.0, repeatx=1024, repeaty=1024, base=0.0)

# octaves -- specifies the number of passes, defaults to 1 (simple noise).
        
# persistence -- specifies the amplitude of each successive octave relative
# to the one below it. Defaults to 0.5 (each higher octave's amplitude
# is halved). Note the amplitude of the first pass is always 1.0.

# lacunarity -- specifies the frequency of each successive octave relative
# to the one below it, similar to persistence. Defaults to 2.0.

# repeatx, repeaty -- specifies the interval along each axis when 
# the noise values repeat. This can be used as the tile size for creating 
# tileable textures

# base -- specifies a fixed offset for the noise coordinates. Useful for
# generating different noise textures with the same repeat interval

import sys
import math
from PIL import Image, ImageDraw
from noise import pnoise2, snoise2

width=256
height=256

image = Image.new("RGB", (width, height))
draw = ImageDraw.Draw(image)
pixels = image.load()

green = (76, 136, 0)
yellow = (224, 143, 0)
blue = (13, 53, 251)
darkGreen = (0, 51, 0)
white = (255, 255, 255)

imgAr = [[0.0 for i in range(width)] for j in range(height)] # image array

f = open('heightmap.raw', 'wt')

octaves = 5
persistence = 0.5
lacunarity = 2.0
repeatx = 1024 
repeaty = 1024
base = 0
freq = 16.0 * octaves
f.write('P2\n')
f.write('%s %s\n'% (width,height))
f.write('255\n')

useSimple = True

for y in range(height):
	for x in range(width):
                '''
                if(useSimple):
                    noise = snoise2(x / freq, y / freq, octaves, persistence,
                            lacunarity, repeatx, repeaty, base )
                else:
                    noise = pnoise2(x / freq, y / freq, octaves, persistence,
                            lacunarity, repeatx, repeaty, base )
                '''
                noise = pnoise2(x / freq, y / freq, octaves, persistence,
                        lacunarity, repeatx, repeaty, base )

                    # imgAr[y][x] = noise # add image layers together
                tmpComputed = noise * 127.0 + 128.0

                noise2 = snoise2(x / tmpComputed, y / tmpComputed, octaves, persistence,
                        lacunarity, repeatx, repeaty, base )

                computed = noise2 * 127.0 + 128.0

                #computed = (x + math.sin(computed) * 8.0) + (y + math.cos(computed) * 8.0)

                imgAr[y][x] = int(computed)
                # c = int(imgAr[y][x] / 128.0 * 255)
                # c = int(imgAr[y][x])
                # pixels[x, y] = (c, c, c)
                if(int(computed) < 100):
                    pixels[x, y] = blue
                elif(int(computed) >= 110 and int(computed) <= 120):
                    pixels[x, y] = yellow
                elif(int(computed) >= 121 and int(computed) <= 150):
                    pixels[x, y] = green
                elif(int(computed) > 150 and int(computed) < 199):
                    pixels[x, y] = darkGreen
                elif(int(computed) >= 200):
                    pixels[x, y] = white
                else:
                    pixels[x, y] = yellow
		# f.write("%s\n" % int(noise * 127.0 + 128.0))
		f.write("%s\n" % int(computed))
f.close()


# paint image

#label = "Persistence = "
#draw.text((0, 0), label, (0, 255, 0)) # write to top-left using green color
image.save("PerlinNoise.png", "PNG")
