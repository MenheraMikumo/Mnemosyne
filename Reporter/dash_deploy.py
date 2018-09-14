# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import yaml
from django_plotly_dash import DjangoDash
from lib import components
import yaml

app = DjangoDash('report')

loads = yaml.load(open('Reporter/media/report_templates/default.yml'))

#def print_button():
#    printButton = html.A(['Print PDF'],className="button no-print print",style={'position': "absolute", 'top': '-40', 'right': '0'})
#    return printButton

#def get_header():
#    header = html.Div([
#
#        html.Div([
#            html.H5(
#                'Vanguard 500 Index Fund Investor Shares')
#        ], className="twelve columns padded")
#
#    ], className="row gs-header gs-text-header")
#    return header

#def get_page(lst):
#    ret_lst = [print_button()]
#    for elm in lst:
#        print(elm)
#        if list(elm.keys())[0] == 'MD':
#            ret_lst.append(html.Div(components.MD_half(list(elm.values())[0]),className="row"))
#    return html.Div(ret_lst,className='page')

app.layout = components.PAGE(*list(loads[0].items())[0])

external_css = ["https://cdnjs.cloudflare.com/ajax/libs/normalize/7.0.0/normalize.min.css",
        "https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css",
        "//fonts.googleapis.com/css?family=Raleway:400,300,600",
        "/static/KQrXdb.css",
        "https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css"]

for css in external_css:
    app.css.append_css({"external_url": css})

external_js = [
        "https://code.jquery.com/jquery-3.2.1.min.js",
        "/static/YaXojL.js"
#        "https://codepen.io/bcd/pen/YaXojL.js"
]

for js in external_js:
    app.scripts.append_script({"external_url": js})

if __name__ == '__main__':
    app.run_server(debug=True)
