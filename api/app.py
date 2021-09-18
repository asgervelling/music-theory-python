from json import decoder
from chords import Chord, InvalidChordException
import sys
from werkzeug.exceptions import HTTPException
from markupsafe import escape
from flask_cors import CORS
from flask import Flask, jsonify


app = Flask(__name__)
CORS(app)
cors = CORS(app, resources={
    r"/*": {
        "origins": "*"
    }
})


@app.route('/')
def hello_world():
    return 'Go to /chords/<chord_notation>'


@app.route('/chords/<chord_notation>/degrees', methods=['GET'])
def chord_degrees(chord_notation):
    try:
        chord = Chord(escape(chord_notation))
        return jsonify(chord.degrees)
    except InvalidChordException as e:
        return jsonify({"error": str(e)})


@app.route('/chords/<chord_notation>/midi')
def midi(chord_notation):
    try:
        chord = Chord(escape(chord_notation))
        return jsonify(chord.midi)
    except InvalidChordException as e:
        return jsonify(["error"])


@app.errorhandler(500)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    response = e.get_response()
    return response


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
