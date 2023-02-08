from typing import Union
from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{'item_name':'Foo'}, {'item_name':'Bar'},{'item_name':'Baz'}]

#1. 기본값
@app.get('/items')
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

#2. 선택적 매개변수
@app.get('/items_str/{item_id}')
async def read_item(item_id: str, q:Union[str, None] = None):
    if q:
        return {'item_id' : item_id, 'q' : q}
    return {'item_id' : item_id}

#3. 선택적 매개변수 형변환
@app.get('/items_bool/{item_id}')
async def read_item(item_id : str, q : Union[str, None] = None, short : bool = False):
    item = {'item_id' : item_id}
    if q:
        item.update({'q' : q})
    if not short:
        item.update(
            {'description' : 'This is an amazing item that has a long description'}
        )
    return item

#4. 여러경로/쿼리 매개변수
@app.get('/users/{users_id}/items/{item_id}')
async def read_user_item(
    user_id : int, item_id : str, q : Union[str, None] = None, short : bool = False
):
    item = {'item_id' : item_id, 'owner_id' : user_id}
    if q:
        item.update({'q' : q})
    if not short:
        item.update({'description' : 'This is an amazing item that has a long description'})
    return item

#5. 필수 쿼리 매개변수
# @app.get('/items/{item_id}')
# async def read_user_item(item_id : str, needy : str):
#     item = {'item_id' : item_id, 'needy' : needy}
#     return item

@app.get('/items/{item_id}')
async def read_user_item(item_id : str, needy : str, skip : int = 0, limit: Union[int, None] = None):
    item = {'item_id' : item_id, 'needy' : needy, 'skip' : skip, 'limit' : limit}
    return item