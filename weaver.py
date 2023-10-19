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



# for i in range(generation_count):
#     try:
#         x = 1 / (i ** 2)
#     except Exception:
#         x = 1
#     x = int(x * 255)
    
    
#     add_row(color=np.array([x, x, x]))
    
    

    
    

    
# print("sine")
# print(sine)
# print("row stats last:")
# row_stats()
# print("row stats last 25:")
# row_stats(25)
# print("row stats all:")
# row_stats(len(app.weave)-1)







