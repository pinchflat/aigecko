import io
from flask import Blueprint, request
from controllers.image_controller import writeImageData,analyseImage,loadImageNames

image_route = Blueprint('image_route', __name__)

@image_route.route("/upload_image", methods=['POST'])
def upload_image():
    return writeImageData(request.stream)

@image_route.route("/analyse_image/<id>", methods=['GET'])
def analyse_image(id):
    return analyseImage(id)

@image_route.route("/list_images", methods=['GET'])
def list_images():
    return loadImageNames()

