# Primitive type와 Reference type


## Java Data Type 
자바에는 기본 자료형(Primitive type)과 참조 자료형(Reference type)이 있다.
```
Primitive Type (기본 자료형)
ㄴ Boolean Type(boolean)
ㄴ Numeric Type
    ㄴ Integral Type
        ㄴ Integer Type(short, int, long)
        ㄴ Floating Point Type(float, double)
        ㄴ Character Type(char)
Reference Type (참조 자료형)
ㄴ Class Type
    ㄴ String Type
    ㄴ Wrapper Class
ㄴ Interface Type
ㄴ Array Type
ㄴ Enum Type
```

### Primitive Type (기본 자료형)
데이터의 값을 저장한다.

#### 특징
- 사용하기 전 선언이 되어야 한다.
- OS에 따라 자료형의 길이가 변하지 않는다.
- 객체가 아니기 때문에 null을 가질 수 없다.

#### 메모리 
- 스택(Stack) 영역에 저장

### Reference Type (참조 자료형)
데이터를 저장하는 메모리의 주소만 저장한다. 
실제 데이터의 값은 다른 영역에 저장하고 참조 자료형이 그 주소를 가져 이를 통해 실제 객체를 참조한다.

#### 특징
- 객체이므로 의미하는 null을 가질 수 있다.
- 문법상으로는 에러가 없지만 실행시켰을 때 에러가 나는 런타임 에러가 발생합니다.

#### 메모리
- 실제 객체는 힙(Heap) 영역에 저장
- 참조 자료형 변수는 스택(Stack) 영역에 실제 객체들의 주소를 저장, 객체를 사용할때 마다 참조 변수에 저장된 객체의 주소를 불러와 사용하는 방식
![java_type](https://github.com/Dayoung1014/TIL/assets/58163364/75f6261c-df93-44e1-85e7-10376493f3dc)
