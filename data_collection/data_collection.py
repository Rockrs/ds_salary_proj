import pickle
import pandas as pd

# Merge Data collected from all cities into a final df and load into a csv file

with open('RawData/bangalore_data', 'rb') as f1, open('RawData/hyderabad_data', 'rb') as f2, open('RawData/pune_data', 'rb') as f3, open('RawData/delhincr_data', 'rb') as f4:
    pd.concat([pickle.load(f1), pickle.load(f2), pickle.load(f3), pickle.load(f4)]).to_csv('data_science_job_result.csv', index=False)