# Data Visualization
from dash import Dash, html, dash_table, dcc
import pandas as pd
import plotly.express as px

df = pd.read_csv("../../datasets/WalmartSalesData.csv")

# gapminder dataset
gm_df = px.data.gapminder()

# carshare df
carshare_df = px.data.carshare()


app = Dash(__name__)


app.layout = html.Div([
    html.Div(
        children="Hello world"
    ),
    # add the visualization component
    dcc.Graph(figure=px.histogram(df, x="Branch", y="Total", histfunc="sum")),
    dcc.Graph(figure=px.pie(df, names="Branch", values="gross income")),
    # gapminder dataset
    dcc.Graph(figure=px.scatter(gm_df, x="gdpPercap", y="lifeExp", animation_frame="year", animation_group="country",
                                size="pop", color="continent", hover_name="country", facet_col="continent",
                                log_x=True, size_max=45, range_x=[100, 100000], range_y=[25, 90])),
    dcc.Graph(figure=px.scatter(df, x="Total", y="gross margin percentage", size="Tax 5%", animation_frame="Date",
                                animation_group="Branch", color="Branch", hover_name="Branch", facet_col="Gender")),
    dcc.Graph(figure=px.scatter_mapbox(carshare_df, lat="centroid_lat", lon="centroid_lon", color="peak_hour", size="car_hours",
                                       color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=10,
                                       mapbox_style="carto-positron")),
    dcc.Graph(figure=px.scatter_geo(gm_df, locations="iso_alpha", color="continent", hover_name="country", size="pop",
                                    animation_frame="year", projection="natural earth")),
    dcc.Graph(figure=px.histogram(gm_df, x='continent', y='lifeExp', histfunc='avg'))

])

# run the app in the main thread
if __name__ == "__main__":
    app.run_server(debug=True)
