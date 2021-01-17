import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


app.layout = html.Div([

    dcc.RadioItems(
        id='radio-1',
        options=[
            {'label': 'Polska', 'value':'Polska'},
            {'label': 'Stany Zjednoczone', 'value':'Stany Zjednoczone'}
        ],
        value='Polska'
    ),

    html.Hr(),
    dcc.RadioItems(
        id='radio-2'
    ),
    html.Hr(),
    html.Div(id='div-1')

])
@app.callback(
    Output(component_id='radio-2', component_property='options'),
    [Input(component_id='radio-1', component_property='value')]
)
def set_options(selected_country):
    if selected_country == 'Polska':
        return [{'label':'Kraków', 'value':'Kraków'},
                {'label':'Kielce', 'value':'Kielce'},
                {'label':'Warszawa', 'value':'Warszawa'}]
    elif selected_country == 'Stany Zjednoczone':
        return [{'label': 'Los Angeles', 'value':'Los Angeles'},
                {'label': 'New York', 'value':'New York'}]
    else:
        return ValueError('Niepoprawna wartość')

@app.callback(
    Output('radio-2', 'value'),
    [Input('radio-1', 'value')]
)
def set_city(selected_country):
    if selected_country == 'Polska':
        return 'Warszawa'
    elif selected_country =='Stany Zjednoczone':
        return 'New York'
    else: return ValueError('Niepoprawna wartość')


@app.callback(
    Output('div-1', 'children'),
    [Input('radio-1', 'value'),
     Input('radio-2', 'value')])
def update_div(selected1, selected2):
    return f'Wybrałeś {selected1} oraz {selected2}'

if __name__ == '__main__':
    app.run_server(debug=True)