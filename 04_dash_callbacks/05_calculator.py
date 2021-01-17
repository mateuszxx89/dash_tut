import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Input(id='input-1', value=1, type='number'),
    dcc.Input(id='input-2', value=1, type='number'),

    html.Table([
        html.Tr([html.Td(['x + y']), html.Td(id='tr-1')]),
        html.Tr([html.Td(['x - y']), html.Td(id='tr-2')]),
        html.Tr([html.Td(['x * y']), html.Td(id='tr-3')]),
        html.Tr([html.Td(['x / y']), html.Td(id='tr-4')]),
        html.Tr([html.Td(['x // y']), html.Td(id='tr-5')])
    ])
])

@app.callback(
    [Output('tr-1', 'children'),
     Output('tr-2', 'children'),
     Output('tr-3', 'children'),
     Output('tr-4', 'children'),
     Output('tr-5', 'children')],
    [Input('input-1', 'value'),
     Input('input-2', 'value')]
)
def update_table(x, y):
    if y==0:
        return x+y, x-y, x*y, 'nie dziel przez zero', 'nie dziel przez zero'
    return x+y, x-y, x*y, x/y, x//y

if __name__ == '__main__':
    app.run_server(debug=True)