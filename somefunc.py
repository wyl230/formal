from random import *

def rand_color():
    f = lambda : randint(1,255) 
    return f(),f(),f() 

def swing(*a):
    u = 100
    return [v + randint(-u,u) for v in a]