from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.exceptions import BadRequest, NotFound, InternalServerError

app = Flask(__name__)
CORS(app)

lizards = [
    {'id': 1, 'name': 'Kommodo Dragon', 'colour': 'Grayish Green'},
    {'id': 2, 'name': 'Iguana', 'colour': 'Yellow'},
    {'id': 3, 'name': 'Chameleon', 'colour': 'Multi'},
    {'id': 4, 'name': 'Plumed Basilisk', 'colour': 'Green'}
]


@app.route('/')
def hello():
    return f"Welcome to Flask!"


@app.route('/lizards', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return jsonify(lizards), 200
    elif request.method == "POST":
        new_lizard = request.json
        last_id = lizards[-1]['id']
        new_lizard['id'] = last_id + 1
        lizards.append(new_lizard)
        return f"{new_lizard['name']} was created", 201


@app.route('/lizards/<int:lizard_id>')
def show(lizard_id):
    try:
        return next(lizard for lizard in lizards if lizard['id'] == lizard_id)
    except:
        raise BadRequest(
            f"Sorry we do not have a lizard of that id: {lizard_id}")


@app.errorhandler(NotFound)
def handle404(err):
    return jsonify({'message': f'oops{err}'}), 404


@app.errorhandler(InternalServerError)
def handle500(err):
    return jsonify({'message': "It's not you, it's us"}), 500


if __name__ == "__main__":
    app.run(debug=True)