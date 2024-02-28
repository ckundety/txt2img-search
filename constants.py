import os

QDRANT_URL = os.environ.get('QDRANT_URL', 'localhost:6333')
QDRANT_COLLECTION = os.environ.get('QDRANT_COLLECTION', 'advert_captions')
