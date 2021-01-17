import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.Div([
        dcc.Input(id='input-1', type='text', value='')
    ]),
    html.Button(id='button-1', children='Wciśnij', n_clicks=0),
    html.Div(id='div-1', children='Wprowadź tekst i naciśnij se przycisk')

])
@app.callback(
    Output('div-1', 'children'),
    [Input('input-1', 'value'),
     Input('button-1', 'n_clicks')]
)
def update_output(tresc, kliki):
    return f'Wprowadziłeś: "{tresc} " i nacisnales przycisk {kliki} razy'

if __name__ == '__main__':
    app.run_server(debug=True)