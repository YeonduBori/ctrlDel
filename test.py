import pymysql
from flask import Flask, redirect, url_for, request, render_template, request, Response
from flask_ngrok import run_with_ngrok
conn = pymysql.connect(host='localhost', user='root', password='171004', db='mydb', charset='utf8')
curs = conn.cursor()
# sql = "select * from student;"
# curs.execute(sql)
# data = curs.fetchall()
# #데이터 삽입작업
# sql = "INSERT into user values ('dongho', '171004', '언행일치');"
# curs.execute(sql)
# sql = "INSERT into workList values ('dongho', '게임플레이고민', '2019-12-14');"
# curs.execute(sql)
# sql = "select * from user;"
# curs.execute(sql)
# user_data = curs.fetchall()
# sql = "select * from workList;"
# curs.execute(sql)
# todo_list = curs.fetchall()
#debug 용 fetch 출력
# for idx in user_data:
#     print(idx)
# for idx in todo_list:
#     print(idx)
# Flask 객체를 생성하고 그 이름을 app 으로 설정
app = Flask(__name__)
run_with_ngrok(app)
id = 'test'
passwd = 'testing'


@app.route('/', methods=['GET', 'POST'])
def page_main():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    user_id = request.form['id']
    user_pass = request.form['pass']
    user_team = user_team_search(user_id)
    todo_list = user_todo(user_team)
    if user_checking(user_id, user_pass):
        return render_template('debug_todo.html', user_id=user_id, user_team=user_team, todo_list=todo_list)
    else:
        return Response('로그인 실패!', status=404)


@app.route('/register', methods=['GET', 'POST'])
def register():
    # user_id = request.form['id']
    # user_pass = request.form['pass']
    # # user_pass_re = request.form['pass_re']
    # user_team = request.form['team']
    # sql = "select id from user where id = '" + user_id + "';"
    # if curs.execute(sql) == 0 and user_id:
    #     sql = "INSERT INTO user values('" + user_id + "', '" + user_pass + "', '" + user_team + "');"
    #     curs.execute(sql)
    #     conn.commit()
    #     return redirect('/')
    # else:
    return render_template('debug_register.html')


@app.route('/register_check', methods=['GET', 'POST'])
def register_check():
    user_id = request.form['id']
    user_pass = request.form['pass']
    user_pass_re = request.form['pass_re']
    user_team = request.form['team']
    sql = "select id from user where id = '" + user_id + "';"
    result_query = curs.execute(sql)
    if result_query == 0 and user_pass_re is user_pass:
        sql = "INSERT INTO user values('" + user_id + "', '" + user_pass + "', '" + user_team + "');"
        curs.execute(sql)
        conn.commit()
        return redirect('/')
    elif result_query == 1:
        error_msg = "이미 존재하는 아이디입니다."
        return render_template('debug_register.html', pass_error=error_msg)
    elif user_pass is not user_pass_re:
        error_msg = "비밀번호와 확인이 다릅니다."
        return render_template('debug_register.html', pass_error=error_msg)


def user_checking(userID, userPass):
    loginOK = False
    sql = "select id from user where id = '" + userID + "';"
    if curs.execute(sql) == 1:
        sql = "select password from user where password = '" + userPass + "';"
        if curs.execute(sql) == 1:
            loginOK = True
    return loginOK


def user_team_search(userID):
    sql = "select team from user where id = '" + userID + "';"
    if curs.execute(sql) == 1:
        team_name = curs.fetchone()
        return team_name[0]


def user_todo(user_team):
    sql = "select * from workList where team = '" + user_team + "';"
    if curs.execute(sql) == 1:
        user_team = curs.fetchall()
        return user_team


app.run()



# sql = "select id from user where id = 'dongho5309';"
# curs.execute(sql)
# print(curs.fetchone())
# print(type(curs.fetchone()))
# sql = "select password from user where password = '5309';"
# curs.execute(sql)
# print(curs.fetchall())
# print(type(curs.fetchall())