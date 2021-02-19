from flask import Blueprint
from models.user import User

users_api_blueprint = Blueprint('users_api',
                             __name__,
                             template_folder='templates')

@users_api_blueprint.route('/', methods=['GET'])
def index():
    user = User.select()
    return jsonify([{"id": user.id, "name":user.name, "number":user.number} for user in users])

@users_api_blueprint.route('/', methods=['POST'])
def create():
    name = request.json.get('name')
    number = request.json.get('number')
    user = User(name = name, number = number)

    if user.save():
        return jsonify({'id':user.id, 'name':user.name, 'number':user.number, 'message': 'Succesfully posted'})
    else:
        return jsonify({'message': 'Failed to add contact to database'})
