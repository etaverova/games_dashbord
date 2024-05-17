from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

from app import app
from data import games

@callback(
    Output('graph0', 'figure'),
    Input('dropdown0', 'value')
)
def update_graph(value):
    df = games[games.platform == value]

    return px.histogram(df, x='year_of_release', y='total_sales', histfunc = 'sum')


@callback(
    Output('graph1', 'figure'),
    Input('dropdown1', 'value')
)
def update_graph(value):
    df = games[games.platform == value].groupby(['year_of_release']).agg({'name': 'count'})
    df = df.rename(columns={'name': 'count_of_games'})
    return px.line(df, x=df.index, y='count_of_games', title='Изменение количества проданных игр по каждой платформе с течением времени')



if __name__ == '__main__':
    app.run(debug=True)