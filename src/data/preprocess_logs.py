import pandas as pd

df = pd.read_csv(
    "data/raw/maintenance_logs/maintenance_logs.csv"
)

df.drop_duplicates(
    inplace=True
)

df.to_csv(
    "data/processed/maintenance_logs_cleaned.csv",
    index=False
)

print(df.shape)

print(
    "Maintenance logs saved"
)