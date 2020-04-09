import pandas as pd
import numpy as np

data = pd.read_csv('relate21a_3times_continuously.csv')
print(data.shape)
result = data.dropna(subset=['n_2', 'n_3'])
result.to_csv('a.csv', index=False)
print(result.shape)
print('done')