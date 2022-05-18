from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('website/index.html')


@app.route('/namecard')
def namecard():
    return render_template('namecard/index.html')


if __name__ == "__main__":
    app.run(debug=True)
