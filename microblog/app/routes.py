# routes are different url's that the application implements.
# In flask, handlers for application routes are written as python functions, called view functions
# view functions are mapped to one or more route URL's so that flask knows what logic to execute when a client requests a specific URL

from app import app

@app.route("/")
@app.route("/index")
def index():
    user = {"username": "miguel"}
    return """
<html>
    <head>
        <title>Home page - Microblog</title>
    </head>
    <body>
        <h1>Hello, """ + user["username"] + """!</h1>
    </body>
</html>"""

# we want to expand the view function to show a complete HTML page.