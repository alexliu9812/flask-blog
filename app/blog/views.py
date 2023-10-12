from flask import Blueprint

bp = Blueprint("blog", __name__, url_prefix="/blog")
# The url_prefix will be prepended to all the URLs associated with the blueprint.

@bp.route("index/")
def index():
    return 'Hello World!'