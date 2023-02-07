from fastapi import FastAPI              #FastAPI 임포트
from enum import Enum                    # 2-3. 참조

app = FastAPI()                          # app 변수에 FastAPI 객체 생성

# 1. FastAPI 활용하여 GET 방식 호출
@app.get("/")                            # 명칭 : 경로동작 데코레이터, GET 방식의 경로 '/' 일 경우 호출됨
async def root():                        # 명칭 : 경로동작 함수 
    return {"message" : "Hello World"}   # 명칭 : 경로동작 함수 반환값, 브라우저에서 '/' URL 호출 -> {'message' : 'Hello World'} 화면 출력

## 1-1. 위와 동일한 방식으로 동작함
# @app.get("/")
# def root():                            # async 함수 존재 유무
#     return {"message" : "Hello World"}

# 2. FastAPI 활용하여 GET 방식의 경로 매개변수 호출
@app.get("/items/{item_id}")             # GET 방식의 경로 '/items/item_id'일 경우 호출됨, items_id의 경우 외부 값 입력
async def read_item(item_id):
    return {'item_id' : item_id}         # 브라우저에서 '/items/King' URL 호출 -> {'item_id' : King} 화면 출력

# 2-1. FastAPI 활용하여 GET 방식의 경로 타입이 정의된 매개변수 호출
@app.get("/numitems/{item_num}")         # GET 방식의 경로 '/numitems/item_num'일 경우 호출됨, items_num의 경우 int 타입으로 제한된 외부 값 입력
async def read_item(item_num:int):
    return {'item_num' : item_num}       # 브라우저에서 '/numitems/1' URL 호출 -> {'item_num' : 1} 화면 출력
                                         
                                         # 브라우저에서 '/numitems/foo' URL 호출 -> 아래와 같은 오류 JSON 화면 출력
                                         # {
                                         #     "detail": [
                                         #         {
                                         #             "loc": [
                                         #                 "path",
                                         #                 "item_num"
                                         #             ],
                                         #             "msg": "value is not a valid integer",
                                         #             "type": "type_error.integer"
                                         #         }
                                         #     ]
                                         # }

# 2-2. 순서 문제
# 동일한 경로에서 값과 타입이 같은 값의 정의된 매개변수가 존재할 경우 일반적인 방식의 URL이 호출되지 않을 수 있다.
# 그렇기 때문에 우선적으로 일반적인 URL을 정의한 뒤 값과 타입이 같은 값이 들어갈 여지가 있는 정의된 매개변수를 정의해야 한다  
# 1번이 정의된 후 2번 함수를 정의해야 둘 다 제대로 호출되게 된다.
# 1번 함수
@app.get('/users/me')
async def read_user_me():
    return {'user_id': 'the current user'}
# 2번 함수
@app.get('/users/{user_id}')
async def read_user(user_id:str):
    return {'user_id': user_id}

# 2-3. 사전정의 매개변수
# Enum 클래스를 활용하여 사전정의 매개변수를 정의할 수 있다
class ModelName(str, Enum):
    alexnet = 'alexnet'
    resnet = 'resnet'
    lenet = 'lenet'

@app.get('/models/{model_name}')
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {'model_name': model_name, 'message': 'Deep Learning FTW!'}

    if model_name.value == 'lenet':
        return {'model_name': model_name, 'message': 'LeCNN all the images'}
    
    return {'model_name': model_name, 'message': 'Have some residuals'}

# 2-4. 경로를 포함하는 경로 매개변수
# /files/{file_path:path}
@app.get('/files/{file_path:path}')
async def read_file(file_path: str):
    return {"file_path": file_path}