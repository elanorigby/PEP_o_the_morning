from flask import Flask
from flask import render_template
import randomcolor

from PEPSoup import get_pep_name


def get_color(lum):
    rand_color = randomcolor.RandomColor()
    color = str(rand_color.generate(luminosity=lum)[0])
    return color


def app_update(pepo):
    # create app instance named whatever current namespace is
    app = Flask(__name__)

    bkcolor = get_color('light')
    hovcolor = get_color('dark')

    pep_name = get_pep_name(pepo)

    # wrap function in a route to make it a view
    @app.route('/')
    def index():
        return render_template('main.html', pepo=pepo, pep_name=pep_name, bkcolor=bkcolor, hovcolor=hovcolor)

    app.run(debug=False)
