from flask import Flask
from config import Config

app = Flask(__name__) # __name__ is a predifined python variable and is set to the name of the module it is used
app.config.from_object(Config)

from app import routes

# there are two entities named app - the folder/package that is app and the variable defined above