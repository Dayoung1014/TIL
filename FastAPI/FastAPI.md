# FastAPI

## FastAPI
FastAPI는 파이썬 표준 타입 힌트에 기초한 Python3.8+의 API를 빌드하기 위한 웹 프레임워크이다.

## FastAPI 기본 실습

### 설치

**FastAPI 설치 (전체)**

```powershell
pip install "fastapi[all]"
```

**FastAPI 설치 (부분적 설치)**

- FastAPI (운영 환경에 배포하려는 경우)
    
    ```powershell
    pip install "fastapi"
    ```
    
- uvicorn (서버 역할)
    
    ```powershell
    pip install "uvicorn"
    ```
    

### 실행

```python
#실행 실습 코드

# FastAPI 임포트 (FastAPI : API에 대한 모든 기능을 제공하는 파이썬 클래스)
from fastapi import FastAPI 

# FastAPI 인스턴스 생성
# 개발 서버 실행 시 -> uvicorn main:인스턴스이름 --reload
app = FastAPI()

# 경로(End Point) & 동작(HTTP 메소드) 생성
# @ : 데코레이터
@app.get("/")
def root():
    return {"message": "Hello World"}
```

```powershell
uvicorn main:app --reload
```
JSON 응답 : http://127.0.0.1:8000/

대화형 API 문서 (Swagger) : http://127.0.0.1:8000/docs

대안 API 문서 (Redoc) : http://127.0.0.1:8000/redoc

- `main`: `main.py`의 파일명 
- `app`: `main.py` 내부의 `app = FastAPI()` 줄에서 생성한 오브젝트
- `-reload`: 코드 변경 후 서버 재시작을 위한 옵션이며 주로 개발 시에만 사용된다.

## FastAPI의 OpenAPI 
**FastAPI**는 API를 정의하기 위한 **OpenAPI** 표준을 사용하여 모든 API를 이용해 "스키마"를 생성한다.

### 스키마란?
**스키마 :** 무언가의 정의, 설명으로 구현하는 코드가 아닌 추상적 설명이다.

**API 스키마** : API 경로, 가능한 매개 변수 등을 포함하며 **OpenAPI**은 API를 어떻게 정의하는지 지시하는 규격이다.

**데이터 스키마** : 스키마가 JSON처럼 특정한 데이터 형태일 수 있다 이 때 JSON 속성, 가지고 있는 데이터 타입을 뜻한다.

### OpenAPI 와 JSON 스키마
- OpenAPI는 API에 대한 스키마를 정의 
- JSON 스키마를 사용하여 API에서 보내고 받은 데이터의 스키마를 포함

FastAPI가 자동으로 생성한 API의 설명과 JSON(스키마): http://127.0.0.1:8000/openapi.json

### FastAPI의 OpenAPI 관련 실습

```python
from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}
```

http://127.0.0.1:8000/items/5?q=somequery → JSON 응답 `{"item_id":5,"q":"test"}`

- `/items/{item_id}`는 *경로 매개변수* `int`형 이어야 하는 `item_id`를 가지고 있다.
- `/items/{item_id}`는 선택적인 `str`형 이어야 하는 *경로 매개변수* `q`를 가지고 있다.
 

## async / await (비동기)

`async def`로 생성된 함수 내부에서만 `await`를 사용할 수 있다.

```python
results = await some_library()
@app.get('/')
async def read_results():
    results = await some_library()
    return results
```

#### 참고
[FastAPI 공식 문서](https://fastapi.tiangolo.com/ko/)

[FastAPI 공식 자습서 - 사용자 안내서](https://fastapi.tiangolo.com/ko/tutorial/)

[FastAPI 공식 자습서 - 사용자 안내서 - 첫걸음](https://fastapi.tiangolo.com/ko/tutorial/first-steps/)

[FastAPI 공식 자습서 - 사용자 안내서 - SQL (Relational) Databases](https://fastapi.tiangolo.com/ko/tutorial/sql-databases/)

[Kakao의 Kafka 적용기(영상)](https://tv.kakao.com/channel/3150758/cliplink/391419257)