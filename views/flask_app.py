from flask import Flask
from flask import render_template
import randomcolor
from PEPSoup import get_pep_name

def get_color():
    rand_color = randomcolor.RandomColor()
    color = str(rand_color.generate(luminosity='light')[0])
    return color

def app_update(pepo, num):
    # create app instance named whatever current namespace is
    app = Flask(__name__)

    color = get_color()

    pep_name = get_pep_name(pepo)

    # wrap function in a route to make it a view
    @app.route('/')
    def index(color=color):
        return render_template('main.html', pepo=pepo, pep_name=pep_name, color=color)

    app.run(debug=False)
