# styling
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
import dash_mantine_components as dmc
# pip install dash-iconify
from dash_iconify import DashIconify

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
                             children=[
                                 dmc.Card(
                                     children=[
                                         dmc.CardSection(
                                             dmc.Image(
                                                 src="https://images.unsplash.com/photo-1527004013197-933c4bb611b3?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=720&q=80",
                                                 height=160,
                                             )
                                         ),
                                         dmc.Group(
                                             [
                                                 dmc.Text(
                                                     "Norway Fjord Adventures", weight=500),
                                                 dmc.Badge(
                                                     "On Sale", color="red", variant="light"),
                                             ],
                                             position="apart",
                                             mt="md",
                                             mb="xs",
                                         ),
                                         dmc.Text(
                                             "With Fjord Tours you can explore more of the magical fjord landscapes with tours and activities on and around the fjords of Norway",
                                             size="sm",
                                             color="dimmed",
                                         ),
                                         dmc.Button(
                                             "Book classic tour now",
                                             variant="light",
                                             color="blue",
                                             fullWidth=True,
                                             mt="md",
                                             radius="md",
                                         ),
                                     ],
                                     withBorder=True,
                                     shadow="sm",
                                     radius="md",
                                     #  style={"width": 350},
                                 )]), span=4),
                         dmc.Col(children=html.Div(
                             children=[
                                 dmc.Card(
                                     children=[
                                         dmc.CardSection(
                                             dmc.Image(
                                                 src="https://images.unsplash.com/photo-1527004013197-933c4bb611b3?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=720&q=80",
                                                 height=160,
                                             )
                                         ),
                                         dmc.Group(
                                             [
                                                 dmc.Text(
                                                     "Norway Fjord Adventures", weight=500),
                                                 dmc.Badge(
                                                     "On Sale", color="red", variant="light"),
                                             ],
                                             position="apart",
                                             mt="md",
                                             mb="xs",
                                         ),
                                         dmc.Text(
                                             "With Fjord Tours you can explore more of the magical fjord landscapes with tours and activities on and around the fjords of Norway",
                                             size="sm",
                                             color="dimmed",
                                         ),
                                         dmc.Button(
                                             "Book classic tour now",
                                             variant="light",
                                             color="blue",
                                             fullWidth=True,
                                             mt="md",
                                             radius="md",
                                         ),
                                     ],
                                     withBorder=True,
                                     shadow="sm",
                                     radius="md",
                                     #  style={"width": 350},
                                 )
                             ]), span=4),
                         dmc.Col(children=html.Div(
                             children=[
                                 dmc.Card(
                                     children=[
                                         dmc.CardSection(
                                             dmc.Image(
                                                 src="https://images.unsplash.com/photo-1527004013197-933c4bb611b3?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=720&q=80",
                                                 height=160,
                                             )
                                         ),
                                         dmc.Group(
                                             [
                                                 dmc.Text(
                                                     "Norway Fjord Adventures", weight=500),
                                                 dmc.Badge(
                                                     "On Sale", color="red", variant="light"),
                                             ],
                                             position="apart",
                                             mt="md",
                                             mb="xs",
                                         ),
                                         dmc.Text(
                                             "With Fjord Tours you can explore more of the magical fjord landscapes with tours and activities on and around the fjords of Norway",
                                             size="sm",
                                             color="dimmed",
                                         ),
                                         dmc.Button(
                                             "Book classic tour now",
                                             variant="light",
                                             color="blue",
                                             fullWidth=True,
                                             mt="md",
                                             radius="md",
                                         ),
                                     ],
                                     withBorder=True,
                                     shadow="sm",
                                     radius="md",
                                     #  style={"width": 350},
                                 )]), span=4),
                         dmc.Col(children=html.Div(
                             children=[
                                 dmc.Group(
                                     [
                                         dmc.Button("Default button"),
                                         dmc.Button("Subtle button",
                                                    variant="subtle"),
                                         dmc.Button("Filled button",
                                                    variant="filled"),
                                         dmc.Button("Light button",
                                                    variant="gradient",
                                                    gradient={"from": "green", "to": "blue", "deg": 60}),
                                         dmc.Button("Outline button",
                                                    variant="outline",
                                                    rightIcon=DashIconify(icon="logos:twitter")),
                                     ]
                                 )]), span=4)
                     ]),
            dmc.ButtonGroup(
                [
                    dmc.Button("First", variant="outline"),
                    dmc.Button("Second", variant="outline"),
                    dmc.Button("Third", variant="outline"),
                ],
                style={"margin-top": "20px"}
            )
        ],
            sizes="xs", fluid=True, px=100, py=10)
    ]
)


if __name__ == "__main__":
    app.run_server(debug=True)
