# ctrlDel
contributors: @pongsoyun, @YeondubBori

# Introduce Our Services
- 회원별 데이터를 개별로 관리합니다.
- 협업시 하나의 팀 내의 to do list를 관리하는 툴을 개발합니다.
- 팀 별로 to do list가 다르게 보입니다. 
- 해당하는 팀의 할일만 볼 수 있습니다. 
- 해야 할 일(to do list)을 각각의 사용자에게 할당할 수 있습니다.  



# Setting
아래의 셋팅은 최소 셋팅이며, mac에 최적화 되어있습니다. 

```
// 1. install pip
sudo easy_install pip

// 2. install Flask
pip install Flask

// 3. install ngrok
pip install flask-ngrok
ngrok http 8080

// 4. run python3
python3 test.py
```

# API 문서

## def user_checking(userID, userPass)
유저 아이디, 유저 패스워드를 매개변수로 db에 존재하면 true 리턴 틀리면 false 리턴

## def user_team_search(userID)
유저 아이디를 넣어주면 유저의 팀을 리턴하는 함수입니다. todoList를 보여주기 위함.

## def user_todo(user_team)
유저의 팀을 넣어주면 할일 테이블에서 팀으로 셀렉트하여 리스트로 리턴해줍니다.


