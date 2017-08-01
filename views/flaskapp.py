from flask import Flask
from flask import render_template
import randomcolor

import scrape


def color(lum):
    rand_color = randomcolor.RandomColor()
    color = str(rand_color.generate(luminosity=lum)[0])
    return color


def app_update(pepo):
    # create app instance named whatever current namespace is
    app = Flask(__name__)

    bkcolor = color('light')
    hovcolor = color('dark')

    title = scrape.title(pepo)

    # wrap function in a route to make it a view
    @app.route('/')
    def index():
        return render_template('main.html', pepo=pepo, title=title, bkcolor=bkcolor, hovcolor=hovcolor)

    app.run(debug=False)
