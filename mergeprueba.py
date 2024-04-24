import numpy as np 
import pandas as pd 

np.random.seed(1)
left_df = pd.DataFrame({'join_keys': ['a', 'b', 'c', 'd'], 'values': np.random.randint(10, 99, 4)})
right_df = pd.DataFrame({'join_keys': ['b', 'd', 'e', 'f'], 'values': np.random.randint(10, 99, 4)})
#print(left_df)
#print(right_df)

inner_join = left_df.merge(right=right_df, how='inner', on='join_keys')
print(inner_join)

left_join = left_df.merge(right=right_df, how='left', on='join_keys')
print(left_join)

right_join = left_df.merge(right=right_df, how='right', on='join_keys')
print(right_join)

outer_join = left_df.merge(right=right_df, how='outer', on='join_keys',indicator=True)
print(outer_join)
