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

def create_subweave():
    columns = app.weave.columns.tolist()
    df = pd.DataFrame(columns=columns)
    return df

def merge_subweave(df):
    app.weave = pd.concat([app.weave, df], ignore_index=True)

# def add_row(starts=np.array([0]), lengths=np.array([0]), colors=[np.array([0, 0, 0])]):

#     new_row = [np.array([0, 0, 0]) for i in range(app.weave.shape[1])]   
#     ends = starts + lengths
#     for i in range(len(starts)):
#         if ends[i] == 0:
#             ends[i] = app.weave.shape[1]
#         if ends[i] < starts[i]:
#             raise ValueError("end can't be smaller than start")
#         if ends[i] > app.weave.shape[1]:
#             raise ValueError("end cant be larger than weave")
        
#         new_row[starts[i]:ends[i]] = [colors[i] for k in range(ends[i]-starts[i])]

#     app.weave.loc[len(app.weave)] = new_row

def add_row(starts=np.array([0]), ends=np.array([0]), colors=[np.array([0, 0, 0])], df=None):
    if df.empty:
        df = app.weave
    
    if len(starts) != len(ends):
        raise ValueError("Starts and ends need to be the same length.")
    if len(colors) != len(starts):
        raise ValueError("Colors need to be same lengths as starts and ends.")
    
    new_row = [np.array([0, 0, 0]) for i in range(df.shape[1])]   
    
    for i in range(len(starts)):
        if ends[i] == 0:
            ends[i] = df.shape[1]
        if ends[i] < starts[i]:
            raise ValueError("end can't be smaller than start")
        if ends[i] > df.shape[1]:
            raise ValueError("end cant be larger than weave")
        
        new_row[starts[i]:ends[i]] = [colors[i] for j in range(ends[i]-starts[i])]

    df.loc[len(df)] = new_row
    
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
    print("Image saved with filename: " + filename)

def export_weave(df, filename="weave_raw"):
    df.to_csv(filename + ".csv")
    print("Weave saved with filename: " + filename)