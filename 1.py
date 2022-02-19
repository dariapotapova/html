from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    if 'инженер' in prof.lower() or 'строитель' in prof.lower():
        return render_template('training.html', title='Инженерные тренажеры', image=url_for('static', filename='img/build.png'))
    else:
        return render_template('training.html', title='Научные тренажеры', image=url_for('static', filename='img/science.png'))


@app.route('/list_prof/<condition>')
def prof_list(condition):
    ll = ["инженер-исследователь",
          "пилот",
          "строитель",
          "экзобиолог",
          "врач",
          "инженер по терраформированию",
          "климатолог",
          "специалист по радиационной защите",
          "астрогеолог",
          "гляциолог",
          "инженер жизнеобеспечения",
          "метеоролог",
          "оператор марсохода",
          "киберинженер",
          "штурман",
          "пилот дронов"]
    return render_template('list_pfor.html', title='Список профессий', ll=ll, condition=condition)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')