from flask import Flask, render_template
from markupsafe import escape

from app.chords import *

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Go to /chords/<chord_notation>'


@app.route('/chords/<chord_notation>', methods=['GET'])
def chord_notation(chord_notation):
    context = {
        'chord_notation': escape(chord_notation),
        'chord_degrees': degrees(escape(chord_notation)),
    }
    return render_template('chord.html',
                           chord_notation=escape(chord_notation),
                           chord_degrees=degrees(escape(chord_notation)))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
