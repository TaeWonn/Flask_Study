from flask import Blueprint, render_template

from app.models import Question

#[1] 블루프린트 생성하기
bp = Blueprint('name', __name__, url_prefix= '/')

@bp.route('/hello')
def hello_pybo():
    return "Hello, Pybo!"

@bp.route('/')
def indx():
    question_list = Question.query.order_by(Question.create_date.desc())
    return render_template('question/question_list.html', question_list=question_list)




