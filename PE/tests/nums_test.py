import pytest
import pandas as pd


def survivedFare(df, num1, num2):
    df = df[
        (df["Survived"] == 1)
        & (df["Sex"] == "female")
        & (df["Fare"] >= num1)
        & (df["Fare"] <= num2)
    ]
    df = df.rename(columns={"Pclass": "Класс", "PassengerId": "Количество"})
    df = df.groupby(by="Класс").count()
    df = df["Количество"]
    return df


header = ["PassengerId", "Survived", "Pclass", "Sex", "Fare"]
none = survivedFare(
    pd.DataFrame(columns=["PassengerId", "Survived", "Pclass", "Sex", "Fare"]), 0, 0
)


def test_num():
    data = [
        [0, 1, 1, "female", 800],
        [1, 1, 1, "female", 500],
        [2, 1, 2, "female", 100],
        [3, 1, 2, "female", 200],
        [4, 1, 3, "female", 50],
        [5, 1, 3, "female", 20],
        [6, 0, 2, "female", 100],
        [7, 1, 3, "male", 20],
        [8, 0, 1, "female", 600],
    ]
    num1 = [-10, -5, 0, 0, 10, 100, 10, 0]
    num2 = [-10, 0, 0, 500, 5, 500, 20, 1000]
    itog = [
        none,
        none,
        none,
        pd.Series([1, 2, 2], index=[1, 2, 3], name="Количество"),
        none,
        pd.Series([1, 2], index=[1, 2], name="Количество"),
        pd.Series([1], index=[3], name="Количество"),
        pd.Series([2, 2, 2], index=[1, 2, 3], name="Количество"),
    ]
    df = pd.DataFrame(data, columns=header)

    for i in range(len(num1)):
        assert (survivedFare(df, num1[i], num2[i]) == itog[i]).all()


def test_strange_data():
    data = [
        [2, 1, 3, "female", 100],
        [3, 1, 2, "female", 87.5],
        [3, 1, 2, "female", -87.5],
        [0, 1, 10, "aaaaaa", 10],
        [1, 0, 5, "female", -10],
        [4, 20, 3, "aaaa", 50],
    ]
    itog = pd.Series([1, 1], index=[2, 3], name="Количество")
    df = pd.DataFrame(data, columns=header)

    assert (survivedFare(df, 0, 1000) == itog).all()


def test_no_data():
    data = []
    df = pd.DataFrame(data, columns=header)

    assert (survivedFare(df, 0, 1000) == none).all()
