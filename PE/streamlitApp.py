import streamlit as st
import pandas as pd

import os


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


def streamlit():
    st.image(
        "https://hi-news.ru/wp-content/uploads/2020/09/titanic_fail_image_one-750x460.jpg"
    )
    st.title("Данные пассажиров Титаника")
    st.header("Выжившие женщины по каждому классу обслуживания")

    num1 = st.number_input("Диапазон платы за проезд:", 0)
    num2 = st.number_input("", 0)

    if st.button("Запустить анализ"):
        script_dir = os.path.dirname(__file__)
        file_path = os.path.join(script_dir, "data.csv")

        df = pd.read_csv(file_path)
        df = survivedFare(df, num1, num2)
        st.subheader("Количество выживших женщин по классу:")
        st.dataframe(df)  # Интерактивная таблица
        # Или st.table(df) для статичной таблиц


streamlit()
