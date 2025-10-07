import csv
import streamlit as st


# 1. Заголовки и текст
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
# 6. Кнопка
if st.button('Запустить анализ'):
 # Эта часть кода выполнится только при нажатии кнопки
 with st.spinner('Анализируем данные...'):
 # Имитация долгой работы (например, инференс модели)
 import time
 time.sleep(2)
 st.success('Анализ завершен!')
 # 7. Генерация и отображение таблицы с данными
 data = np.random.randn(5, 3)
 df = pd.DataFrame(data, columns=[f'Колонка {i}' for i in range(1, 4)])
 st.subheader("Сгенерированные данные:")
 st.dataframe(df) # Интерактивная таблица
 # Или st.table(df) для статичной таблицы
# Боковая панель (Sidebar)
with st.sidebar:
 st.header("Настройки")
 confidence = st.slider("Порог уверенности модели:", 0.0, 1.0, 0.8)
 st.info(f"Порог уверенности: {confidence}")
Запуск приложения:
streamlit streamlit_app.py

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
