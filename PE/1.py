import pandas as pd

df = pd.read_csv('data.csv')
df = df[df['Sex'] == 'female']
df = df[df['Fare'] >= 0]
df = df[df['Fare'] <= 1000]
df = df[df['Survived'] == 1]
df = df.groupby(by='Pclass').count()
df = df['PassengerId']
# df = df.rename(columns={'PassengerId': 'Количество'})
print(df.head())
