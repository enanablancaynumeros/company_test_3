from db_handlers.handlers import VisitsHandler
from db_handlers.postgres_config import Postgres_DB_Session
from flask import Blueprint, jsonify, request

from db_handlers.utils import get_db_session_scope

gender_app = Blueprint('gender', __name__)


@gender_app.route('', methods=['GET'])
def visits_all(client_id):
    with get_db_session_scope(Postgres_DB_Session) as db_session:
        visits = VisitsHandler(db_session).get_all()
        return jsonify(data=visits)


@gender_app.route('getGender/<int:client_id>/', methods=['GET'])
def gender(client_id):
    heuristic = request.args.get('heuristic', "default")
    gender_predicted = get_gender(heuristic)
    data = {"gender": gender_predicted}
    return jsonify(data=data)


def get_gender(heuristic):
    with get_db_session_scope(Postgres_DB_Session) as db_session:
        visit_handler = VisitsHandler(db_session)
        return "women"
