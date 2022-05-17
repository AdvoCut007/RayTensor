from flask import *
from raytensor import RayTensor

app = Flask(__name__)
neural = RayTensor()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/xray-scan')
def xray_scan():
    return redirect('/in_development')


@app.route('/ct-scan')
def ct_scan():
    return redirect('/in_development')


@app.route('/about')
def about():
    return redirect('/in_development')


@app.route('/in_development')
def dev():
    return render_template('in_development.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

# TODO: Связка с RayTensor, Доработка HTML, JS по возможности.
