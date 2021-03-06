'''
This modules incorporates all tabs (layouts) into one html.
'''

from dash import html, dcc
from dash.dependencies import Input, Output
from crimes_app.dashboard.maindash import app
import plotly.express as px

# Connect to the layout and callback of different tabs
from crimes_app.dashboard.crime_tab import crime_layout
from crimes_app.dashboard.social_inv_tab import si_layout
from crimes_app.dashboard.index_color_tab import hm_layout

# App Layout with Tabs
def make_layout():
    '''
    App layout with tabs
    '''
    #colors = {
    #'background': '#B9E5E8',
    #'text': '#7FDBFF'
    #}

    return html.Div(children = [
        html.H1("Ward-level data, Chicago (2020)", style = {"textAlign": "center"}),
        html.Hr(),
        dcc.Tabs(id = "tabs", value = "tab-crime", children = 
            [
                dcc.Tab(label="Crime", value = "tab-crime"),
                dcc.Tab(label="Social Investment", value = "tab-si"),
                dcc.Tab(label="Chicago Heatmap", value = "tab-hm")
            ]),
        html.Div(id = 'content', children = [])
    ])

# Connect Plotly graphs with Dash Core Components
@app.callback(
    Output("content", "children"),
    [Input("tabs", "value")]
)

# Render the selected tab
def select_tab(tab_slctd):
    '''
    Define the callback function to render the 
    chosen tab
    '''
    if tab_slctd == "tab-crime":
        return crime_layout
    elif tab_slctd == "tab-si":
        return si_layout
    elif tab_slctd == "tab-hm":
        return hm_layout