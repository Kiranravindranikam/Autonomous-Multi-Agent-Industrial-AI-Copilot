import pandas as pd

df = pd.read_csv(
    "data/raw/ai4i/ai4i2020.csv"
)

# Remove duplicates
df = df.drop_duplicates()

# Remove unnamed columns if present
df = df.loc[
    :,
    ~df.columns.str.contains("^Unnamed")
]

df.to_csv(
    "data/processed/ai4i_cleaned.csv",
    index=False
)

print(df.shape)
print("AI4I cleaned dataset saved")