from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px

df = pd.read_csv("../../datasets/WalmartSalesData.csv")

app = Dash(__name__)

app.layout = html.Div([
    html.Div(
        children="Callbacks and Control"
    ),
    html.H1(children="Control And Callbacks"),
    # dash_table.DataTable(data=df.to_dict(orient="records"), page_size=10),
    dcc.Graph(figure={},
              style={'width': '90vh',
                     'height': '70vh',
                     'margin-top': '100px'
                     },
              id="control-bar-graph"
              ),
    # value is the default value
    dcc.RadioItems(options=["Male", "Female"], id="radio-btn-value", value="Male")
])


# The inputs and outputs of our app are the properties of a 
# particular component. In this example, our input is the value 
# property of the component that has the ID 
# "controls-and-radio-item". If you look back at the layout, 
# you will see that this is currently lifeExp. Our output is 
# the figure property of the component with the ID 
# "controls-and-graph", which is currently an empty dictionary 
# (empty graph).



@callback(
    Output(component_id="control-bar-graph", component_property="figure"),
    Input(component_id="radio-btn-value", component_property="value")
)
def update_bar_graph(col_choosen):
    fig = px.histogram(data_frame=df[df["Gender"] == col_choosen], x="Branch", y="Total",
                       histfunc="sum")
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
