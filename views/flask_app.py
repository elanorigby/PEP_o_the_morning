from flask import Flask
from flask import render_template
import randomcolor


def app_update(pepo, num):
    # create app instance named whatever current namespace is
    app = Flask(__name__)

    rand_color = randomcolor.RandomColor()
    color = str(rand_color.generate(luminosity='light')[0])
    print(color)

    # wrap function in a route to make it a view
    @app.route('/')
    def index(color=color):
        return render_template('main.html', pepo=pepo, num=num, color=color)

    app.run(debug=True)
