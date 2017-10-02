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
from noise import pnoise2, snoise2

width=256
height=256

f = open('img.raw', 'wt')
octaves = 5
freq = 16.0 * octaves
f.write('P2\n')
f.write('%s %s\n'% (width,height))
f.write('255\n')

for y in range(width):
	for x in range(height):
                noise = pnoise2(x / freq, y / freq, octaves )
		# f.write("%s\n" % int(noise * 127.0 + 128.0))
		f.write("%s\n" % int(noise * 127.0 + 128.0))
f.close()
