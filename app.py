from flask import Flask, render_template
from collections import namedtuple

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/test')
def test():
    return render_template("layout.html", \
                           title="hey there", \
                           trims=[{'title': '2018 Chevrolet Tahoe LS',
                                   'content': 'Expect the unexpected with the Chevy Tahoe LS. This base model is packed with advanced technologies and premium amenities that you’re sure to use to your advantage.',
                                   'trim list': ['5.3L EcoTec3 V8 engine', 'Premium Smooth Ride suspension',
                                                 '6-speed automatic transmission']},
                                  {'title': '2018 Chevrolet Tahoe LT',
                                   'content': 'Expect even more advanced features with the 2018 Chevy Tahoe LT, including an upgraded sound system and a driver-assist system. The Tahoe LT includes many Tahoe LS features, plus:',
                                   'trim list': ['Rear Vision Camera', 'Rear Vision Camera',
                                                 '4.2-in. multi-color driver information center']}])

    if __name__ == '__main__':
        app.run(FLASK_DEBUG=True)
