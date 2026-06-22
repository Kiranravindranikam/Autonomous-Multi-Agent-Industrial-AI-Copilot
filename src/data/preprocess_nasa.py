import pandas as pd

columns = ["unit","cycle"]

for i in range(1,4):
    columns.append(
        f"op_setting_{i}"
    )

for i in range(1,22):
    columns.append(
        f"sensor_{i}"
    )

df = pd.read_csv(
    "data/raw/nasa_cmapss/train_FD001.txt",
    sep=r"\s+",
    header=None
)

df.columns = columns

max_cycles = df.groupby(
    "unit"
)["cycle"].max()

df["RUL"] = df.apply(
    lambda row:
    max_cycles[row["unit"]]
    - row["cycle"],
    axis=1
)

# Drop constant columns

drop_cols = [
    "sensor_1",
    "sensor_5",
    "sensor_10",
    "sensor_16",
    "sensor_18",
    "sensor_19",
    "op_setting_3"
]

df.drop(
    columns=drop_cols,
    inplace=True
)

df.to_csv(
    "data/processed/nasa_fd001_rul.csv",
    index=False
)

print(df.shape)
print("NASA dataset saved")