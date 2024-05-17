import pandas as pd


games = pd.read_csv('data/games.csv')

#приведем название столбцов к одному регистру
games.columns = games.columns.str.lower()

#Изменим некоторые типы данных для удобства работы
games['year_of_release'] = games['year_of_release'].astype('Int64')
games['critic_score'] = games['critic_score'].astype('Int64')
games['user_score'] = games['user_score'].astype('float32', errors='ignore')
games['critic_score'] = games['critic_score'].fillna(0)

#Добавим столбец total_sales, который будет отражать общие продажи
games['total_sales'] = games['na_sales'] + games['eu_sales'] + games['jp_sales'] + games['other_sales']

#Подготовка сводной таблицы для круговой диаграммы (количество игр по каждой платформе)
games_counts = games.groupby("platform").agg({"name": "nunique"})
games_counts = games_counts.rename(columns={"name": "games_count"})

#Подготовка сводной таблицы для столбчатого графика (сумма продаж по жанрам)
genre_sales = games.groupby("genre").agg({"total_sales": "sum"})

#Cредние продажи по платформам
mean_sales_of_plat = (games.groupby(["platform"]).agg({"total_sales": "mean"}).reset_index())

#Топ самых продаваемых и популярных платформ
top_platform = games.pivot_table(index='platform', values='total_sales', aggfunc='sum').sort_values(by='total_sales', ascending=False).reset_index()['platform'].head(5)

#Средняя оценка критиков по платформам
mean_critic_score = (games.groupby(["platform"]).agg({"critic_score": "mean"}).reset_index())