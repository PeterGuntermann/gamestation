from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# bottom import = workaround to circular imports
from app import routes
