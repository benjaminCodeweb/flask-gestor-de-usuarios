from flask import Blueprint, request, render_template, redirect, url_for, jsonify
from typing import List, Tuple, Any, Dict
from . import db 
from .models import User
from .schemas import  UserCreateSchema
from flask_sqlalchemy import  query

user_bp = Blueprint('user_bp', __name__)

@user_bp.route("/")
def index() -> str:
    users: List[Tuple[Any]] = User.query.all()

    return render_template('index.html', users = users)


@user_bp.route('/users/new')
def new_user_form() -> str:
    return render_template('user_form.html')


@user_bp.route('/users', methods=['POST'])
def create_user() -> str:
    data: Tuple[Any] = request.form

    try: 
        user_data = UserCreateSchema(first_name = data['first_name'], last_name = data ['last_name'], email = data['email'], image_url= str(data ['image_url']))


    except  ValueError as e:
        return jsonify({"error": e}), 400
    
    new_user: User =  User(first_name = data['first_name'], last_name = data ['last_name'], email = data['email'], image_url= str(data ['image_url']))

    db.session.add(new_user) 
    db.session.commit()

    return render_template('user_item.html', user= new_user)
#esto es para editar el user


#esto es para eliminar el user
@user_bp.route('/users/<int:user_id>/edit')
def edit_user_form(user_id: int) -> str:
    user: User = User.query.get_or_404(user_id)
    return render_template('user_item.html', user = user ) 

@user_bp.route('/users/<int:user_id>', methods = ['DELETE'])
def delete_user(user_id: int) -> str:
        user: User = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()

        users: List[Tuple[Any]] = User.query.all()

        return render_template('index_html', users= users)