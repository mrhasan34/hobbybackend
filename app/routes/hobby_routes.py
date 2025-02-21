from flask import Blueprint, jsonify
from ..services.hobby_service import get_all_hobbies

hobby_bp = Blueprint('hobby', __name__)

@hobby_bp.route('/hobbies', methods=['GET'])
def get_hobbies():
    hobbies = get_all_hobbies()
    return jsonify(hobbies)