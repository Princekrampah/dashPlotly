from dash import Dash, html, dcc, dash_table
import pandas as pd
import plotly.express as px
import dash_mantine_components as dmc

# instantiate app
app = Dash(__name__)

# data import
df = pd.read_csv("./dataset/walmartData.csv")

# create a layout
app.layout = dmc.MantineProvider(theme={
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
                                     dmc.Group(
                                         [
                                             dmc.Text(
                                                 "Revenue By Branch", weight=500),
                                             dmc.Badge(
                                                 "Revenue", color="red", variant="light"),
                                         ],
                                         position="apart",
                                         mt="md",
                                         mb="xs",
                                     ),
                                     dmc.CardSection(
                                         dcc.Graph(figure=px.histogram(
                                             df, x="branch", y="revenue", histfunc="sum"))
                                     )],
                                 withBorder=True,
                                 shadow="sm",
                                 radius="md",
                                 #  style={"width": 350},
                             )]), span=4),
                     dmc.Col(children=html.Div(
                         children=[
                             dmc.Card(
                                 children=[
                                     dmc.Group(
                                         [
                                             dmc.Text(
                                                 "Gross Sales By Branch", weight=500),
                                             dmc.Badge(
                                                 "Gross Sales", color="red", variant="light"),
                                         ],
                                         position="apart",
                                         mt="md",
                                         mb="xs",
                                     ),
                                     dmc.CardSection(
                                         dcc.Graph(figure=px.pie(df, names="branch", values="gross_income")))],
                                 withBorder=True,
                                 shadow="sm",
                                 radius="md",
                                 #  style={"width": 350},
                             )]), span=4),
                     dmc.Col(children=html.Div(
                         children=[
                             dmc.Card(
                                 children=[
                                     dmc.Group(
                                         [
                                             dmc.Text(
                                                 "Reveneu Trend", weight=500),
                                             dmc.Badge(
                                                 "Revenue Trend", color="red", variant="light"),
                                         ],
                                         position="apart",
                                         mt="md",
                                         mb="xs",
                                     ),
                                     dmc.CardSection(
                                         dcc.Graph(figure=px.histogram(df, x="date", y="revenue", histfunc="sum")))],
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
                                         dash_table.DataTable(data=df[["revenue", "cogs", "gross_income", "gross_margin_pct"]].to_dict(orient="records"), page_size=10)),

                                 ],
                                 withBorder=True,
                                 shadow="sm",
                                 radius="md",
                                 #  style={"width": 350},
                             )]), span=4)
                 ])
    ],
        sizes="xs", fluid=True, px=100, py=10)
]
)

# entry point
if __name__ == "__main__":
    app.run_server(debug=True)
