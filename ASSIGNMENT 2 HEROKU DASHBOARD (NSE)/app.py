from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output
# import requests
# import json

app = Dash(__name__)
server = app.server
data = pd.read_csv("./data.csv")
print(data.head())
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Nairobi Securities Exchange',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    html.Div(children='Dash: A time series stock prices for listed companies.', style={
        'textAlign': 'center',
        'color': colors['text']
    }),
    dcc.Dropdown(
        id="select_ticker",
        options=[
            {'label': 'Absa Bank Kenya Plc', 'value': 'ABSA'},
            {'label': 'ARM Cement Limited', 'value': 'ARM'},
            {'label': 'British American Tobacco (Kenya) Ltd.', 'value': 'BAMB'},
            {'label': 'British American Tobacco ', 'value': 'BAT'},
            {'label': 'Crown Paints Kenya Limited', 'value': 'BERG'},
            {'label': 'Uchumi Supermarket Limited', 'value': 'UCHM'},
            {'label': 'Umeme Limited', 'value': 'UMME'},
            {'label': 'Unga Group Limited', 'value': 'UNGA'},
            {'label': 'Williamson Tea Kenya Limited', 'value': 'WTK'},
            {'label': 'Express Kenya Limited', 'value': 'XPRS'},
        ],
        placeholder='Select Company',
        value='ABSA' # This argument makes sure that ABSA is the default value ploted when the page is loaded
                     # Without the value argument, the default plot will be blamk untill the user selects from the dropdown

    ),

    # html.Label('Text Box'),
    # dcc.Input(value='BAT', type='text'),
    dcc.Graph(
        id='Graph1'
    )
])

# html.Div([
#     html.Div([
#         dcc.Graph(
#             id='graph', config={'displayModelBar': False}
#         )
#
#     ], className='card_container ten columns')
# ], className='run display flex',
#
#     id='appcontainer', style={'display': 'flex', 'flex direction': 'column'}
# )


# callbacks
@app.callback(
    Output(component_id='Graph1', component_property='figure'),#you used small o for output
    Input(component_id='select_ticker', component_property='value')#you used small i for input
)
def enter_input(ticker):
    df = data.copy()
    df["price"] = df["price"].str.replace(",", "").astype("float")
    df["date"] = pd.to_datetime(df["date"])
    df["date"] = df["date"].dt.strftime("%d/%m/%Y")
    df = df[(df["ticker"] == ticker)]
    fig = px.bar(df, x="date", y="price") # Time series data is best represented with a line graph
    # fig.update_layout[colourway := ['#BE33FF', '#CEFF33'],
    #                   (template := 'plotly express_dark',
    #                    paper_bgcolor := colors['background'],
    #                    plot_bgcolor := colors['background'],
    #                    # margin == {'b': 15},
    #                    # hovermode == 'x',
    #                    # autosize == True,
    #                    # title == {'text': 'Nairobi Stock Exchange', 'font': {'color': 'cyan'}}
    #                 )]

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
