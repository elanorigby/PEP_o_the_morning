from flask import Flask
from flask import render_template

def app_update(pepo):
    # create app instance named whatever current namespace is
    app = Flask(__name__)

    # wrap function in a route to make it a view
    @app.route('/')
    def index(pepo=pepo):
        return render_template('main.html', pepo=pepo)

    app.run(debug=False)
