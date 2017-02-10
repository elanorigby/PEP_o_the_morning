from flask import Flask
from flask import render_template

from color_get import get_color
from pusher import push_it_real
from PEPSoup import get_pep_name

# create app instance named whatever current namespace is
app = Flask(__name__)

bkcolor = get_color('light')
hovcolor = get_color('dark')

pepo = push_it_real()
pep_name = get_pep_name(pepo)

# wrap function in a route to make it a view
@app.route('/')
def index():
    return render_template('main.html', pepo=pepo, pep_name=pep_name, bkcolor=bkcolor, hovcolor=hovcolor)
