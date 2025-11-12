from flask import Flask, render_template, redirect, session, flash
import random

app = Flask(__name__)
app.secret_key = "123"

@app.route('/', methods=["GET"])
def home():
    return render_template('index.html')

# get session cookie
@app.route('/login', methods=['POST'])
def login():
    session['user']='Demo'
    session['account'] = random.randint(1000, 9999)
    session['balance'] = random.randint(1111,9999)
    return redirect('/myaccount')

@app.route('/myaccount', methods=['GET'])
def myaccount():
    if 'user' in session:
        return render_template('myaccount.html', account=session.get('account'), balance=session.get('balance'))
    else:
        return redirect('/')

@app.route('/transfer', methods=['POST'])
def transfer():
    if 'user' in session:
        if session.get('balance')>=1000:
            session['balance']-=1000
        else:
            flash('Insufficient balance. Minimum required is $1000.')
    else:
        return redirect('/')
    return redirect('/myaccount')

@app.route('/delete', methods=['GET'])
def delete():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000, debug=True)