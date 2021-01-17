import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from dash.dependencies import Input, Output
import dash_table

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = dash_table.DataTable(
    columns=[
        {'name':'UserID', 'id':'UserID'},
        {'name':'Rating', 'id':'Rating'},
        {'name':'Age', 'id':'Age'}
    ],
    data=[
        {'UserID': '001', 'Rating': '4.5', 'Age': '24'},
        {'UserID': '002', 'Rating': '3', 'Age': '34'},
        {'UserID': '003', 'Rating': '5', 'Age': '29'},
        {'UserID': '004', 'Rating': '4', 'Age': '29'}
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)