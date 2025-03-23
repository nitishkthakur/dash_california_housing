import dash
from dash import dcc, html
import plotly.express as px
from sklearn.datasets import fetch_california_housing
import pandas as pd

# Load the dataset
california = fetch_california_housing()
df = pd.DataFrame(california.data, columns=california.feature_names)
df["MedHouseVal"] = california.target

# Create scatter plot
fig = px.scatter(df, x="MedInc", y="MedHouseVal",
                 title="California Housing: Income vs House Value",
                 labels={"MedInc": "Median Income", "MedHouseVal": "Median House Value"},
                 color="HouseAge")

# Initialize Dash app
app = dash.Dash(__name__)

# Define layout
app.layout = html.Div([
    html.H1("California Housing Dashboard"),
    dcc.Graph(figure=fig)
])

# Run app
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8050)
