import os
import pandas as pd

def get_wind_data():

    file_name = os.listdir('data')[0]
    
    wind_data = pd.read_csv(f'data/{file_name}')
    
    wind_data = wind_data.T
    wind_data.columns = wind_data.iloc[0]
    wind_data = wind_data.drop(wind_data.index[0])
    wind_data.index.name = 'Date-Time'

    return wind_data