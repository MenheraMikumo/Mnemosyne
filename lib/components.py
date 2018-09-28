import dash_html_components as html
import dash_core_components as dcc
import glob
import json
import uuid
import pandas as pd

def H1(string):
    return html.H1(string, className="gs-header gs-text-header padded")
def H2(string):
    return html.H2(string, className="gs-header gs-text-header padded")
def H3(string):
    return html.H3(string, className="gs-header gs-text-header padded")
def H4(string):
    return html.H4(string, className="gs-header gs-text-header padded")
def H5(string):
    return html.H5(string, className="gs-header gs-text-header padded")
def H6(string):
    return html.H6(string, className="gs-header gs-text-header padded")

def MD(string):
    return html.Div(
            dcc.Markdown(string),
            style = {"margin-left":"5px", "margin-right":"5px"}
            )

def CRT(item):
    uid = str(uuid.uuid1())
    lst = glob.glob(item)
    if len(lst) > 1:
        fig_lst = [json.load(open(j)) for j in lst]
        Graph_list = [
                html.Div(
                    dcc.Graph(
                        id = fig_lst[0]['data'][0]['uid'],
                        figure = fig_lst[0],
                        config = {
                            'autosizable': True,
                            'displayModeBar': False,
                            },
                        style = {
                            'width':'100%',
                            }
                        ),
                    className="carousel-item active",
                    style={'width':'100%'},
                    ),
                ]
        for fig in fig_lst[1:]:
            Graph_list.append(
                    html.Div(
                        dcc.Graph(
                            id = fig['data'][0]['uid'],
                            figure = fig,
                            config = {
                                'autosizable': True,
                                'displayModeBar': False,
                                },
                            style = {
                                'width':'100%',
                                },
                            ),
                        className="carousel-item",
                        style={'width':'100%'},
                        ),
                    )

        return html.Div([
            html.Div(
                Graph_list,
                className="carousel-inner",
                ),
            html.A([
                html.Span(className="carousel-control-prev-icon",style={"background-color":"grey"},**{"aria-hidden":"true"}),
                html.Span("Previous",className="sr-only")
                ],
                className="carousel-control-prev",
                href="#"+uid,
                role="button",
                **{"data-slide":"prev"},
                ),
            html.A([
                html.Span(className="carousel-control-next-icon",style={"background-color":"grey"},**{"aria-hidden":"true"}),
                html.Span("Next",className="sr-only")
                ],
                className="carousel-control-next",
                href="#"+uid,
                role="button",
                **{"data-slide":"next"},
                ),
            ],
            className="carousel slide",
            **{"data-ride":"carousel"},
            id=uid,
                )

    elif len(lst) == 1: 
        fig = json.load(open(lst[0]))
        return html.Div(
                dcc.Graph(
                    id = fig['data'][0]['uid'],
                    figure = fig,
                    config = {
                        'autosizable': True,
                        'displayModeBar': False,
                        },
                        style = {
                        },
                    ),
                    style={'width':'100%'},
                )

def TBL(string):
    df = pd.read_table(string)
    head = [html.Tr([html.Td(name) for name in df.columns])]
    body = [html.Tr([html.Td(cell) for cell in row]) for row in df.values]
    table = head + body
    return html.Div(
            html.Table(table),
            style = {"margin-left":"5px", "margin-right":"5px"},
            )

func_dic = {
        'H1': H1,
        'H2': H2,
        'H3': H3,
        'H4': H4,
        'H5': H5,
        'H6': H6,
        'MD': MD,
        'CRT': CRT,
        'TBL': TBL,
        }

def COL(lst,width="twelve columns"):
    ret = []
    for elm in lst:
        key, value = list(elm.items())[0]
        ret.append(func_dic[key](value))
    return html.Div(
            ret,
            className = width,
            )

def ROW(lst):
    if len(lst) == 1:
        ret = [COL(list(elm.values())[0],"twelve columns") for elm in lst]
    elif len(lst) == 2:
        ret = [COL(list(elm.values())[0],"six columns") for elm  in lst]
    else:
        raise ValueError
    return html.Div(
            ret,
            className = 'row',
            )

def print_button():
    printButton = html.A(['Print PDF'],className="button no-print print",style={'position': "absolute", 'top': '-40', 'right': '0'})
    return printButton

def PAGE(id, lst, head):
    menubar = [html.Div([
        html.Div([
           dcc.Input(id='hash-box', type='text', className="button no-print", style={'position': "absolute", 'top': '-38.3', 'width':'50%', 'right': '50%'}),
            ], className = "six cloumns"),
        html.Div([
            html.Button('Submit', className="btn btn-primary btn-sm no-print", id='button', style={'position': "absolute", 'top': '-38.3', 'right': '30%'}),
            ], className = "three columns"),
        html.Div([
            print_button(),
            ], className = "three columns"),
        ],className = 'row')]
    head = [ROW(list(elm.values())[0]) for elm in head]
    ret = [ROW(list(elm.values())[0]) for elm in lst]
    return  html.Div(
            head + ret,
            className = 'page',
            id = id,
            )

def REPORT(loads):
    menubar = [html.Div([
        html.Div([
            dcc.Input(id='hash-box', type='text', className="button no-print", style={'position': "absolute", 'top': '-38.3', 'width':'50%', 'right': '50%'}),
            ], className = "six cloumns"),
        html.Div([
            html.Button('Submit', className="btn btn-primary btn-sm no-print", id='button', style={'position': "absolute", 'top': '-38.3', 'right': '30%'}),
            ], className = "three columns"),
        html.Div([
            print_button(),
            ], className = "three columns"),
        ],className = 'row')]
    ret = [PAGE(*list(page.items())[0], loads['HEADER']) for page in loads['CONTENT']]
    ret[0].children = menubar + ret[0].children
    return html.Div(
            ret,
            )

