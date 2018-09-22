from flask import Flask, render_template, request
from caesar import encrypt

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
@app.route('/home')
def home():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        return render_template('about.html')

@app.route('/home/about', methods = ['POST'])
def about():
    rot_amount = request.form.get('rotate-by')
    try:
        int(rot_amount)
    except ValueError:
        return "Rotation amount must be an integer."
    new_text = request.form.get('user-submitted-text')
    ##TODO:
    # run caesar algorithm
    encrypted_text = encrypt(new_text, rot_amount)
    # receive back a list|string| whatever you want with the answer
    return render_template('about.html', rot = rot_amount, en_text = encrypted_text)

app.run(debug = True)
