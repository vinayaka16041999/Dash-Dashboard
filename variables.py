import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
import plotly.graph_objects as go

df = pd.read_csv(r'df.csv')

unique_age_groups = df['age_group'].unique()
unique_job_type = df['job_type'].unique()
unique_marital_type = df['marital'].unique()
unique_churn_type = df['churn_cat'].unique()
unique_loan_type = df['hasloan'].unique()

months_in_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
quarter_in_order = ['Q1','Q2','Q3','Q4']

controls = dbc.Card(
    [   
        html.H5("Filter Menu",style={'text-align':'center'}),
        dbc.FormGroup(
            [
                dbc.Label("Age Group"),
                dcc.Dropdown(
                    id="age-group",
                    options=[
                        {"label": col, "value": col} for col in unique_age_groups
                    ],
                    value="Adult",
                ),
            ],
            className='mt-5'
        ),
        dbc.FormGroup(
            [
                dbc.Label("Job Type"),
                dcc.Dropdown(
                    id="job-type",
                    options=[
                        {"label": col, "value": col} for col in unique_job_type
                    ],
                    value="management",
                ),
            ]
        ),
        dbc.FormGroup(
            [
                dbc.Label("Marital Status"),
                dcc.Dropdown(
                    id="marital-status",
                    options=[
                        {"label": col, "value": col} for col in unique_marital_type
                    ],
                    value="single",
                ),
            ]
        ),
        dbc.FormGroup(
            [
                dbc.Label("Churn Type"),
                dbc.RadioItems(
                    id="churn-type",
                    options=[
                        {"label": col,"value": col} for col in unique_churn_type
                    ],
                    value="Subscribed"
                ),
            ]
        ),
        dbc.FormGroup(
            [
                dbc.Label("Loan Category"),
                dbc.RadioItems(
                    id="loan-cat",
                    options=[
                        {"label": "True","value": True},
                        {"label": "False","value": False}
                    ],
                    value=True
                ),
            ]
        ),
        dbc.FormGroup(
            [
                dbc.Label("Month/Quarter"),
                dbc.RadioItems(
                    id="month-quarter",
                    options=[
                        {"label": "Monthly","value":"month" },
                        {"label": "Quarterly","value": "quarter" }
                    ],
                    value="month"
                ),
            ]
        )
    ],
    body=True,
    className="sticky-top h-100",
    style={'box-shadow':'2px 2px 10px grey'}
    
)

graphs1 = [
 
    dbc.Row(dbc.Col([
        html.H3("What customer segment to target? and When?",style={'text-align':'center'}),
        dcc.Graph(id="bar-graph")],md=12,className='p-0')
        ),
    dbc.Row([dbc.Col([
        html.H3("Subscribers gain over time.....",style={'text-align':'center'}),
        dcc.Graph(id="line-graph")],md=12),]),

]

graphs2 = [
 
    dbc.Row(dbc.Col([
        html.H3("Average bank balance of Customers by JobType.",style={'text-align':'center'}),
        dcc.Graph(id="bar-graph2")],md=12)
        ),
    dbc.Row([dbc.Col([
        html.H3("Average call duration by JobType.",style={'text-align':'center'}),
        dcc.Graph(id="tree-map")],md=12),]),

]

cards = [
        dbc.Col(
            dbc.Card(
            dbc.CardBody(
                [
                    html.H4("1826.74", className="card-title"),
                    html.H6(
                        [
                            "Average bank balance of Customers (Subscribers/Unsubscribers)"            
                        ],
                        className="card-text",
                    ),
                ]
            ),
            className="w-100",
            style={'box-shadow':'2px 2px 10px grey'}
        )
        ),
        dbc.Col(
            dbc.Card(
            dbc.CardBody(
                [
                    html.H4("48.7%", className="card-title"),
                    html.H6(
                        [
                            "of the ",html.I("Subscribers"), " are ",html.Code("Students")," or",html.Br(),html.Code(" Retired.")
                        ],
                        className="card-text",
                    ),
                ]
            ),
            className="w-100",
            style={'box-shadow':'2px 2px 10px grey'}
        )
        ),
        dbc.Col(
            dbc.Card(
            dbc.CardBody(
                [
                    html.H4("83%", className="card-title"),
                    html.H6(
                        [
                            "new",html.I("Subscribers")," gained since last camapaign.",html.Br()
                        ],
                        className="card-text",
                    ),
                ]
            ),
            className="w-100",
            style={'box-shadow':'2px 2px 10px grey'}
        )
        ),
        dbc.Col(
            dbc.Card(
            dbc.CardBody(
                [
                    html.H4("3346", className="card-title"),
                    html.H6(
                        [
                            "new ",html.I("Subscribers")," gained since last",html.Br()," campaign." 
                        ],
                        className="card-text",
                    ),
                ]
            ),
            className="w-100",
            style={'box-shadow':'2px 2px 10px grey'}
        )
        ),
        dbc.Col(
            dbc.Card(
            dbc.CardBody(
                [
                    html.H4("61%", className="card-title"),
                    html.H6(
                        [
                            "of the ",html.I("Subscribers")," has no loan.(Personal or House) "
                        ],
                        className="card-text",
                    ),
                ]
            ),
            className="w-100",
            style={'box-shadow':'2px 2px 10px grey'}
        )
        ),
        dbc.Col(
            dbc.Card(
            dbc.CardBody(
                [
                    html.H4("557.25", className="card-title"),
                    html.H6(
                        [
                            "Average call duration for successfully gained ",html.I("Subscriber.")
                        ],
                        className="card-text",
                    ),
                ]
            ),
            className="w-100",
            style={'box-shadow':'2px 2px 10px grey'}
        )
        )
    
    ]



           