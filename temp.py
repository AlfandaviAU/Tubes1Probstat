import pandas as pd

# Read filenya
df = pd.read_csv ("Gandum.csv")

print(df)
print(df["Daerah"].mean())