# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import yaml
from django_plotly_dash import DjangoDash
from lib import components
import yaml

app = DjangoDash('report')

config = yaml.load(open('config.yaml'))
loads = yaml.load(open('Reporter/media/report_templates/default.yml'))

app.layout = components.PAGE(*list(loads[0].items())[0])

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
