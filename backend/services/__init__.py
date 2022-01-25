import os

WRITE_BUFFER_LENGTH = 1024 * 1024
STORAGE_PATH = os.getenv('STORAGE_ROOT','/srv/aigecko')
os.makedirs(STORAGE_PATH, exist_ok= True)