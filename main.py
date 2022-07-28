from bottle import run, get

from controller import UserController
from controller import CompanyController


@get('/index')
def index():
    return {'code': 0, 'msg': 'welcome index'}


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run(host='localhost', port=8081)
