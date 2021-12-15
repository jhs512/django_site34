# 가정
- 프로젝트 : site45
- 리포지터리 : https://github.com/jhs512/django_site34
- DB : site34
- DBMS ID : sbsst
- DBMS PW : sbs123414
- 장고 superuser 아이디 : admin
- 장고 superuser 이메일 : 없음
- 장고 superuser 비번 : 1234

# 커밋

## 커밋 1
- 아나콘다 설치
- 파이참 설치
  - 참고 : [https://wiken.io/ken/2377](https://wiken.io/ken/2377)
- 파이참 프로젝트 생성
- 터미널 켜기
- pip install Django
- pip install djangorestframework
- pip install mysqlclient
- .gitignore 파일생성
  - https://www.toptal.com/developers/gitignore/api/pycharm,django

## 커밋 2
- mysql로 DB 변경
- 터미널 열기
- python manage.py runserver
  - 끄기 : Ctrl + C

## 커밋 3
- 언어, 시간대 변경

## 커밋 4
- python manage.py migrate
- python manage.py createsuperuser
  - 아이디 : admin
  - 이메일 : 없음
  - 비번 : 1234