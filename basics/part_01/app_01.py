from dash import Dash, html

# Instantiate the app by calling the 
# Dash constructor
app = Dash(__name__)

# The app layout represents the app components 
# that will be displayed in the web browser
app.layout = html.Div([
    html.Div(
        children="Hello world"
    )
])

# run the app in the main thread
if __name__ == "__main__":
    app.run_server(debug=True)