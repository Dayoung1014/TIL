# SQLAlchemy에서 `relationship`
두 모델 간의 연관 관계를 정의하며 이를 통해 인스턴스에서 연관되어 있는 다른 모델을 접근할 수 있다.

## relationship 의 인자 
### `back_populates` or `backref`
양방향 관계 설정 시 엔티티가 서로를 어떻게 참조할지 설정할 수 있다.

#### back_populates 
- 관련된 두 모델에 각각 서로를 참조하는 이름을 지정한다.  
    ```python
    class Parent(Base):
        __tablename__ = 'parent'
        id = Column(Integer, primary_key=True)
        children = relationship("Child", back_populates="parent")

    class Child(Base):
        __tablename__ = 'child'
        id = Column(Integer, primary_key=True)
        parent_id = Column(Integer, ForeignKey('parent.id'))
        parent = relationship("Parent", back_populates="children")
    ```

#### backref 
- 하나의 모델에 관계를 설정하면 반대쪽 모델에 자동으로 참조 속성이 추가된다.
    ```python
    class Parent(Base):
        __tablename__ = 'parent'
        id = Column(Integer, primary_key=True)
        children = relationship("Child", backref="parent")

    class Child(Base):
        __tablename__ = 'child'
        id = Column(Integer, primary_key=True)
        parent_id = Column(Integer, ForeignKey('parent.id'))
        # parent 속성이 자동으로 추가된다.
    ``` 

