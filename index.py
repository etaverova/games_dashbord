from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc
import plotly.graph_objects as go

from modul import pie_fig, bar_fig, colors

from app import app
from data import games
from modul import genre_sales, mean_sales_of_plat, mean_critic_score, count_games



@callback(
    Output('graph0', 'figure'),
    Input('dropdown0', 'value')
)
def update_graph(value):
    df = games[games.platform == value]

    return px.histogram(df, x='year_of_release', y='total_sales', histfunc = 'sum', title='Сумма продаж каждой платформы по годам')


@callback(
    Output('graph1', 'figure'),
    Input('dropdown1', 'value')
)
def update_graph(value):
    df = games[games.platform == value].groupby(['year_of_release']).agg({'name': 'count'})
    df = df.rename(columns={'name': 'count_of_games'})
    return px.line(df, x=df.index, y='count_of_games', title='Изменение количества проданных игр по каждой платформе с течением времени')

@callback(
    Output('graph2', 'figure'),
    Input('dropdown2', 'value')
)
def update_graph(value):
    df = genre_sales
    bar_fig = px.bar(genre_sales, x = genre_sales.index, y = value, color = genre_sales.index, color_discrete_sequence=colors, title = 'Количество продаж по жанрам')
    bar_fig.update_layout(xaxis ={"categoryorder":"total descending"})


    return bar_fig


@callback(
    Output('ind1', 'figure'),
    Input('dropdown0', 'value')
)
def update_graph(value):
    fig = go.Figure(go.Indicator(
            mode = "number+delta",
            value = mean_sales_of_plat.loc[value, 'total_sales'],
            delta = {"reference": mean_sales_of_plat['total_sales'].max(), "valueformat": ".0f"},
            #title = {"text": "Users online"},
            #domain = {'y': [0, 1], 'x': [0.25, 0.75]})
            ))
    fig.update_layout(
        paper_bgcolor="lightgray",
        height=200,  # Added parameter
    )
    return fig

@callback(
    Output('ind2', 'figure'),
    Input('dropdown0', 'value')
)
def update_graph(value):
    fig = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = mean_critic_score.loc[value, 'critic_score'],
    #title = {'text': "Speed"},
    domain = {'x': [0, 1], 'y': [0, 1]}
        ))

    fig.update_layout(
        paper_bgcolor="lightgray",
        height=200,  # Added parameter
    )
    return fig


@callback(
    Output('ind3', 'figure'),
    Input('dropdown1', 'value')
)
def update_graph(value):
    fig = go.Figure(go.Indicator(
            mode = "number+delta",
            value = count_games.loc[value, 'name'],
            delta = {"reference": count_games['name'].max(), "valueformat": ".0f"},
            #title = {"text": "Users online"},
            #domain = {'y': [0, 1], 'x': [0.25, 0.75]})
            ))
    fig.update_layout(
        paper_bgcolor="lightgray",
        height=200,  # Added parameter
    )
    return fig


@app.callback(Output("content", "children"), [Input("tabs", "active_tab")])
def switch_tab(at):
    if at == "tab-1":
        return [
                dcc.Dropdown(games.platform.unique(), games.platform.unique()[0], id='dropdown0'),
                dbc.Card(
                    dbc.CardBody(
                        [
                            html.H6("Card subtitle", className="card-subtitle"),
                            dcc.Graph(id='ind1'),
                        ]
                    ),
                    style={"width": "18rem"},
                ),
                dbc.Card(
                    dbc.CardBody(
                        [
                            html.H6("Card subtitle", className="card-subtitle"),
                            dcc.Graph(id='ind2'),
                        ]
                    ),
                    style={"width": "18rem"},
                ),
                dcc.Graph(id='graph0'),
                ]
    elif at == "tab-2":
        return  [dcc.Dropdown(games.platform.unique(), games.platform.unique()[0], id='dropdown1'),
                dbc.Card(
                    dbc.CardBody(
                        [
                            html.H6("Card subtitle", className="card-subtitle"),
                            dcc.Graph(id='ind3'),
                        ]
                    ),
                    style={"width": "18rem"},
                ),
                dcc.Graph(id='graph1')]
    elif at == "tab-3":
        return  [
                dcc.Graph(figure= pie_fig)
            ]
    elif at == "tab-4":
        return  [dbc.RadioItems(
            id="dropdown2",
            options=[
                {"label": "Все продажи", "value": "total_sales"},
                {"label": "Продажи в Северной Америке", "value": "na_sales"},
                {"label": "Продажи в Европе", "value": "eu_sales"},
                {"label": "Продажи в Японии", "value": "jp_sales"},
            ],
            value="total_sales",
            inline=True,
        ), dcc.Graph(id='graph2')]
        





if __name__ == '__main__':
    app.run(debug=True)