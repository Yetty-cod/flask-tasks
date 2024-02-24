from flask import Flask, render_template


app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def main_page(title):
    '''Главная страница'''
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def profession(prof):
    '''Страница с профессией'''
    return render_template('index.html', prof=prof)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')