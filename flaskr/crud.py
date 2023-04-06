from model import User, Admin, Animal

"""Admins"""


"""Users"""

def get_user_by_id(user_id):
    return User.query.filter_by(id=user_id).first()

"""Animals"""