# Call by value와 Call by reference

## Call by Value (값에 의한 호출)
**함수 호출 시** 
- 메모리 공간에 함수를 위한 별도의 임시 공간 생성 
- 전달되는 변수 값을 복사해서 함수 인자로 전달 (function local variable)
- 함수 안에서 인자의 값이 변경되어도 함수 내 지역 변수가 변경되는 것이므로, 외부의 변수의 값은 변경되지 않는다.

## Call by Reference (참조에 의한 호출)
**함수 호출 시** 
- 메모리 공간에 함수를 위한 별도의 임시 공간 생성 
- 인자로 전달되는 변수의 레퍼런스를 전달
- 함수 안에서 인자의 값이 변경되면 레퍼런스가 변수를 가리키고 있기 때문에 인자로 전달된 변수의 값도 함께 변경된다.

## Java는 항상 Call by Value 
[Primitive type와 Reference type](https://github.com/Dayoung1014/TIL/blob/main/interview/Java/Primitive%20type%EC%99%80%20Reference%20type.md)

**Primitive Type(기본 자료형)**
- 변수의 값을 복사해서 전달

**Reference Type(참조 자료형)**
- 변수가 가지는 값이 레퍼런스이므로 인자로 넘길 때 Call by Value에 의해 변수가 가지고 있는 레퍼런스가 복사되어 전달
