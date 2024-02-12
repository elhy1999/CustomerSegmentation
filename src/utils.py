import os

REPO_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__))).replace("\\", "/")
DATA_PATH = os.path.join(REPO_PATH, "data")
MODELS_PATH = os.path.join(REPO_PATH, "models")
SRC_PATH = os.path.join(REPO_PATH, "src")
NOTEBOOKS_PATH = os.path.join(REPO_PATH, "notebooks")