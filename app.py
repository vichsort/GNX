from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/home')
def red_home():
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
