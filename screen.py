from sense_hat import SenseHat
import random
from time import sleep

sense = SenseHat()

sense.clear()
matrix = [[0,0,0] for i in range(64)]
for i in range(8):
    for j in range(8):
        matrix[i*8+j] = [255,0,0];
        sense.set_pixels(matrix)
        sleep(0.1)
sleep(5)
sense.clear()
