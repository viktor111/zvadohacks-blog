from flask import Flask, render_template

app = Flask(__name__, static_url_path = '/static')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/articles')
def articles():
    return render_template('articles.html', title='articles')


if __name__ == '__main__':
    app.run(debug=True)