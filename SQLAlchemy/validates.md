# SQLAlchemy의 `@validates`
SQLAlchemy @validates 데코레이터를 사용하여 모델의 특정 속성에 대한 유효성 검증을 할 수 있다.

서비스 레벨에서도 데이터에 대한 유효성 검증을 할 수 있지만 모델 레벨에서 처리하는 경우 아래와 같은 이점이 있다. 

- 중복 방지 : 여러 서비스에서 동일한 엔티티에 대한 검증 로직을 반복하여 작성하지 않아도 된다. 하나의 메소드로 관리되므로 유지보수에도 용이하다.
- 데이터의 일관성 : 모델 레벨에서 데이터베이스에 저장되기 전 동일한 메소드를 통해 검사를 수행하므로 데이터의 일관성, 무결성을 유지할 수 있다. 
- 관심사 분리 : 서비스 로직에서는 데이터의 유효성 검사를 수행하지 않아도 되어 서비스, 모델이 관심사가 명확해지고 자신의 역할에만 집중할 수 있다. 이를 통해 오류가 발생했을 경우 raise 되는 지점이 명확해져 관리에 용이하다.


#### @validates 예시 코드
```python
class PostEntity(Base):
    __tablename__ = "post"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column("post_title", String(128), nullable=False)
    content: Mapped[str] = mapped_column("post_content", String(128), nullable=False)

    @validates("title")
    def validate_name(self, key, title):
        if not title or title.strip() == "":
            raise ValueError("Title must not be empty")
        return name
```