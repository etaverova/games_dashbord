from dash import html, dcc
#import dash_mantine_components as dmc
import dash_bootstrap_components as dbc


from data import games
from modul import pie_fig, bar_fig

'''
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
'''

general_layout = html.Div(
    [
        html.H1(children='Компьютерные игры', style={'textAlign':'center'}),
        dbc.Tabs(
            [
                dbc.Tab(label="Гистограмма", tab_id="tab-1"),
                dbc.Tab(label="Линейный график", tab_id="tab-2"),
                dbc.Tab(label="Круговая диаграмма", tab_id="tab-3"),
                dbc.Tab(label="Столбчатый график", tab_id="tab-4"),
            ],
            id="tabs",
            active_tab="tab-1",
        ),
        html.Div(id="content"),
    ]
)