import csv
import streamlit as st

st.title("Мое первое ИИ-приложение")
st.header("Раздел для анализа данных")
st.write("Здесь я могу выводить любой текст, данные и графики.")
# 2. Поле ввода текста
user_name = st.text_input("Введите ваше имя:", "Алексей")
st.write(f"Привет, {user_name}!")
# 3. Слайдер (числовой)
age = st.slider("Ваш возраст:", min_value=0, max_value=100, value=25)
st.write(f"Вам {age} лет.")
# 4. Переключатели (radio buttons)
model_type = st.radio(
 "Выберите модель для анализа:",
 ('Линейная регрессия', 'Случайный лес', 'Нейронная сеть')
)
st.write(f"Выбрана модель: {model_type}")
# 5. Выпадающий список (selectbox)
dataset = st.selectbox(
 "Выберите датасет:",
 ('Iris', 'Titanic', 'Boston Housing')
)

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
