import secrets
from datetime import datetime

from app import app


def req_handler(request, path):
    """
    Функция обработки запросов, всех, для создания всех логов
    """
    # Эта штука создает метку события, по которой его можно однозначно идентифицировать
    req_stamp = f'{request.method}_{secrets.token_hex(5)}_{str(datetime.now())}'

    log_msg_creator(req_stamp, request.method, path)

    # Проверка на метод запроса
    if request.method != 'GET':
        log_msg_creator(req_stamp, request.method, path, err_msg=True, err_type='Method error')

    # Проверка на путь
    if path != 'api':
        log_msg_creator(req_stamp, request.method, path, err_msg=True, err_type='Path error')

    # Распаковка параметров
    param_lst = []
    for key, value in request.args.items():
        param_lst.append((key, value))

    # Проверка на параметры
    if param_lst:
        log_msg_creator(req_stamp, request.method, path, err_msg=True, err_type='Parameter error', param_lst=param_lst)


def log_msg_creator(req_stamp, method, path, err_msg=False, err_type=None, param_lst=None):
    """
    Функция записи лога в файл
    :param req_stamp: Метка запроса
    :param path: Путь запроса
    :param err_msg: Это лог ошибки или нет
    :param err_type: Тип ошибки если это лог ошибки
    :param param_lst: Список параметров запроса
    """

    msg = f'Request stamp:{req_stamp}\n' \
          f'Method:{method}\n' \
          f'Path:{path}\n'

    msg_param = 'Params:\n'

    if param_lst:
        for item in param_lst:
            msg_param += f'{item[0]}\n'

    if err_msg:
        msg_err = f'Type error:{err_type}\n'
        msg_result = f'{msg}{msg_err}{msg_param}'
        app.logger.error(msg_result)
    else:
        msg_result = f'{msg}{msg_param}'
        app.logger.info(msg_result)
