from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    app.config.from_object(config)

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)

    from . import models

    # 플라스크 앱 생성시 블루프린터 적용하기
    from .views import main_views
    app.register_blueprint(main_views.bp)
    
    return app












"""
├── pybo/
│      ├─ __init__.py
│      ├─ models.py
│      ├─ forms.py
│      ├─ views/
│      │   └─ main_views.py
│      ├─ static/
│      │   └─ style.css
│      └─ templates/
│            └─ index.html
└── config.py

데이터베이스를 처리하는 models.py 파일
    파이보 프로젝트는 ORM(object relational mapping)을 지원하는 파이썬 데이터베이스 도구인 SQLAlchemy를 사용한다. 
    SQLAlchemy는 모델 기반으로 데이터베이스를 처리한다. 
    지금은 모델 기반으로 데이터베이스를 처리한다는 말이 이해되지 않겠지만, 
    이후 프로젝트를 진행하면 잘 알 수 있을 것이다. 
    아무튼 지금 여러분이 알아야 할 내용은 파이보 프로젝트에는 
    ‘모델 클래스들을 정의할 models.py 파일이 필요하다’는 것이다.

서버로 전송된 폼을 처리하는 forms.py 파일
    파이보 프로젝트는 웹 브라우저에서 서버로 전송된 폼을 처리할 때 WTForms라는 라이브러리를 사용한다. 
    WTForms 역시 모델 기반으로 폼을 처리한다. 
    그래서 폼 클래스를 정의할 forms.py 파일이 필요하다.

화면을 구성하는 views 디렉터리
    pybo.py 파일에 작성했던 hello_pybo 함수의 역할은 화면 구성이었다. 
    views 디렉터리에는 바로 이런 함수들이 작성된 여러 가지 뷰 파일을 저장한다. 
    파이보 프로젝트에는 기능에 따라 main_views.py, question_views.py, answer_views.py 등 
    여러 가지 뷰 파일을 만들 것이다.

CSS, 자바스크립트, 이미지 파일을 저장하는 static 디렉터리
    static 디렉터리는 파이보 프로젝트의 
    스타일시트(.css), 자바스크립트(.js) 그리고 이미지 파일(.jpg, .png) 등을 저장한다.

HTML 파일을 저장하는 templates 디렉터리
    templates 디렉터리에는 파이보의 질문 목록 조회, 
    질문 상세 조회 등의 HTML 파일을 저장한다. 
    앞에서 살펴본 파이보 프로젝트 구조에는 index.html 파일만 있다. 
    하지만 파이보 프로젝트가 진행되면서 question_list.html, 
    question_detail.html과 같은 템플릿 파일을 계속 추가할 것이다.

파이보 프로젝트를 설정하는 config.py 파일
    config.py 파일은 파이보 프로젝트를 설정한다. 
    파이보 프로젝트의 환경변수, 데이터베이스 등의 설정을 이 파일에 저장한다.
"""