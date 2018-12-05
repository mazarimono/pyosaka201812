import pandas as pd 
import numpy as np 
import dash 
import dash_core_components as dcc 
import dash_html_components as html 
import plotly.graph_objs as go 

df = pd.read_csv('kyoto_hotel_comp.csv', index_col=0)
mapbox_access_token = "pk.eyJ1IjoibWF6YXJpbW9ubyIsImEiOiJjanA5Y3NnYzYwMmJmM3BsZDRva2plYTQ0In0.vlsrPy60tmdPB0tbUmtoTQ"
app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children="Kyoto Hotel Map"),

    dcc.Graph(
        id="kyoto-hotel-graph",
        figure = {
           'data':[
               go.Scattermapbox(
                   lat = df['ido'],
                   lon = df['keido'],
                   mode = 'markers',
                   opacity= 0.6,
                   marker = dict(
                       size=9
                   ),
                   text = df['hotel_name']
               )
           ],
           'layout':
               go.Layout(
                   autosize=True,
                   hovermode='closest',
                   mapbox = dict(
                       accesstoken = mapbox_access_token,
                       bearing = 0,
                       center=dict(
                           lat = np.mean(df['ido']),
                           lon = np.mean(df['keido'])
                       ),
                       pitch = 90,
                       zoom=11
                   ),
               )
           
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)