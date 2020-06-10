from django.shortcuts import render
import random
from datetime import datetime
# Create your views here.
def index(request):
    return render(request, 'index.html')

def hello(request):
    menu = ['닭갈비', '탕수육', '초밥', '스파게티 돈까스']
    pick = random.choice(menu)
    return render(request, 'hello.html', {'pick':pick})

def name(request):
    my_name = '유명인'
    return render(request, 'name.html', {'my_name':my_name})

def introduce(request) :
    my_info = ['가','나','다','라','마']
    name = '유명인'
    age = 28
    git = 'https://github.com/myomi2767'
    context = {
        'name' : name,
        'age' : age,
        'git' : git
    }
    return render(request, 'introduce.html', context)

def ranName(request):
    random_name=['유명인','김현수','윤소윤','성민재','이영주','김민정']
    pick = random.choice(random_name)
    context = {
        'pick' : pick
    }
    return render(request, 'ranName.html', context)

def yourname(request, name):
    # name = name
    context = {
        'name' : name
    }
    return render(request, 'yourname.html', context)

# Q1. 이름과 나이 받아보기
# 1. 주소창에 이름과 나이(반드시 int)입력
# 1-1. url.py에 경로 설정 시 <> 꺽쇠 형태로 구분하여 표현
# 2. 입력 받은 내용을 페이지에 출력

def input(request, name, age):
    context = {
        'name' : name,
        'age' : age,
    }
    return render(request, 'input.html', context)
# Q2. 숫자 곱한 값 보여주기
# 1. 숫자 2개를 입력 받아서
# 2. 그 두개를 곱한 값을 페이지에 출력
# 출력형태
# {{num1}} 곱하기 {{num2}} 는 {{num}}

def multiple(request, num1, num2):
    num = num1 * num2
    context = {
        'num' : num
    }
    return render(request, 'multiple.html', context)

# Q3. 구구단 리스트 만들기
# 1. 숫자 2개를 입력받아서
# 2. 첫번째 숫자 만큼 반복하는데 range(1, num1)
# 2-1. for data in range(1, num1)
# 3. num2와 data를 곱한 값 list에 담기
# 3-1. list.append(data*num2)

def pigeon(request, big, small):
    result = []
    if big < small :
        big, small = small, big
    for num in range(1, small):
        result.append(num*big)
    context = {
        'result' : result
    }
    return render(request, 'pigeon.html', context)

def dtl(request):
    my_list = ['짜장면', '차돌짬뽕', '탕수육', '콩국수']
    empty_list = []
    my_string = "Life is short, You need Python"
    today = datetime.now()
    context = {
        'my_list' : my_list,
        'empty_list' : empty_list,
        'my_string' : my_string,
        'today' : today
    }
    return render(request, 'dtl.html', context)

def forif(request):
    my_list = [100, 50, 30, 20 ,10]
    my_string = '간단한 문자열'
    data_a = '첫번째 데이터'
    data_b = '두번째 데이터'
    data_a, data_b = data_b, data_a
    context = {
        'my_list' : my_list,
        'my_string' : my_string,
        'data_a' : data_a,
        'data_b' : data_b,
    }
    return render(request, 'forif.html', context)

# 1. 간단한 반복문으로 리스트 각 요소들 출력
# 2. if, else 활용해서 문자열 비교
# 2-1. 내가 넘긴 문자열과 특정한 문자열 비교
# 3. if, elif, else 사용해보기
# 3-1. 문자열의 길이가 5이하이면 short,
# 3-2. 문자열의 길이가 10이상이면 long
# 3-3. 모두 아니면 적당 출력

# 모두 작성했다면, 
## 1. 반복문으로 리스트 가가 요소들을 출력해서
## 2. 해당 요소가 90이상이면 A
## 3. 해당 요소가 50이상이면 B
## 4. 그 외면 C 출력