import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from dash.dependencies import Input, Output
import base64

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.config.suppress_callback_exceptions=True

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
], style={
    'background-color': '#e6b89c',
    'height':'1000px'
})

index_page = html.Div([
    html.H3('MENU'),
    html.Div([
        html.Hr(),
        dcc.Link('Wybierz technologię', href='/tech'),
        html.Br(),
        dcc.Link('Wyświetl logo', href='/logo'),
        html.Hr()
    ], style={'background-color': 'white'}),
    html.H6('Korzystasz z aplikacji w fazie developmentu')
], style={
    'textAlign': 'center',
    'fontSize': 28,
    'color': '#545254'
})

tab_style={
    'background-color': '#9cafb7'
}
tab_selected_style={
    'background-color': '#4281a4',
    'borderTop': '5px solid black'
}
tech_layout = html.Div([
    html.Div([
        html.H4('Wybierz technlogię z podanych poniżej:'),
        html.Hr(),
        dcc.Tabs(
            id='tech-1-tabs',
            children=[
                dcc.Tab(label='Python', value='tab-1', style=tab_style, selected_style=tab_selected_style),
                dcc.Tab(label='SQL', value='tab-2', style=tab_style, selected_style=tab_selected_style),
                dcc.Tab(label='Java', value='tab-3', style=tab_style, selected_style=tab_selected_style)
            ],
            value='tab-1'
        )
    ],style={
        'fontSize': 28,
        'textAlign': 'center'
    }),
    html.Div(id='tech-1-div'),
    html.Hr(),
    html.Div([
        dcc.Link('Wróć do MENU', href='/')
    ])
],style={
        'fontSize': 18
    })

logo_layout = html.Div([
    html.Div([
        html.H4('Wybierz technologię, aby wyświetlić logo')
    ], style={
        'fontSize': 32
    }),
    html.Hr(),
    dcc.RadioItems(
        id='logo-1-radio',
        options=[{'label': i, 'value': i} for i in ['Python', 'SQL', 'Java']]
    ),
    html.Hr(),
    html.Div(id='logo-1-div'),
    html.Hr(),
    dcc.Link('Wróć do MENU', href='/')
], style={
    'textAlign': 'center',
    'fontSize': 20,
})

@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')]
)
def display_page(pathname):
    if pathname == '/tech':
        return tech_layout
    elif pathname == '/logo':
        return logo_layout
    else:
        return index_page

@app.callback(
    Output('tech-1-div', 'children'),
    [Input('tech-1-tabs', 'value')]
)
def tech_1_tabs(value):
    if value == 'tab-1':
        return html.Div([
            dcc.Markdown(
                '''
                ```python
                def fetch_financial_data(company='AMZN'):
                """
                    This function fetch stock market quatations.
                    """
                    import pandas_datareader.data as web
                    return web.DataReader(name=company, data_source='stooq')
                ```
                '''
            )
        ])
    elif value == 'tab-2':
        return html.Div([
            dcc.Markdown('''
            ```sql
            CREATE TABLE Persons (
            PersonID int,
            LastName varchar(255),
            FirstName varchar(255),
            Address varchar(255),
            City varchar(255)
            );
            ```
            ''')
        ]),
    elif value == 'tab-3':
        return html.Div([
            dcc.Markdown('''
            ```
            // Your First Program
            
            class HelloWorld {
                public static void main(String[] args) {
                    System.out.println("Hello, World!"); 
                }
            }
            ```
            ''')
        ])

img_python = '/home/mateusz/PycharmProjects/dash_tut/07_case_studies/python-logo.png'
img_sql = '/home/mateusz/PycharmProjects/dash_tut/07_case_studies/sql-logo.png'
img_java = '/home/mateusz/PycharmProjects/dash_tut/07_case_studies/java-logo.png'

encoded_img_python = base64.b64encode(open(img_python, 'rb').read())
encoded_img_sql = base64.b64encode(open(img_sql, 'rb').read())
encoded_img_java = base64.b64encode(open(img_java, 'rb').read())

@app.callback(
    Output('logo-1-div', 'children'),
    [Input('logo-1-radio', 'value')]
)
def logo_1_radio(value):
    if value is None:
        return html.Div([
            html.H6('Wybierz jedną z opcji, aby wyświetlić logo!')
        ])
    elif value == 'Python':
        return html.Div([
            html.Img(src=f'data:image/png;base64,{encoded_img_python.decode()}',
                     style={'width': '230px'})
        ])
    elif value == 'SQL':
        return html.Div([
            html.Img(src=f'data:image/png;base64,{encoded_img_sql.decode()}',
                     style={'width': '230px'})
        ])
    elif  value == 'Java':
        return html.Div([
            html.Img(src=f'data:image/png;base64,{encoded_img_java.decode()}',
                     style={'width': '230px'})
        ])

if __name__ == '__main__':
    app.run_server(debug=True, port=8052)
