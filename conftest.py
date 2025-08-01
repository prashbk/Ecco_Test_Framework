import sys
import os

from utils.playwright_utils import *  # This exposes login, page, browser fixtures
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "pages")))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "utils")))