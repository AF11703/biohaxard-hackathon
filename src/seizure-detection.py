# %%

from dotenv import load_dotenv
from pathlib import Path
import os
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 

base_path = Path(os.getenv('BASE_PATH'))

data_files = list(base_path.glob("*/data.csv"))

if data_files:
    data_csv = data_files[0]
    print(f"Found file: {data_csv}")
else:
    print("No matching file found")


pd_csv = pd.read_csv(data_csv)
headset_df = pd.DataFrame(pd_csv)



#for i in range(5,10):
 #   trace = headset_df[headset_df.columns[i]]
    #plt.plot(range(len(trace)),trace,label = f"{headset_df.columns[i]} traces")


theta = headset_df['theta']
lowAlpha = headset_df['lowAlpha']
highAlpha = headset_df['highAlpha']
lowBeta = headset_df['lowBeta']
highBeta = headset_df['highBeta']


wave_sums = theta + lowAlpha + highAlpha + lowBeta + highBeta

normalized = (wave_sums - wave_sums.min()) / (wave_sums.max() - wave_sums.min())
        
plt.plot(normalized, label='EEG Data')    
    

plt.legend()
