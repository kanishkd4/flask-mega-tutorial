# routes are different url's that the application implements.
# In flask, handlers for application routes are written as python functions, called view functions
# view functions are mapped to one or more route URL's so that flask knows what logic to execute when a client requests a specific URL

from app import app

@app.route("/")
@app.route("/index")
def index():
    return "Hello, world"

