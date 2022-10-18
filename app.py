from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.exceptions import BadRequest, NotFound, InternalServerError

app = Flask(__name__)
CORS(app)

shows = [
    {'id': 1, 'name': 'Game Of Thrones', 'seasons': 8},
    {'id': 2, 'name': 'House Of The Dragon', 'seasons' : 1},
    {'id': 3, 'name': 'The Boys', 'seasons': 3},
    {'id': 4, 'name': 'Breaking Bad', 'seasons' : 5},
    {'id': 5, 'name': 'Mr Robot', 'seasons' : 4}
]


@app.route('/')
def hello():
    return f"Welcome to Flask!"


@app.route('/shows', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return jsonify(shows), 200
    elif request.method == "POST":
        new_show = request.json
        last_id = shows[-1]['id']
        new_show['id'] = last_id + 1
        shows.append(new_show)
        return f"{new_show['name']} was created", 201


@app.route('/shows/<int:shows_id>')
def show(shows_id):
    try:
        return next(shows for shows in shows if shows['id'] == shows_id)
    except:
        raise BadRequest(
            f"Sorry we do not have a shows of that id: {shows_id}")


@app.errorhandler(NotFound)
def handle404(err):
    return jsonify({'message': f'oops{err}'}), 404


@app.errorhandler(InternalServerError)
def handle500(err):
    return jsonify({'message': "It's not you, it's us"}), 500


if __name__ == "__main__":
    app.run(debug=True)
