import uuid
import logging

from flask import make_response, jsonify
from http import HTTPStatus
from services.storage_service import StorageServiceException, writeImage,getImageDimensions,loadStoredImageNames

def writeImageData(imageStream):
    try:
        id = writeImage(imageStream)
        return make_response({'íd':id,'message' : 'Saved Successfully!'}, HTTPStatus.CREATED)
    except StorageServiceException as see:
        return make_response({'message' : see.message}, see.statusCode)
    except Exception as ex:
        logging.error("Internal Server Error {}", ex)
        return make_response({'message' : 'Internal Server Error'}, HTTPStatus.INTERNAL_SERVER_ERROR)
    
def analyseImage(imageId):
    try:
        width,height = getImageDimensions(imageId) 
        return make_response({'id': imageId, 'width':width, 'height':height}, HTTPStatus.OK)
    except StorageServiceException as see:
        return make_response({'message' : see.message}, see.statusCode)
    except Exception as ex:
        logging.error("Internal Server Error {}", ex)
        return make_response({'message' : 'Internal Server Error'}, HTTPStatus.INTERNAL_SERVER_ERROR)

def loadImageNames():
    try:
        imageNames = loadStoredImageNames() 
        return make_response(jsonify(imageNames), HTTPStatus.OK)
    except StorageServiceException as see:
        return make_response({'message' : see.message}, see.statusCode)
    except Exception as ex:
        logging.error("Internal Server Error {}", ex)
        return make_response({'message' : 'Internal Server Error'}, HTTPStatus.INTERNAL_SERVER_ERROR)