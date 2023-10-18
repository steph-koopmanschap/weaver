import math
import numpy as np
import random

#import pandas as pd
from utils import add_row, row_stats, export_png, random_color
from init import app, init

RED = np.array([255, 0, 0])
GREEN = np.array([0, 255, 0])
BLUE = np.array([0, 0, 255])

columns_size = 400
generation_count = 500

init(columns_size)

array = np.arange(0, generation_count)
sine = np.round(np.sin(array), 2)
for i in range(generation_count):
    try:
        x = 1 / (i ** 2)
    except Exception:
        x = 1
    x = int(x * 255)
    
    
    add_row(color=np.array([x, x, x]))
    
    
    start = random.randint(0, app.weave.shape[1]-1)
    end = random.randint(start+1, app.weave.shape[1])
    
    add_row(start, end, color=random_color())
    add_row(color=random_color())
    
    x = round(math.sin(x), 2)
    
    if x > 0 and x < 0.5:
        add_row(color=RED)
    elif x < 0 and x > -0.5:
        add_row(color=BLUE)
    else:
        add_row(color=GREEN)
    
    # if x > 0 and x < 0.5:
    #     add_row(color=random_color())
    # elif x < 0 and x > -0.5:
    #     add_row(color=random_color())
    # else:
    #     add_row(color=random_color())
    #
print("sine")
print(sine)
#print("row stats last:")
#row_stats()
#print("row stats last 25:")
#row_stats(25)
#print("row stats all:")
#row_stats(len(app.weave)-1)

print("WEAVE SNAPSHOT:")
print(app.weave.head(10))
export_png()





