from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.exceptions import BadRequest, NotFound, InternalServerError
from controllers import shows

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello():
    return f"Welcome to Flask!",200


@app.route('/shows', methods=["GET", "POST"])
def shows_handler():
    fns = {
        "GET":shows.index,
        "POST":shows.create
    }
    resp, code = fns[request.method](request)
    return jsonify(resp), code 


@app.route('/shows/<int:shows_id>', methods=["GET", "PATCH", "PUT", "DELETE"])
def shows_handler_id(shows_id):
    fns = {
        "GET":shows.show,
        "PATCH":shows.update,
        "PUT":shows.update,
        "DELETE": shows.destroy
    }
    resp, code = fns[request.method](request, shows_id)
    return jsonify(resp), code
    
        


@app.errorhandler(NotFound)
def handle404(err):
    return jsonify({'message': f'oops{err}'}), 404


@app.errorhandler(InternalServerError)
def handle500(err):
    return jsonify({'message': "It's not you, it's us"}), 500


if __name__ == "__main__":
    app.run(debug=True)
