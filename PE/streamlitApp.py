import csv
import streamlit as st
import pandas as pd
import json

import os



def t2(num1, num2):
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

    with open('data.csv', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for line in reader:
            if line['Survived'] == '1' and line['Sex'] == 'female' and line['Fare'] >= num1 and line['Fare'] <= num2:
                js['sex']['female']['class'][line['Pclass']]['SurvivedCount'] += 1

            # passId = line['PassengerId']
        print(js)

    jsn = json.dumps(js)
    df = pd.read_json(jsn)
    return df



st.title("Мое первое ИИ-приложение")
st.header("Выжившие женщины по каждому классу обслуживания")
st.write("Здесь я могу выводить любой текст, данные и графики.")
# 2. Поле ввода текста
num1 = st.number_input("Диапазон платы за проезд:", 0)
num2 = st.number_input("", 1000)

if st.button('Запустить анализ'):
    with st.spinner('Анализируем данные...'):
        # Get the directory of the current script
        script_dir = os.path.dirname(__file__)
        # Construct the absolute path to your file
        file_path = os.path.join(script_dir, 'data.csv')

        try:
            a =1
            # df = pd.read_csv(file_path)
            # st.write(df)
        except FileNotFoundError:
            st.error(f"Error: File not found at {file_path}")

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

        with open(file_path, encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for line in reader:
                if line['Survived'] == '1' and line['Sex'] == 'female' and int(line['Fare']) >= num1 \
                        and int(line[
                    'Fare']) <= num2:
                    js['sex']['female']['class'][line['Pclass']]['SurvivedCount'] += 1

                # passId = line['PassengerId']
            print(js)

        jsn = json.dumps(js)
        df = pd.read_json(jsn)


        st.subheader(":")
        st.dataframe(df) # Интерактивная таблица
         # Или st.table(df) для статичной таблиц



