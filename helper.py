import pygame
import time
import math


WIDTH = 600
HEIGHT = 400
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class Point:
    AMPLITUDE = 50 
    ANG_FREQ = 10
    DECREASING_AMP_CT = 0.0000001
    IS_DECR = True
    def __init__(self, pos, start_time) -> None:
        self.pos = pos
        self.x = pos[0]
        self.y = pos[1]
        self.start_time = start_time 

    def move(self):
        self.y = HEIGHT//2 + (Point.AMPLITUDE)*math.sin(Point.ANG_FREQ*(time.time()-self.start_time))
        if Point.IS_DECR:
            Point.AMPLITUDE = Point.AMPLITUDE * pow(math.e, -Point.DECREASING_AMP_CT*(time.time()+1-self.start_time))

POINTS = [Point([50+i, HEIGHT//2], time.time()+i/100) for i in range(500)]


