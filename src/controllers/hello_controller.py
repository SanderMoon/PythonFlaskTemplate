"""This is an example controller for flask, which sets a blueprint for flask to use.

Returns:
    Blueprint: A blueprint for flask to use.
"""

from flask import Blueprint, jsonify

hello_blueprint = Blueprint("hello", __name__)


@hello_blueprint.route("/hello", methods=["GET"])
def hello_world():
    """Exposes a simple hello world endpoint.

    Returns:
        Response: A response object with a message ("hello world") and status code.
    """
    return jsonify(message="Hello world"), 200
