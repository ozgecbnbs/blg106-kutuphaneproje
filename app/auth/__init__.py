from flask import Blueprint

auth = Blueprint('auth', __name__)

# Import routes later
from app.auth import routes
