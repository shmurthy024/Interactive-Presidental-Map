import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly as py
import plotly.express as px
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import pandas as pd
import csv

f = open('1976-2016-president.csv')
csvf = csv.reader(f)

app = dash.Dash()

df = pd.read_csv('1976-2016-president.csv')


app.layout = html.Div([
    html.H1("Presidential Elections 1976-2016", style={'text-align': 'center'}),

    dcc.Dropdown(id='slect-year',
                 options=[
                     {'label': '1976', 'value': 1976},
                     {'label': '1980', 'value': 1980},
                     {'label': '1984', 'value': 1984},
                     {'label': '1988', 'value': 1988},
                     {'label': '1992', 'value': 1992},
                     {'label': '1996', 'value': 1996},
                     {'label': '2000', 'value': 2000},
                     {'label': '2004', 'value': 2004},
                     {'label': '2008', 'value': 2008},
                     {'label': '2012', 'value': 2012},
                     {'label': '2016', 'value': 2016}],
                 multi=False,
                 value=1976,
                 style={'width': '40%'}
                 ),
    html.Div(id='output-container', children=[]),
    html.Br(),

    dcc.Graph(id='election_map', figure={})
])


@app.callback(
    [Output(component_id='output-container', component_property='children'),
     Output(component_id='election_map', component_property='figure')],
    [Input(component_id='slect-year', component_property='value')]
)
def update_graph(option_slctd):
    print(option_slctd)
    print(type(option_slctd))

    candidate = ''
    if option_slctd == 1976:
        candidate += 'Jimmy Carter'
    elif option_slctd == 1980:
        candidate += 'Ronald Reagan'
    elif option_slctd == 1984:
        candidate += 'Ronald Reagan'
    elif option_slctd == 1988:
        candidate += 'George H.W Bush'
    elif option_slctd == 1992:
        candidate += 'Bill Clinton'
    elif option_slctd == 1996:
        candidate += 'Bill Clinton'
    elif option_slctd == 2000:
        candidate += 'George W. Bush'
    elif option_slctd == 2004:
        candidate += 'George W. Bush'
    elif option_slctd == 2008:
        candidate += 'Barack Obama'
    elif option_slctd == 2012:
        candidate += 'Barack Obama'
    elif option_slctd == 2016:
        candidate += 'Donald Trump'

    winner = 'The winner was '
    winner += candidate
    container = 'The year chosen was {}. '.format(option_slctd)
    container += winner
    print(winner)
    dff = df.copy()
    dff = dff[dff['year'] == option_slctd]

    # Px
    fig = px.choropleth(
        data_frame=dff,
        locationmode='USA-states',
        locations='state_po',
        scope='usa',
        color='totalvotes',
        hover_data=['candidate', 'candidatevotes'],
        color_continuous_scale=px.colors.qualitative.D3,
        labels={'candiate': 'candiatevotes'},
        template='plotly_dark'
    )

    return container, fig


if __name__ == '__main__':
    app.run_server(debug=True)
