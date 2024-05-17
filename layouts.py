from dash import html, dcc
import plotly.express as px
from data import games, top_platform, games_counts, genre_sales

pie_fig = px.pie(games_counts, values='games_count', names=games_counts.index, title = 'Платформы с большим количеством игр', hole=.2)
bar_fig = px.bar(genre_sales, x=genre_sales.index, y='total_sales',title = 'Количество продаж по жанрам')
bar_fig.update_layout(xaxis ={"categoryorder":"total descending"})

general_layout = html.Div([
    html.H1(children='Games dashboard', style={'textAlign':'center'}),
    html.H4(children='Сумма продаж каждой платформы по годам', style={'textAlign':'left'}),
    dcc.Dropdown(games.platform.unique(), games.platform.unique()[0], id='dropdown0'),
    dcc.Graph(id='graph0'),
    dcc.Dropdown(games.platform.unique(), games.platform.unique()[0], id='dropdown1'),
    dcc.Graph(id='graph1'),
    dcc.Graph(figure= pie_fig),
    dcc.Graph(figure= bar_fig),
])
