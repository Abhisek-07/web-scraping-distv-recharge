import pandas as pd
import os
current_dir = os.path.dirname(__file__)  # Directory where utils.py is located
relative_path = os.path.join(current_dir, 'DISHSAMPLEDATA.xlsx')
f = pd.read_excel(relative_path)


print(f)