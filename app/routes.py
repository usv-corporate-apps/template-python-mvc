from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, current_app
)
from werkzeug.exceptions import abort

bp = Blueprint('app', __name__)

@bp.route('/')
def index():
    return render_template('app/index.html')

