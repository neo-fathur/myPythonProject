from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def generate_password(length=12, use_digits=True, use_special=True):
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

@app.route('/', methods=['GET', 'POST'])
def index():
    password = ""
    if request.method == 'POST':
        length = int(request.form.get('length', 12))
        use_digits = 'digits' in request.form
        use_special = 'special' in request.form
        password = generate_password(length, use_digits, use_special)
    
    return render_template('password.html', password=password)

if __name__ == '__main__':
    app.run(debug=True)
