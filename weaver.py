import numpy as np
import pandas as pd
from PIL import Image

weave = None
RED = np.array([255, 0, 0])
GREEN = np.array([0, 255, 0])
BLUE = np.array([0, 0, 255])

def export_png(df, filename="output"):
    # Convert the DataFrame to a list of lists
    image_data = weave.values.tolist() #weave.to_numpy()
    # Convert the list of lists to a NumPy array
    image_array = np.array(image_data)
    # Convert the list of lists to a NumPy array
    image_array = image_array.astype('uint8')
    # Create an image using Pillow (PIL)
    image = Image.fromarray(image_array)
    # Save the image to a PNG file
    image.save("output" + ".png")
    print("Image saved")

def export_weave(filename="weave_raw"):
    pass

def add_row(start=0, end=0, color=None):
    if end == 0:
        end = weave.shape[1]
    new_row = [np.array([0, 0, 0]) for i in range(weave.shape[1])]
    new_row[start:end] = [color for i in range(end)]

    weave.loc[len(weave)] = new_row
    
def init(n_cols=400):
    global weave
    columns = [str(i) for i in range(n_cols)]
    initial_row = [[np.array([0,0,0]) for i in range(len(columns))]]
    weave = pd.DataFrame(initial_row, columns=columns)
        
init()
#add_row(color=RED)
array = np.arange(1, weave.shape[1])
sine = np.sin(array)

for x in sine:
 if x < 0:
    add_row(color=RED)
 elif x > 0:
    add_row(color=BLUE)
 


print(sine)

export_png(weave)

print(weave.head(10))




#print(image_array.mean())
#flat = image_array.flatten()
#flat.mean()

