import pandas as pd
df = pd.read_csv("zerve_hackathon_dataset.csv")
print("Dtypes:\n", df.dtypes)
print("Columns:", list(df.columns))
