from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.exceptions import BadRequest, NotFound, InternalServerError
from werkzeug import exceptions
from controllers import shows
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db = SQLAlchemy(app)
db.init_app(app)

with app.app_context():
    class shows(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(80), nullable=False)
        seasons = db.Column(db.Integer, nullable=False)

    GOT = shows(
        name = "Hoyse of the Dragon",
        seasons = 8,
    )
    db.create_all()
    db.session.add(GOT)
    db.session.commit()


@app.route('/')
def hello():
    return jsonify({'message': 'Hello from Flask!'}), 200


@app.route('/shows', methods=["GET"])
def shows_handler():
    fns = {
        "GET":index,
    }
    resp, code = fns[request.method](request)
    return jsonify(resp), code 

def index(req):
    return db.session.execute(db.select(shows)).one()
    # return [show for show in tv_shows], 200


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

@app.errorhandler(exceptions.BadRequest)
def handle_400(err):
    return {'message': f'Oops! {err}'}, 400

@app.errorhandler(InternalServerError)
def handle500(err):
    return jsonify({'message': "It's not you, it's us"}), 500


if __name__ == "__main__":
    app.run(debug=True)
