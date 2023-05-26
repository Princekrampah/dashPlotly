# styling
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
import dash_mantine_components as dmc

# 1. External stylesheet

df = pd.read_csv("../../datasets/WalmartSalesData.csv")

app = Dash(__name__, external_stylesheets=[
    # include google fonts
    "https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400;500;900&display=swap"
])

# 5. Adding styles
style = {
    "border": f"1px solid {dmc.theme.DEFAULT_COLORS['indigo'][4]}",
    "textAlign": "center",
}

# 2. Add theme and general styling
app.layout = dmc.MantineProvider(
    theme={
        "fontFamily": "'Inter', sans-serif",
        "primaryColor": "indigo",
        "components": {
            "Button": {"styles": {"root": {"fontWeight": 400}}},
            "Alert": {"styles": {"title": {"fontWeight": 500}}},
            "AvatarGroup": {"styles": {"truncated": {"fontWeight": 500}}},
        },
    },
    inherit=True,
    withGlobalStyles=True,
    withNormalizeCSS=True,

    # 3. Adding a container
    children=[
        dmc.Container(children=[
            # 4. Adding the grid layout
            # set grow to allow last row to fill the whole available row section
            dmc.Grid(gutter="xl",
                     grow=True,
                     justify="center",
                     align="center",

                     children=[
                         dmc.Col(children=html.Div(
                             children="1", style=style), span=4),
                         dmc.Col(children=html.Div(
                             children="2", style=style), span=4),
                         dmc.Col(children=html.Div(
                             children="3", style=style), span=4),
                         dmc.Col(children=html.Div(
                             children="4", style=style), span=4)
                     ])
        ],
            sizes="xs", fluid=True, px=100, py=10)
    ]
)


if __name__ == "__main__":
    app.run_server(debug=True)
