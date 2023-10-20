import numpy as np
import pandas as pd

class App():
    weave = None
    
app = App()

def init(n_cols=400):
    columns = [str(i) for i in range(n_cols)]
    initial_row = [[np.array([0,0,0]) for i in range(len(columns))]]
    app.weave = pd.DataFrame(initial_row, columns=columns)
