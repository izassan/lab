import logging, os
from logging import getLogger
from logging import StreamHandler, FileHandler

logger = getLogger(__name__)
logger.setLevel(logging.DEBUG)

st_handler = StreamHandler()
st_handler.setLevel(logging.INFO)

if os.name == 'nt':
    current_dir = os.getenv('USERPROFILE').replace(os.sep, '/')
else:
    current_dir = os.getenv('HOME')
fl_handler = FileHandler(filename=f"{current_dir}/logtest.log", encoding="utf-8")
fl_handler.setFormatter
fl_handler.setLevel(logging.DEBUG)

logger.addHandler(st_handler)
# logger.addHandler(fl_handler)
