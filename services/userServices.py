from sqlalchemy.orm import Session
from database import db
from models.userModels import User
from sqlalchemy import select
from flask import jsonify
from werkzeug.security import generate_password_hash
from models.roleModels import Role, UserManagment
from middleware.userSchema import user_schema, users_schema
from utils.util import encode_token



def check_username(username):
    with Session(db.engine) as session:
        with session.begin():
            user = session.execute(select(User).where(User.username == username)).scalars().first()
            return user is None
        
def check_roles(roles):
    with Session(db.engine) as session:
        with session.begin():
            set_roles = set(session.execute(select(Role.role_name)).scalars().all())
            return all(role in set_roles for role in roles)

def create(user_data):
    with Session(db.engine) as session:
        with session.begin():
            if not check_username(user_data['username']):
                return jsonify({
                    "status":"BAD",
                    "message":"username exists"
                }), 400
            if not check_roles(user_data['roles']):
                return jsonify({
                    "status":"BAD",
                    "message":"one or more roles are not valid"
                }), 400
            else:
                roles = session.execute(select(Role).where(Role.role_name.in_(user_data['roles']))).scalars().all()

                new_user = User(
                    name=user_data['name'],
                    username=user_data['username'],
                    roles = roles,
                    hashed_pass = generate_password_hash(user_data['password'])
                                )
                session.add(new_user)
                session.commit()
                return jsonify({
                    "status":"OK",
                    "message":"user added"
                }), 200
            
def edit(user_data):
    with Session(db.engine) as session:
        with session.begin():
            if not check_roles(user_data['roles']):
                return jsonify({
                    "status":"BAD",
                    "message":"one or more roles are not valid"
                }), 400
            user = session.get(User,user_data['id'])
            if not user:
                return jsonify({
                    "status":"BAD",
                    "message":"user not found"
                }), 404
            user.username = user_data['username']
            user.roles = user_data['roles']
            user.name = user_data['name']
            user.hashed_pass = generate_password_hash(user_data['password'])
            session.commit()
            return jsonify({
                    "status":"OK",
                    "message":"user updated"
                }), 200
        
def remove(user_id):
    with Session(db.engine) as session:
        with session.begin():
            user = session.get(User,user_id)
            if user:

                session.delete(user)
                session.commit()
                return jsonify({
                    "status":"OK",
                    "message":"user deleted"
                }), 200
            return jsonify({
                    "status":"BAD",
                    "message":"product not found"
                }), 200

def get_one(user_id):
    with Session(db.engine) as session:
        with session.begin():
            user = session.get(User, user_id)
            if user:
                return user_schema.jsonify(user)
            else:
                return jsonify({
                    "status":"BAD",
                    "message":"user not found"
                }), 404

def get_all():
    with Session(db.engine) as session:
        with session.begin():
            users = session.execute(select(User)).scalars().all()
            return users_schema.jsonify(users)
    

def login(user_data):
    with Session(db.engine) as session:
        with session.begin():
            user = session.execute(select(User).where(User.username == user_data['username'])).scalars().first()
            roles = [role.role_name for role in user.roles]
            print(roles)
            if user:
                if user.check_password(user_data['password']):
                    return jsonify({
                        "status":"OK",
                        "message":"Login Successfull",
                        "auth_token":encode_token(user.id,roles)
                    })
                else:
                    return jsonify({
                        "status":"BAD",
                        "message":"Invalid Password"
                    }), 401
            else: 
                return jsonify({
                    "status":"BAD",
                    "message":"User not Found"
                }), 400
            

    