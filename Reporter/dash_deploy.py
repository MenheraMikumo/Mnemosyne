# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import yaml
from django_plotly_dash import DjangoDash
from lib import components
from jinja2 import Template
import yaml
from dash.dependencies import Input, Output, State

app = DjangoDash('report')

config = yaml.load(open('config.yaml'))
#rendered_yaml = Template(open(f'{config["templates_Dir"]}/default.yml').read()).render(**config)
#loads = yaml.load(rendered_yaml)

app.layout = html.Div([
    html.Div([
        html.Div([
            html.Div([
                dcc.Input(id='hash-box', type='text', className="form no-print", style={'position': "absolute", 'top': '-38.3', 'width':'50%', 'right': '50%'}),
                ], className = "six cloumns"),
            html.Div([
                html.Button('Submit', className="btn btn-primary btn-sm no-print", id='submit-button', style={'position': "absolute", 'top': '-38.3', 'right': '30%'}),
                ], className = "three columns"),
            html.Div([
                components.print_button(),
                ], className = "three columns"),
            ],className = 'row'),
        ],className='page'),
    ],id='fullReport')

@app.callback(
        Output('fullReport', 'children'),
        [Input('submit-button', 'n_clicks')],
        [State('hash-box', 'value')],
        )
def render_report(n_clicks, hash_value):
    if hash_value == None:
        return [html.Div([
            html.Div([
                html.Div([
                    dcc.Input(id='hash-box', type='text', className="form no-print", style={'position': "absolute", 'top': '-38.3', 'width':'50%', 'right': '50%'}),
                    ], className = "six cloumns"),
                html.Div([
                    html.Button('Submit', className="btn btn-primary btn-sm no-print", id='submit-button', style={'position': "absolute", 'top': '-38.3', 'right': '30%'}),
                    ], className = "three columns"),
                html.Div([
                    components.print_button(),
                    ], className = "three columns"),
                ],className = 'row'),
            html.Div(
            dcc.Markdown("""
# Welcome~
            """),
            style = {'top':'50%'}
            )
            ],className='page')]
    else:
        try:
            try:
                params = yaml.load(open(f'{config["results_Dir"]}/{hash_value}/params.yaml'))
            except:
                params = yaml.load(open(f'{config["results_Dir"]}/{hash_value}/params.json'))
            params.update(config)
            rendered_yaml = Template(open(f'{config["templates_Dir"]}/{params["template"]}.yml').read()).render(**params)
            loads = yaml.load(rendered_yaml)
            ret =  components.REPORT(loads).children
            return ret
        except:
            return [html.Div([
                html.Div([
                    html.Div([
                        dcc.Input(id='hash-box', type='text', className="form no-print", style={'position': "absolute", 'top': '-38.3', 'width':'50%', 'right': '50%'}),
                        ], className = "six cloumns"),
                    html.Div([
                        html.Button('Submit', className="btn btn-primary btn-sm no-print", id='submit-button', style={'position': "absolute", 'top': '-38.3', 'right': '30%'}),
                        ], className = "three columns"),
                    html.Div([
                        components.print_button(),
                        ], className = "three columns"),
                    ],className = 'row'),
                dcc.Markdown("""
#### Error~
                """)
                ],className='page')]


external_css = ["https://cdnjs.cloudflare.com/ajax/libs/normalize/7.0.0/normalize.min.css",
        "https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css",
        "//fonts.googleapis.com/css?family=Raleway:400,300,600",
        "/static/KQrXdb.css",
        "https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css",
#        "/static/bootstrap.min.css",
        ]

for css in external_css:
    app.css.append_css({"external_url": css})

external_js = [
        "https://code.jquery.com/jquery-3.2.1.min.js",
        "/static/YaXojL.js",
#        "/static/bootstrap.min.js",
#        "https://codepen.io/bcd/pen/YaXojL.js"
        ]

for js in external_js:
    app.scripts.append_script({"external_url": js})

if __name__ == '__main__':
    app.run_server(debug=True)
