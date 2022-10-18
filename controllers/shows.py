from werkzeug.exceptions import BadRequest

tv_shows = [
    {'id': 1, 'name': 'Game Of Thrones', 'seasons': 8},
    {'id': 2, 'name': 'House Of The Dragon', 'seasons' : 1},
    {'id': 3, 'name': 'The Boys', 'seasons': 3},
    {'id': 4, 'name': 'Breaking Bad', 'seasons' : 5},
    {'id': 5, 'name': 'Mr Robot', 'seasons' : 4}
]

def index(req):
    # db.session.execute(db.select('SELECT * FROM SHOWS'))
    return [show for show in tv_shows], 200

def show(req, id):
    return find_by_id(id), 200

def create(req):
    new_show = req.get_json()
    new_show['id'] = sorted([show['id'] for show in tv_shows])[-1] + 1
    tv_shows.append(new_show)
    return new_show, 201

def update(req, id):
    show = find_by_id(id)
    data = req.get_json()
    print(data)
    for key, val in data.items():
        show[key] = val
    return show, 200

def destroy(req, id):
    show = find_by_id(id)
    tv_shows.remove(show)
    return show, 204

def find_by_id(id):
    try:
        # db.session.execute(db.select('SELECT * FROM SHOWS'))
        return next(show for show in tv_shows if show['id'] == id)
    except:
        raise BadRequest(f"We don't have that show with id {id}!")
