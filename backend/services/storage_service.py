import imghdr
import os
import stat
from http import HTTPStatus
from uuid import uuid4
from services import STORAGE_PATH,WRITE_BUFFER_LENGTH
from PIL import Image

class StorageServiceException(Exception):
    
    def __init__(self, internal, message):
        self.internal = internal
        self.message = message
        self.statusCode = HTTPStatus.INTERNAL_SERVER_ERROR if self.internal else HTTPStatus.BAD_REQUEST
        super().__init__(self.message)
        
def writeImage(imageStream):
    try:
        imageId = uuid4().hex
        filePath = os.path.join(STORAGE_PATH,imageId)
        flags = os.O_WRONLY | os.O_CREAT | os.O_TRUNC
        mode = stat.S_IRUSR | stat.S_IWUSR
        with os.fdopen(os.open(filePath, flags, mode), 'bw') as img_file:
            b = imageStream.read(WRITE_BUFFER_LENGTH)
            while b:
                img_file.write(b)
                b = imageStream.read(WRITE_BUFFER_LENGTH)
        if (imghdr.what(filePath) is None):
            raise StorageServiceException(False, 'Unsupported image type!')    
        return imageId
    except IOError as err:
        raise StorageServiceException(True, 'Storage error!')

def getImageDimensions(imageId):
    try:
        filePath = os.path.join(STORAGE_PATH,imageId)

        if (os.path.exists(filePath)):
            if (os.path.isfile(filePath)):
                return Image.open(filePath).size
            else:
                raise StorageServiceException(True, imageId + ' is directory!')        
        else:
            raise StorageServiceException(False, imageId + ' does not exists!')    
    except IOError as err:
        raise StorageServiceException(True, 'Storage error!')

def loadStoredImageNames():
    try:
        return [f for f in os.listdir(STORAGE_PATH) if os.path.isfile(os.path.join(STORAGE_PATH, f))]
    except IOError as err:
        raise StorageServiceException(True, 'Storage error!')