from flask import Blueprint
from controllers import idea_controller

ideas_bp = Blueprint('ideas', __name__)

@ideas_bp.route('/')
def index():
    return idea_controller.list_ideas()

@ideas_bp.route('/add', methods=['GET', 'POST'])
def add():
    return idea_controller.add_idea()

@ideas_bp.route('/edit/<int:idea_id>', methods=['GET', 'POST'])
def edit(idea_id):
    return idea_controller.edit_idea(idea_id)

@ideas_bp.route('/delete/<int:idea_id>', methods=['POST'])
def delete(idea_id):
    return idea_controller.delete_idea(idea_id)
