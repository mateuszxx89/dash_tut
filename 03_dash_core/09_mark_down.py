import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

markdown="""
Naglowki
# H1
## H2
### H3
#### H4
##### H5

Znaczniki tekstu:  
Kursywa: *tekst napisany kursywa* lub _drugi tekst kursywa_  
Pogrubienie: **a tu mamy gruby tekst** lub __dwa podresliniki i jest to samo__  
kursywa i pogrubienie  **pogrubienie i _kursywa_**  
przekreslenie ~~Przekreslenie z 2 tyldami~~  
  
Listy:  
Lista uporzadkowana:  
1.Python  
2.SQL  
3. Java  
Lista nieuporzadkowana:  
* Python  
* SQL  
* Java  
  
Linkowanie:  
[Google.com](http://www.google.com)
  
Kod:  
# Uzyj `print ('Hello World')`  
### Blok kodu  
```
import numpy as np

x=np.random.rand(100)
print(x)
```

Tabele:  

 |UserID     |Rating     |Age|
 |-----------|-----------|---|
 |001        |4.5        |23 |
 |002        |3.3        |24 |

Cytowanie:  
> Python jest wenszem

LInie horyzntalne  
---  
***  
"""

app.layout = html.Div([
    dcc.Markdown(markdown)
])

if __name__ == '__main__':
    app.run_server(debug=True)