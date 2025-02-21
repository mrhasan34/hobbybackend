from flask import Blueprint, request, jsonify
from app.services.text_service import save_text, get_user_texts

text_bp = Blueprint('text', __name__)

@text_bp.route('/texts', methods=['POST'])
def add_text():
    data = request.get_json()
    new_text = save_text(data['content'], data['user_id'])
    return jsonify({"id": new_text.id, "content": new_text.content}), 201

@text_bp.route('/users/<int:user_id>/texts', methods=['GET'])
def get_texts(user_id):
    texts = get_user_texts(user_id)
    return jsonify([{"id": t.id, "content": t.content} for t in texts]), 200