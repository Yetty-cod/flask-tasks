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


@app.route('/list_prof/<list>')
def prof_list(list):
    '''Страница со списком профессий'''
    prof = ['Инструктор по туризму', 'Бортпроводник', 'Сотрудник круизного лайнера', 'Парфюмер',
            'Модель', 'Шоколатье', 'Уборщик мест преступлений', 'Психолог домашних животных',
            'Частный сыровар', 'Пилот воздушного шара']
    return render_template('prof_list.html', prof=prof, list=list)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    '''Страница с заполненной анкетой'''
    fields = {'Name': 'Vasya', 'Surname': 'Pupkin', 'Age': 147, 'Education': 'Not bad, not good',
              'Motivation': 'I love red:/', 'Sex': 'Male', 'Profession': 'Engineer',
              'Ready to stay on Mars': 'I\'ll think..'}
    return render_template('auto_answer.html', fields=fields)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')