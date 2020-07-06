import pgzrun
from math import *
from random import *
from pgzero.actor import Actor
from pgzero.loaders import sounds
from pgzero.clock import clock
from pgzero.screen import Screen
from pgzero.rect import Rect
from pgzero.keyboard import keys
screen: Screen  # 类型标注
TITLE = 'undetermined'

def draw():
    screen.clear() 
    start = 111,111
    end = 444,444
    color = (1,111,11)
    screen.draw.line(start,end,color) 

pgzrun.go()
