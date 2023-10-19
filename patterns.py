import math
import random
import numpy as np
from utils import add_row, random_color, merge_subweave, create_subweave
from init import app
from constants import RED, GREEN, BLUE

def true_random(length=10):
    subweave = create_subweave()
    for i in range(length):
        starts = np.random.randint(0, subweave.shape[1]-2, size=random.randint(1, subweave.shape[1]-2))
        ends = np.random.randint(0, subweave.shape[1], size=len(starts))
        colors = np.array([random_color() for color in range(len(starts))])
        # make sure ends are always larger than starts
        for j in range(len(starts)):
            if starts[j] > ends[j]:
                starts[j], ends[j] = ends[j], starts[j]
        add_row(starts, ends, colors, subweave)
    merge_subweave(subweave)

def random_row(length=10):
    subweave = create_subweave()
    for i in range(length):
        add_row(colors=[random_color()], df=subweave)
    merge_subweave(subweave)

def random_simple(length=10):
    subweave = create_subweave()
    for i in range(length):
        start = random.randint(0, app.weave.shape[1]-1)
        end = random.randint(start+1, app.weave.shape[1])
        add_row([start], [end], [random_color()], subweave)
    merge_subweave(subweave)

def sine(length=10):
    subweave = create_subweave()
    array = np.arange(0, length)
    sine = np.round(np.sin(array), 2)
    #x = round(math.sin(x), 2)
    
    for x in sine:
        if x > 0 and x < 0.5:
            add_row(colors=[RED], df=subweave)
        elif x < 0 and x > -0.5:
            add_row(colors=[BLUE], df=subweave)
        else:
            add_row(colors=[GREEN], df=subweave)

        # if x > 0 and x < 0.5:
        #     add_row(color=random_color())
        # elif x < 0 and x > -0.5:
        #     add_row(color=random_color())
        # else:
        #     add_row(color=random_color())
    
    merge_subweave(subweave)

patterns_list = [
                    true_random,
                    random_row,
                    random_simple,
                    sine
                ]
