from flask import Blueprint

main = Blueprint('main', __name__)

# Import routes later
from app.main import routes
