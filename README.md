# ctrlDel
contributors: @pongsoyun, @YeondubBori

# Introduce Our Services
- 회원별 데이터를 개별로 관리합니다.
- 협업시 하나의 팀 내의 to do list를 관리하는 툴을 개발합니다.
- 팀 별로 to do list가 다르게 보입니다. 
- 해당하는 팀의 할일만 볼 수 있습니다. 
- 해야 할 일(to do list)을 각각의 사용자에게 할당할 수 있습니다.  



# Setting
아래의 셋팅은 최소 셋팅입니다.

```
// 1. install pip
sudo easy_install pip

// 2. pyMySQL install
python3 -m pip install PyMySQL

// 3. install Flask
pip install Flask

// 4. install ngrok
pip install flask-ngrok
ngrok http 8080

// 5. run python3
python3 test.py
```
맥OS version
```
Python 2.7.10
Flask 1.1.1
Werkzeug 0.16.0
```

윈도우 version
```
Flask 1.0.2
Python 3.6.7
```
# API 문서

## def user_checking(userID, userPass)
유저 아이디, 유저 패스워드를 매개변수로 db에 존재하면 true 리턴 틀리면 false 리턴

## def user_team_search(userID)
유저 아이디를 넣어주면 유저의 팀을 리턴하는 함수입니다. todoList를 보여주기 위함.

## def user_todo(user_team)
유저의 팀을 넣어주면 할일 테이블에서 팀으로 셀렉트하여 리스트로 리턴해줍니다.

## def register_check()
회원가입시 이미 가입한 유저인지 확인하고 비밀번호 확인과 비밀번호가 다르면 회원가입이 안되게 해줍니다.
그 경우가 아니여야 회원가입 됩니다.

## def delete_todo(user_id, todo)
할일 리스트에서 할 일을 삭제해주는 함수입니다.

## def lnsert_todo(user_id)
할일 리스트에서 할 일을 추가해주는 함수입니다.

# 추가안내사항
from flask_ngrok import run_with_ngrok
run_with_ngrok(app)
이 코드에 대해서 주석을 삭제해주면 ngrok 간이 서버에 올라갑니다. 
