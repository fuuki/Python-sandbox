import pandas as pd
from io import StringIO

#%%
test_data = StringIO(
"""col1,col2,col3
1,4.4,99
2,4.5,200
3,4.7,65
4,3.2,140
""")
df = pd.read_csv(test_data, sep=",")
print(df)
print()

csv = df.to_csv(index = False)
print(csv)

# %%
