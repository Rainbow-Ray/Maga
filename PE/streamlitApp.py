import csv
import streamlit as st

st.title("Мое первое ИИ-приложение")
st.header("Выжившие женщины по каждому классу обслуживания")
st.write("Здесь я могу выводить любой текст, данные и графики.")
# 2. Поле ввода текста
num1 = st.number_input("Диапазон платы за проезд:", "0")
num2 = st.number_input("", "1000")

def t2():
    js = {
        'sex': {
            'female': {
                'class': {
                    '1': {
                        'SurvivedCount': 0
                    },
                    '2': {
                        'SurvivedCount': 0
                    },
                    '3': {
                        'SurvivedCount': 0
                    },

                }
            },
        }
    }



    with open('../EngData/data.csv', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for line in reader:
            if line['Survived'] == '1' and line['Sex'] == 'female':
                js['sex']['female']['class'][line['Pclass']]['SurvivedCount'] += 1

            # passId = line['PassengerId']
        print(js)
