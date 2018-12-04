import dash
import dash_core_components as dcc 
import dash_html_components as html 
import plotly.graph_objs as go 
import pandas as pd
import numpy as np  

df = pd.read_csv('kyoto_hotel_comp.csv', index_col=0)
lat1 = list()
lon1 = list()
hotel_name = list()

for i in range(len(df)):
    lat1.append(df.iloc[i, 6])
    lon1.append(df.iloc[i, 7])
    hotel_name.append(df.iloc[i, 0])

lat2 = np.mean(lat1)
lon2 = np.mean(lon1)

mapbox_access_token="pk.eyJ1IjoibWF6YXJpbW9ubyIsImEiOiJjam95OGhvaHMyOWJmM3NucjYzNDA1dnFkIn0.XuJiO6JqXfkof_RuTtdRZw"

app = dash.Dash(__name__)

app.layout = html.Div(children=[
        html.Div(children='Kyoto Hotel Map'),

        dcc.Graph(
            id='kyoto-map',
            figure={
                'data':[
                    go.Scattermapbox(
                        lat = lat1,
                        lon = lon1,
                        mode = 'markers',
                        marker=dict(
                            size=14
                        ),
                        text = hotel_name
                    )
                ],
                'layout':[
                    go.Layout(
                        autosize=True,
                        hovermode='closest',
                        mapbox=dict(
                            accesstoken=mapbox_access_token,
                            bearing = 0,
                            center = dict(
                                lat = lat2,
                                lon = lon2
                            ),
                            pitch = 0,
                            zoom=10
                        ),
                    )
                ]
            }
        )
        ]
)

if __name__=="__main__":
    app.run_server(debug=True)