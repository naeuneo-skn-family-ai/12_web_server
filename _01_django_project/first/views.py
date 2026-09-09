from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world")

def greeting(request):
    return HttpResponse("""
        <h1>침대 ♥️ 나</h1>
        <h3>집에 가시겠습니까?</h3>
        <input type = "radio">네</input>
        <input type = "radio">아니오</input>
        <br></br>
        <button type="button">집에 가는 버튼🏠</button>
    """)

def foo(request):
    return HttpResponse('<h1>🦑Foooooooooooooooooooo🦑</h1>')


def bar(request):
    return HttpResponse('''
    <html>
    <head>
      <title>🐳Bar Page🐳</title>
    </head>
    <body>
      <h1>🐳Bar Page🐳</h1>
      <p>🐳This is a bar page🐳</p>
    </body>
    </html>
    ''')