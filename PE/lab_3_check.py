from lab_3 import survivedFare
import pandas as pd

file_path = 'data.csv'
num1 = 1
num2 = 500
df = pd.read_csv(file_path)
df = survivedFare(df, num1, num2)
print(df)