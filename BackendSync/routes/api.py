from flask import Blueprint, request, jsonify
from biblioteca216sync.utils.supabase_connector import update_supabase

api_bp = Blueprint('api_bp', __name__)

@api_bp.route('/update', methods=['POST'])
def update():
    data = request.json
    topic = data.get('topic')
    name = data.get('name')
    author = data.get('author')
    
    # Call the function to update Supabase
    result = update_supabase(topic, name, author)
    
    return jsonify(result)
