import math
import numpy as np
import random

#import pandas as pd
from utils import add_row, row_stats, export_png, random_color
from init import app, init
from patterns import patterns_list

columns_size = 400
generation_count = 500

def generate(row_count = generation_count):  
    pattern_length = 100
    
    for i in range(500):
        pattern = random.choice(patterns_list)
        pattern(random.randint(1, 3))
    
    #for pattern in patterns_list:
    #    pattern(pattern_length)
    #pattern = patterns_list[0]
    #pattern(100)

init(columns_size)
generate()
print("WEAVE SNAPSHOT:")
print(app.weave.head(10))
export_png()
