# HTTP 요청 메소드

## HTTP 프로토콜에서 요청 메소드란?
클라이언트 - 서버 구조에서 요청(request), 응답(response)가 이루어지는 방식
이를 통해 Safe(안전), Chacheable(캐시 가능), Idempotence(멱등성)을 가질 수 있다.

## 종류 
### GET
- 특정 리소스의 표시를 요청
- GET을 사용하는 요청은 오직 데이터를 받는다

### HEAD
- GET 메서드의 요청과 동일한 응답을 요구하지만, 응답 본문을 포함하지 않는다.

### POST
- 특정 리소스에 엔티티를 제출할 때 
- 종종 서버의 상태의 변화나 부작용을 일으킨다.
### PUT .
- 목적 리소스 모든 현재 표시를 요청 payload로 바꾼다.

### DELETE
- 특정 리소스를 삭제한다.

### CONNECT
- 목적 리소스
- 식별되는 서버로의 터널을 맺는다.

### OPTIONS
- 목적 리소스의 통신을 설정하는 데 쓰인다.

### TRACE (en-US)
- 목적 리소스의 경로를 따라 메시지 loop-back 테스트를 한다.

### PATCH
- 리소스의 부분만을 수정하는 데 쓰인다.
 

![image](https://github.com/Dayoung1014/TIL/assets/58163364/7bf6c7ac-ccbd-43bf-910e-fae74042d5a6)
<sub>출처 https://www.rfc-editor.org/rfc/rfc7231#section-4.2.2</sub>

#### 출처
https://developer.mozilla.org/ko/docs/Web/HTTP/Methods

