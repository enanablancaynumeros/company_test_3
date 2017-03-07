from logging import getLogger

from flask import Flask, jsonify
from flask_script import Manager


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = b'5DXKI52PTJJJ2ZHWJR5VQQZHRYD4CXLNFIXQ15L2RB30FV02FN'
    new_manager = Manager(app)
    return app, new_manager


def init_app(app):
    register_general_endpoints(app)
    handler = getLogger("werkzeug")
    app.logger.addHandler(handler)


def register_general_endpoints(app):
    @app.route("/_internal_/health")
    def flask_api_health():
        return jsonify(msg="ok")

    from api.apps.gender_app import gender_app
    app.register_blueprint(gender_app, url_prefix='/')
