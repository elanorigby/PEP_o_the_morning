from flask import Flask
from flask import render_template

def app_update(pepo, num):
    # create app instance named whatever current namespace is
    app = Flask(__name__)

    # wrap function in a route to make it a view
    @app.route('/')
    def index(pepo=pepo):
        return render_template('main.html', pepo=pepo, num=num)

    app.run(debug=False)
