import pandas as pd


def clean():

    df = pd.read_csv('cars.csv')

    print(df.info())

    df = df.drop_duplicates()

    df = df.reset_index(drop=True)

    print(df.duplicated().sum())

    df.to_csv('cars_clean.csv', index=False)


df = pd.read_csv('cars_clean.csv')

print(df.head(6))
print(df.tail(9))

print(df.info())

print(df[df['Make']=='Suzuki'])


print(df.loc[69:322,:].sort_values(by = 'Distance', ascending=False).iloc[1]['Style'])

df1 = pd.read_csv('cars.csv')
print(df1)


# 1. Object
# 2. Цена
# 3. Трансмиссия (коробка)
# 4. Minivan
# 5. 9 columns ([41007 rows x 9 columns])