from flask import Flask # Import the Flask class from the flask package, making the code available to build web apps with flask.

app = Flask(__name__) # Create an instance of the Flask class and assign it to the variable app. The first argument of the Flask class is the name

@app.route('/') # Use the route() decorator to map the specific URL with the associated function that is intended to perform some task. In this case, the function is triggered when the user accesses the root URL. 
def index(): # The function is given a name which is also used to generate URLs for that particular function, and returns the message we want to display in the user’s browser.
    return 'Web App with Python Flask!' # The message we want to display in the user’s browser

app.run(host='0.0.0.0', port=81) # The run() method of the Flask class runs the application on the local development server. We specify the host and port to run the application on. The host is set to