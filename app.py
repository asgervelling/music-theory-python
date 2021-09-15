from flask import Flask, jsonify
from markupsafe import escape

from chords import Chord

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Go to /chords/<chord_notation>'


@app.route('/chords/<chord_notation>/degrees', methods=['GET'])
def chord_degrees(chord_notation):
    chord = Chord(escape(chord_notation))
    return jsonify(chord.degrees)


@app.route('/chords/<chord_notation>/midi')
def midi(chord_notation):
    chord = Chord(escape(chord_notation))
    return jsonify(chord.midi)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
