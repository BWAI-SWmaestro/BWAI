'''
BWAI V1 API Module Package
'''
from flask import Blueprint

bwai_v1 = Blueprint('bwai_v1', __name__)

from . import bwai, label, dashboard
