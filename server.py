import os
from bottle import Bottle, run, route

from http import HTTPStatus

from bottle import HTTPError
from bottle import HTTPResponse

import env

import sentry_sdk
from bottle import Bottle, run
from sentry_sdk.integrations.bottle import BottleIntegration

# Укажите в файле env.py адрес DSN Sentry со своего аккаунта
sentry_sdk.init(dsn=env.SENTRY_DSN,
                integrations=[BottleIntegration()])

@route("/")
def hello():
    html = """
        <!doctype html>
        <html lang="en">
          <head>
            <title>Модуль D2</title>
          </head>
          <body>
            <h1>Домашнее задание D2.10</h1>
            <p class="small">пожалуйста, перейдите по <a href="/success">"/success"</a> или <a href="/fail">"/fail"</a></p>
          </body>
        </html>
        """
    return html

@route("/success")
def success():
    #raise HTTPResponse(status=HTTPStatus.OK)
    html = """
        <!doctype html>
        <html lang="en">
          <head>
            <title>Модуль D2</title>
          </head>
          <body>
            <h1>HTTPStatus.OK</h1>
          </body>
        </html>
        """
    return html 

@route("/fail")
def fail():
    raise RuntimeError("Ошибка! Вы зашли на fail!")  
    return


if os.environ.get("APP_LOCATION") == "heroku":
    run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        server="gunicorn",
        workers=3,
    )
else:
    run(host="localhost", port=8080)