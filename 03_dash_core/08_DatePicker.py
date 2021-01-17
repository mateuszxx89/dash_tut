import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from datetime import datetime as dt

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.DatePickerSingle(
        date=dt(2019,1,1),
        display_format='YYYY-MM-DD'
    ),
    html.Br(),
    dcc.DatePickerSingle(
        date=dt(2019, 1, 1),
        display_format='DD-MM-YYYY'
    ),
    html.Br(),
    dcc.DatePickerRange(
        start_date=dt(2019, 1, 7),
        display_format='YYYY-MM-DD',
        end_date=dt(2019,3,28)
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)