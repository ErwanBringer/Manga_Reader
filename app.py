#Importation des librairies
import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_leaflet.express as dlx
import dash_core_components as dcc
from dash.dependencies import Input, Output, State


#Définition de l'app dash avec le thème solar
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SOLAR])

server = app.server

#Création card 1


card_main = dbc.Card(
    [
        #Image
        dbc.CardImg(src='/assets/eeee.jpg', top=True, bottom=False,
                    title="image", alt='band',id='band'),
        dcc.Dropdown(id="user_choice_contours", options=[{'label': cont, "value": cont} for cont in ['arome','iris','commune']],
                             value='arome', clearable=False, style={"color": "#000000"}),
        dbc.CardImg(src='/assets/0.jpg', top=True, bottom=False,
                    title="image", alt='band',id='band2'),
        dbc.Button("NEXT", color="primary", className="mr-1",id="but"),
    ],
    color="dark",
    inverse=True,
    outline=False,
)

app.layout = html.Div([
    dbc.Row(dbc.Col(card_main, width=3), justify="around")
             ])


@app.callback(Output("band2", "src"), [Input("but", "n_clicks")])
def update(n_clicks):
    return str(n_clicks)+'.jpg'

if __name__ == "__main__":
    app.run_server(debug=True)


