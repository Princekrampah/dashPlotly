# Connecting data
from dash import Dash, html, dash_table
import pandas as pd

df = pd.read_csv("../../datasets/WalmartSalesData.csv")


app = Dash(__name__)


app.layout = html.Div([
    html.Div(
        children="Hello world"
    ),
    # add the data component
    dash_table.DataTable(data=df.to_dict(orient="records"), page_size=10)
])

# run the app in the main thread
if __name__ == "__main__":
    app.run_server(debug=True)