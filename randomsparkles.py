#!/usr/bin/python3
from time import sleep
from colorzero import Color
from tree import RGBXmasTree
import random

tree = RGBXmasTree(brightness=0.1)
tree.color = (0,1,0)

def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return (r, g, b)

try:
    for pixel in tree:
        pixel.color = random_color()

    while True:
        pixel = random.choice(tree)
        pixel.color = random_color()
        sleep(0.5)
except KeyboardInterrupt:
    tree.off()
    tree.close()
