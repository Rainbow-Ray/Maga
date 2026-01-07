import fastapi
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from fastapi import FastAPI

app = FastAPI()

def survivedFare(df, survived, sex):
    df = df[(df['Survived'] == survived) & (df['Sex'] == sex)]
    mn =  df['Age'].min()
    mx =  df['Age'].max()

    # df = df.rename(columns={'Pclass': 'Класс', 'PassengerId': "Количество"})
    # df = df.groupby(by='Класс').count()
    # df = df['Количество']
    return [mn,mx]


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/{sex}&{isSurvived}")
async def read_item(sex: str, isSurvived: int):
    if(sex not in ['female', 'male'] or isSurvived not in [1,0,'1','0']):
        return {"Error": "Пол должен быть female или male, выжил = 1, погиб = 0"}
    else:
        df = pd.read_csv('PE/data.csv')
        ages = survivedFare(df, isSurvived, sex)
        return {"Диапазон возрастов": ages}
