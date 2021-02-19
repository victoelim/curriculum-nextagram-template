from flask import Blueprint, render_template, request, redirect, url_for
from models.user import User


users_blueprint = Blueprint('users',
                            __name__,
                            template_folder='templates')


@users_blueprint.route('/new', methods=['GET'])
def new():
    return render_template('users/new.html')


@users_blueprint.route('/', methods=['POST'])
def create():
    name = request.form.get('name')
    number = request.form.get('number')
    user = User(name = name, number = number)

    if user.save():
        return redirect(url_for('users.new'))
    else: 
        return "Something went wrong. Please try again."