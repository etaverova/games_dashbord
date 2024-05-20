import plotly.express as px
from data import games

colors =['#FFE6E6', '#FDCEDF', '#E1AFD1', '#AD88C6', '#7469B6', '#F2BED1', '#DBDFEA', '#ACB1D6', '#ACB1D6', '#8294C4', '#E5E0FF', '#8EA7E9', '#7286D3']

#Подготовка сводной таблицы для круговой диаграммы (количество игр по каждой платформе)
games_counts = games.groupby("platform").agg({"name": "nunique"})
games_counts = games_counts.rename(columns={"name": "games_count"})

#Подготовка сводной таблицы для столбчатого графика (сумма продаж по жанрам)
genre_sales = games.groupby("genre").agg({"na_sales": "sum", "eu_sales": "sum", "jp_sales": "sum", "total_sales": "sum"})

#Сумма продаж по платформам
sum_sales_of_plat = games.pivot_table(index='platform', values='total_sales', aggfunc='sum')

#Средняя оценка критиков по платформам
mean_critic_score = games.pivot_table(index='platform', values='critic_score', aggfunc='mean')

#Количество игр по платформам
count_games = games.pivot_table(index='platform', values='name', aggfunc='count')

pie_fig = px.pie(games_counts, values='games_count', names=games_counts.index, color_discrete_sequence=colors, title = 'Платформы с большим количеством игр', hole=.2)
bar_fig = px.bar(genre_sales, x = genre_sales.index, y = 'total_sales', color = genre_sales.index, color_discrete_sequence=colors, title = 'Количество продаж по жанрам')
bar_fig.update_layout(xaxis ={"categoryorder":"total descending"})
