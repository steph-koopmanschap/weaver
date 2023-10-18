import random
from init import app
from PIL import Image
import numpy as np
import pandas as pd
from statistics import mode
from functions import function_list

def choose_function():
    selected_function = random.choice(function_list)
    
def random_color():
    return np.random.randint(0, 256, 3)

# Returns statistics of rows
# The offset is the number of rows minus the current row
def row_stats(offset=0):    
    # Calculate row stats for the last row
    if offset == 0:
        selected_rows = app.weave.iloc[-1].values
        selected_rows = np.concatenate(selected_rows)
    # Calculate row stats for multiple rows
    else:
        selected_rows = app.weave.iloc[(-1)-offset:-1].values
        selected_rows = np.concatenate(selected_rows)
        selected_rows = np.concatenate(selected_rows)

    # Calculate mean, median, mode, and variance
    mean_value = np.mean(selected_rows)
    median_value = np.median(selected_rows)
    mode_value = mode(selected_rows)
    variance_value = np.var(selected_rows)

    return [mean_value, median_value, mode_value, variance_value]

def normalize_color(color):
    return color / 255

def denormalize_color(color):
    return color * 255

def add_row(start=0, end=0, color=np.array([0, 0, 0])):
    if end == 0:
        end = app.weave.shape[1]
    new_row = [np.array([0, 0, 0]) for i in range(app.weave.shape[1])]    
    new_row[start:end] = [color for i in range(end-start)]

    app.weave.loc[len(app.weave)] = new_row
    
def export_png(filename="output"):
    # Convert the DataFrame to a list of lists
    image_data = app.weave.values.tolist() #weave.to_numpy()
    # Convert the list of lists to a NumPy array
    image_array = np.array(image_data)
    # Convert the list of lists to a NumPy array
    image_array = image_array.astype('uint8')
    # Create an image using Pillow (PIL)
    image = Image.fromarray(image_array)
    # Save the image to a PNG file
    image.save("output/" + filename + ".png")
    print("Image saved")

def export_weave(filename="weave_raw"):
    pass