
from flask import Blueprint, jsonify
from service import get_all_mission

mission = Blueprint('mission', __name__)

#get all mission
@mission.route('/mission', methods=['GET'])
def all_mission():
    result = get_all_mission()
    if result:
        return {'result': result}, 200  # return jsonify(({'result': r})),200
    else:
        return {'result': False}, 400
