import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import dash_bootstrap_components as dbc
from variables import *


app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])



app.layout = dbc.Container(
    [   
        html.Br(),
        dbc.Row(cards),
        html.Br(),
        html.Br(),
        html.Br(),
        dbc.Row(
            [   
                dbc.Col(graphs1,md=5),
                dbc.Col(graphs2,md=5),
                dbc.Col(controls),
            ],
        ),
    ],
    fluid=True,
    style={'margin':'0 !important','padding':'0 !important'}
)

@app.callback(
    Output("bar-graph", "figure"),
    [
        Input("age-group", "value"),
        Input("job-type", "value"),
        Input("marital-status", "value"),
        Input("churn-type", "value"),
    ],
)
def make_graph(age, job, marital,churn):
    temp = df[(df['age_group']=='{}'.format(age)) & (df['job_type']=='{}'.format(job)) & (df['marital']=='{}'.format(marital)) & (df['churn_cat']=='{}'.format(churn))]
    temp = pd.DataFrame(df[['month']].groupby('month').size().reindex(months_in_order).reset_index())
    temp.columns = ['Month','Count']
    fig1 = px.bar(temp,x='Month',y="Count",barmode='group',color_discrete_sequence=['#7201a8'])
    return fig1
 
@app.callback(
    Output("line-graph", "figure"),
    [
        Input("month-quarter","value"),
    ],
)
def make_graph2(month_quarter):
    if month_quarter=="month":
        df['month'] = df['month'].apply(lambda x: x.title())
        time_data = df[['camp_success','month']].groupby('month').count().reindex(months_in_order)
        fig2 = px.line(time_data.cumsum(), x=time_data.index, y="camp_success",labels={'x':'Months'},height=400,color_discrete_sequence=['#0d0887'])
        return fig2
    else:
        time_data = df[['camp_success','quarter']].groupby('quarter').count().reindex(quarter_in_order)
        fig2 = px.line(time_data.cumsum(), x=time_data.index, y="camp_success",labels={'x':'Quarter'},height=400,color_discrete_sequence=['#0d0887'])
        return fig2

@app.callback(
    Output("bar-graph2", "figure"),
    [
        Input("loan-cat","value"),
        Input("churn-type", "value"),
        Input("age-group","value")
    ],
)
def make_graph3(loan,churn,age):
    temp3 = df[(df['hasloan']==loan) & (df['churn_cat']=='{}'.format(churn)) & (df['age_group']== '{}'.format(age))]
    fig3 = px.histogram(temp3,x="job_type",y="balance",histfunc="avg",color_discrete_sequence=['#46039f'])
    return fig3    

@app.callback(
    Output("tree-map", "figure"),
    [
        Input("churn-type", "value"),
    ],
)
def make_graph4(churn):
    temp4 = df[(df['churn_cat']=='{}'.format(churn))]
    temp4 = temp4[['job_type','last_contact_duration']].groupby("job_type").mean('last_contact_duration').round(2).reset_index()
    fig4 = px.treemap(temp4,path=['job_type'],values='last_contact_duration',height=400,color_discrete_sequence=px.colors.sequential.Plasma)
    fig4.data[0].textinfo = 'label+value'
    return fig4

if __name__ == "__main__":
    app.run_server()