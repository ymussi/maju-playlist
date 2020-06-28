from maju.api import api
from maju.config import config_db
from maju.api.healthcheck.view import ns as healthcheck
from maju.api.playlist.view import ns as playlist
from maju.api.statistics.view import ns as statistics
from flask import Flask, Blueprint
from flask_cors import CORS


def create_app(config_filename=None):
    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": "*"}})

    connect_string = config_db()['database_uri']
    app.config['SQLALCHEMY_DATABASE_URI'] = connect_string
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['RESTPLUS_VALIDATE'] = True
    app.config['RESTPLUS_MASK_SWAGGER'] = False

    blueprint = Blueprint('login', __name__)
    api.init_app(blueprint)
    api.add_namespace(healthcheck, "/healthcheck")
    api.add_namespace(playlist, "/playlist")
    api.add_namespace(statistics, "/statistics")

    app.register_blueprint(blueprint)
    app.teardown_appcontext(shutdown_session)
    return app

def shutdown_session(exception=None):
    from maju.database import session
    session.remove()