import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
matplotlib.use('TkAgg')
sns.set()


def columns_describe(cat_col, num_col):
    print("Категориальные данные:", cat_col)
    print("\t Количество столбцов:", len(cat_col))
    print("Числовые данные:", num_col)
    print("\t Количество столбцов:", len(num_col))
    print(df.describe())

def data_plots(df, num_col):
    width = 2
    height = int(np.ceil(len(num_col)/width))
    fig, ax = plt.subplots(nrows=height, ncols=width, figsize=(12,7))

    for idx, column_name in enumerate(num_col):
        plt.subplot(height,width, idx+1)
        sns.histplot(data=df,
                x=column_name, bins = 20)
    plt.show()


def price_distance_plots(df):
    plt.figure(figsize=(14,5))
    sns.histplot(data=df,
            x='Price(euro)', bins = 20, log_scale=True)


def distance_plot(df):
    plt.figure(figsize=(14,5))
    sns.histplot(data=df,
            x='Distance', bins = 20, log_scale = True)
    plt.show()


def data_cleanse(df):
    quest_dist = df[df.Distance == 0]
    df = df.drop(quest_dist.index)

    question_dist = df[(df.Year < 2021) & (df.Distance < 1001)]
    df = df.drop(question_dist.index)

    question_dist = df[(df.Distance > 1e6)]
    df = df.drop(question_dist.index)

    question_engine = df[df["Engine_capacity(cm3)"] < 200]
    df = df.drop(question_engine.index)

    question_engine = df[df["Engine_capacity(cm3)"] > 5000]
    df = df.drop(question_engine.index)

    question_price = df[df["Price(euro)"] < 101]
    df = df.drop(question_price.index)

    question_price = df[df["Price(euro)"] > 1e5]
    df = df.drop(question_price.index)

    question_year = df[df.Year < 1971]
    df = df.drop(question_year.index)

    df = df.reset_index(drop=True)
    print(df.tail())
    return df


def depence_plot(df):
    sns.pairplot(data=df, hue='Transmission')
    plt.show()

def add_km_year(df):
    df['km_year'] =  df.Distance / (2022 - df.Year)
    question_km_year = df[df.km_year > 50e3]
    df = df.drop(question_km_year.index)
    question_km_year = df[df.km_year < 100]
    df = df.drop(question_km_year.index)
    return df

def km_year_plot(df):
    plt.figure(figsize=(10,7))
    sns.histplot(data=df,
                x='km_year', bins = 20)

    plt.figure(figsize=(10, 7))
    sns.scatterplot(
        data=df,
        x="km_year", y="Distance",
        hue="Transmission",
        size="Price(euro)", alpha=0.7
    )

    plt.figure(figsize=(10, 7))
    sns.scatterplot(
        data=df,
        x="km_year", y="Year",
        hue="Transmission",
        size="Price(euro)", alpha=0.7
    )

    plt.show()


def num_anomaly(num_columns):
    fig, ax = plt.subplots(nrows=3, ncols=2, figsize=(14, 8))

    for idx, column_name in enumerate(num_columns):
        plt.subplot(3, 2, idx + 1)

        sns.boxplot(data=df,
                    x=column_name)

    fig.tight_layout()

    fig, ax = plt.subplots(nrows=3, ncols=2, figsize=(14, 8))

    for idx, column_name in enumerate(num_columns):
        plt.subplot(3, 2, idx + 1)

        sns.kdeplot(data=df,
                    x=column_name)

    fig.tight_layout()

    plt.show()

def corr_plot(df, num):
    cm = sns.color_palette("vlag", as_cmap=True)

    # df.corr().style.background_gradient(cmap=cm, vmin=-1, vmax=1)

    plt.figure(figsize=(14,7))
    plt.subplot()
    sns.heatmap(df[num].corr(), annot=True, cmap='coolwarm', vmin=-1, vmax=1)

    plt.show()

def clean_rare(df, cat_col):
    print(df[cat_col].nunique())
    make_count = df.Make.value_counts()
    print(make_count)
    print(make_count.median())

    rare = make_count[make_count<25]
    print(rare)
    print([rare.index.values])
    df['Make'] = df['Make'].replace(rare.index.values, 'Rare')

    make_count = df.Make.value_counts()
    print(make_count)

    model  = df.Model.value_counts()
    print(df.Model.value_counts())
    print(df.Model.value_counts().median())
    print(model[model<50])
    rare = model[model<50]

    df['Model'] = df['Model'].replace(rare.index.values, 'Rare')
    make_count = df.Model.value_counts()
    print(make_count)


def cleaning_data():
    df = pd.read_csv('cars_clean.csv')
    cat_col = []
    num_col = []

    for column in df.columns:
        if df[column].dtype == object:
            cat_col += [column]
        else:
            num_col += [column]

    # data_plots(df, num_col)

    df = data_cleanse(df)

    # data_plots(df, num_col)

    df = add_km_year(df)

    num_col.append('km_year')

    # num_anomaly(num_col)

    # sns.kdeplot(data=df, x="total_bill")

    # corr_plot(df, num_col)

    clean_rare(df, cat_col)

    df.to_csv('cars_cleanest.csv', index=False)

def binary_to_num(df):
    df['Transmission'] = df['Transmission'].map({'Automatic': 1, 'Manual': 0})

def cat_to_numCAT(df, cat_columns):
    df_se = df.copy()
    df_se[cat_columns] = df_se[cat_columns].astype('category')

    for _, column_name in enumerate(cat_columns):
        df_se[column_name] = df_se[column_name].cat.codes
    df_se.info()
    print(df_se.head())
    print(df_se.info())
    df_se.to_csv('cars_cat.csv')


def cat_to_numONEHOT(df):
    df_se = df.copy()
    df_se = pd.get_dummies(df_se)
    print(df_se.head())
    print(df_se.info())
    df_se.to_csv('cars_one_hot.csv')

def column_count(df):
    cat_col = []
    num_col = []

    for column in df.columns:
        if df[column].dtype == object:
            cat_col += [column]
        else:
            num_col += [column]

    return cat_col, num_col




df = pd.read_csv('cars_cleanest.csv')
binary_to_num(df)
cat_col, num_col = column_count(df)

cat_to_numCAT(df, cat_col)

# df = pd.read_csv('cars_clean.csv')
# cat_col, num_col = column_count(df)
# columns_describe(cat_col, num_col)
# df = data_cleanse(df)
# df = add_km_year(df)
# clean_rare(df, cat_col)
#
# binary_to_num(df)
# add_km_year(df)
# cat_to_numCAT(df, cat_col)
# cat_to_numONEHOT(df)
#
