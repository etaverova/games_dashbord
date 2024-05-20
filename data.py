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