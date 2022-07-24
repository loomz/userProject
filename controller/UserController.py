from bottle import get, post, put, delete, request
import json

from model.User import User


# 根据id 查询用户信息
@get('/user/<id>')
def getUser(id):
    print('getUser id=%s' % id)
    user = User(1, 'loomz', 36, "男", "1986-05-11")

    # 将class对象转为json字符串
    # 方法一，直接使用系统的dict函数，简单
    print(user.__dict__)
    return {'code': 0, 'msg': 'success', 'data': user.__dict__}

    # 方法二：使用json，相对复杂一些
    # userJsonString = json.dumps(u1, default=lambda o: o.__dict__, ensure_ascii=False)
    # print('result=%s' % userJsonString)
    # return {'code': 0, 'msg': 'success', 'data': userJsonString}
    # return {'code': 0, 'msg': 'success', 'data': '{id:1,name:"loomz",age:36,sex:"男", address:"shenzhen"}'}


# 创建一个新的用户
@post('/user')
def createUser():
    requestJson = request.json

    name = requestJson['name']
    age = requestJson['age']
    sex = requestJson['sex']
    birth = requestJson['birth']

    user = User(None, name, age, sex, birth)

    print("createUser user=%s" % user.__dict__)

    return {'code': 0, 'msg': 'success', 'data': 1}


@put('/user/<id>')
def updateUser(id):
    print('updateUser id=%s' % id)

    requestJson = request.json

    name = requestJson['name']
    birth = requestJson['birth']

    print("id=%s name=%s birth=%s" % (id, name, birth))

    return {'code': 0, 'msg': 'success', 'data': 1}


@delete('/user/<id>')
def deleteUser(id):
    print('deleteUser id=%s' % id)
    return {'code': 0, 'msg': 'success', 'data': id}

