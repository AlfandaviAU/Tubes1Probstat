import pandas as pd

# Read filenya
df = pd.read_csv (r'Gandum.csv')
print(len(df))
print (df)


def describe(df):
    print( pd.concat([df.describe().T,
                      df.var().rename('variansi'),
                      df.median().rename('median'),
                      df.skew().rename('skewness'),
                      df.kurt().rename('kurtosis'),
                     ], axis=1).T)
    print("\nDATA MODUS ")
    print(df.mode())

    print("\nDATA RANGE ")
    minimum = df.min()
    maksimum = df.max()
    print(maksimum-minimum)

    print("\nDATA IQR ")
    Q1 = df.quantile(0.25)
    Q3 = df.quantile(0.75)
    IQR = Q3 - Q1
    print(IQR)
    

describe(df)
df[["Daerah"]].plot(kind="hist",bins=[0,10,20,30,40,50,60,70,80,90,100],rwidth=0.95, color='red')