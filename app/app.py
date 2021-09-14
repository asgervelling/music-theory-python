from flask import Flask, json, jsonify
from markupsafe import escape

from app.chords import *

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Go to /chords/<chord_notation>'


@app.route('/chords/<chord_notation>/degrees', methods=['GET'])
def chord_notation(chord_notation):
    return jsonify(degrees(escape(chord_notation)))


@app.route('/chords/<chord_notation>/midi')
def midi(chord_notation):
    return jsonify(midi_chord(escape(chord_notation)))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
