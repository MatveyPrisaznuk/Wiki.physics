from flask import Flask, render_template, url_for, redirect


app = Flask(__name__)


@app.route('/')
def page():
    return render_template('page.html')

@app.route('/author')
def author():
    return render_template('author.html')


if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0')