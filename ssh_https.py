from os import *
from flask import Flask, Response

a = Flask(__name__)

def terminal(texted):
    with popen(texted) as stream:  # Используем with для автоматического закрытия
        for line in stream:
                yield f"data: {line.strip()}\n\n"
                # Форматируем как SSE

@a.route("/")

def started():
    return "localhost@root: "

@a.route("/<m>")

def m1(m):
    return Response(terminal(m), content_type="text/event-stream")
    
if __name__ == "__main__":
    a.run(host="0.0.0.0")
