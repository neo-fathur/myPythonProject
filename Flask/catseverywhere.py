from flask import Flask, render_template, request, redirect, g
import sqlite3
app = Flask(__name__)   # Create a new instance of the Flask class

@app.before_request
def before_request():
    g.db = sqlite3.connect("emails.db")

email_addresses = []

@app.route('/')         # Define the route for the URL / and bind it to the function hello_world
def hello_world():
    author = "Me"
    name = "You"
    return render_template('index.html', author=author, name=name)

@app.route('/signup', methods = ['POST'])
def signup():
    email = request.form['email']
    #print("The email address is '" + email + "'")
    #email_addresses.append(email)
    #print(email_addresses) 
    g.db.execute("INSERT INTO email_addresses VALUES (?)", [email])
    g.db.commit()
    return redirect('/')

@app.route('/emails.html')
def emails():
    email_addresses = g.db.execute("SELECT email FROM email_addresses").fetchall()
    return render_template('emails.html', email_addresses=email_addresses)

@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()

if __name__ == "__main__":  # If the script is executed, then run the app
    app.run()            # Start the server