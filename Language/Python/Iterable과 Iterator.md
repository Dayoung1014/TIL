# Iterable과 Iterator

## Iterable
- 반복 가능한 객체
- list, dict, set, str, bytes, tuple, range

## Iterator
- 값을 차례대로 꺼낼 수 있는 객체
- 파이썬 내장 함수(iter())로 생성할 수 있다.
- iterable 객체의 매직 메소드(__iter__())로 생성할 수 있다.

### 파이썬 내장 함수 iter()를 사용한 iterator 객체 만들기
```python
    >>> a = [1, 2, 3]
    >>> a_iter = iter(a)
    >>> type(a_iter)
    <class 'list_iterator'>
    
    # 파이썬 내장 함수 next()를 사용하여 값을 차례대로 하나씩 꺼내기
    >>> next(a_iter)
    1
    >>> next(a_iter)
    2
    >>> next(a_iter)
    3

    # 다음 값이 없는 경우 StopIteration 예외 발생
    >>> next(a_iter)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    StopIteration
```

### iterable 객체의 매직 메소드 __iter__() 를 사용한 iterator 객체 만들기
```python 
    >>> b = {1, 2, 3}
    >>> dir(b)
    ['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
    >>> b_iter = b.__iter__()
    >>> type(b_iter)
    <class 'set_iterator'>
    
    # iterator 매직 메소드 __next__()를 사용하여 값을 차례대로 하나씩 꺼내기
    >>> b_iter.__next__()
    1
    >>> b_iter.__next__()
    2
    >>> b_iter.__next__()
    3
    >>>
```
    

#### 출처
https://wikidocs.net/16068