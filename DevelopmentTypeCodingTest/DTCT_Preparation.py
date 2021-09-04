'''
    다음은 2020 카카오 2차 코딩테스트 안내문에 쓰여 있던 문장입니다.

     "오프라인 코딩 테스트에서는 JSON format의 데이터를 응답하는 REST API를
      활용해야 하니, REST API 호출과 JSON format 데이터를 파싱해 활용할 수 있는
      parser 코드를 미리 준비해 오시기 바랍니다."

     개발형 코딩 테스트의 핵심 키워드 : REST API, JSON

     REST의 등장 배경
     - HTTP는 GET, POST, PUT, DELETE 등의 다양한 HTTP 메서드를 지원합니다.
       ㅇ 실제로는 서버가 각 메서드의 기본 설명을 따르지 않아도 프로그램을 개발할
          수 있습니다.
       ㅇ 하지만 저마다 다른 방식으로 개발하면 문제가 될 수 있어 기준이 되는
          아키텍처가 필요합니다.
       ㅇ 예를 들어, 서버입장에서 생성은 DELETE 메서드를 받고, 사용자 삭제를
          할때에는 POST 메서드를 쓰면 안 되는 걸까? 라는 생각을 할 수가 있다.
          이러면 API를 클라이언트 측에서 서버에 맞게 코딩을 해야하므로 명확한
          기준이 필요하다
     - REST는 각 자원에 대하여 자원의 상태에 대한 정보를 주고받는 개발 방식을 의미합니다.
     - REST의 구성 요소
       ㅇ 자원(Resource) : URL를 이용
       ㅇ 행위(Verb) : HTTP 메서드를 이용
       ㅇ 표현(Representations) : 페이로드를 이용
       예) 사용자(자원) 회원등록(행위)를 하고 싶습니다.
           아이디는 123 비번은 12로 설정하고 싶어요(표현)
           URL : https://www.example.com/users
           HTTP Method : POST
           Payload : {"id": "123", "password": "12"}

     - REST API란?
       ㅇ API : 프로그램이 상호작용하기 위한 인터페이스를 의미합니다.
       ㅇ REST API : REST 아키텍처를 따르는 API를 의미합니다.
       ㅇ REST API 호출 : REST 방식을 따르고 있는 서버에 특정한 요청을 전송하는
                         것을 의미합니다.

     - JSON(JavaScript Object Notation)
       ㅇ 데이터를 주고 받는데 사용하는 경량의 데이터 형식
     - JSON 형식을 따르는 데이터 예시
        {
           "id": "asd",
           "password": "12",
           "age": 30,
           "hobby": ["football", "programming"]
        }
     - JSON 데이터는 키와 값의 쌍으로 이루어진 데이터 객체를 저장합니다.

     REST API 연습용 서비스
     - 목킹(Mocking)이란 어떠한 기능이 있는 것처럼 흉내내어 구현한 것을 의미합니다.
     - 가상의 REST API 제공 서비스 : https://jsonplaceholder.typicode.com/
     - API 호출 경로 : https://jsonplaceholder.typicode.com/users/2
                     https://jsonplaceholder.typicode.com/users
'''

# JSON 객체 사용 예제
import json

# 사전 자료형(dict) 데이터 선언
user = {
    "id": "asd",
    "password": "12",
    "age": 30,
    "hobby": ["football", "programming"]
}

# 파이썬 변수를 JSON 객체러 변환
json_data = json.dumps(user, indent=4)
print(json_data)

# JSON 데이터로 변환하여 파일로 저장
with open("user.json", "w", encoding="utf-8") as file:
    json_data = json.dump(user, file, indent=4)

# REST API를 호출하여 회원 정보를 처리하는 예제
import requests

# REST API 경로에 접속하여 응답(Response) 데이터 받아오기
target = "https://jsonplaceholder.typicode.com/users"
reponse = requests.get(url=target)

# 응답(Response) 데이터가 JSON 형식이므로 바로 파이썬 객체로 변환
data = reponse.json()

# 모든 사영자(user) 정보를 확인하며 이름 정보만 삽입
name_list = []
for user in data:
    name_list.append(user['name'])

print(name_list)