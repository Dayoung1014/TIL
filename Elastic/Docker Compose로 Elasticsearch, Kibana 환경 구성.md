# Docker Compose로 Elasticsearch, Kibana 환경 구성  

[Docker로 Elasticsearch, Kibana 환경 구성](https://github.com/Dayoung1014/TIL/blob/main/Elastic/Docker%EB%A1%9C%20Elasticsearch%2C%20Kibana%20%ED%99%98%EA%B2%BD%20%EA%B5%AC%EC%84%B1.md) 에서는 Docker 명령어를 사용하여 Elasticsearch, Kibana 환경을 구성했습니다.

이를 개발 환경에서 더욱 편리하게 관리하기 위해 아래의 Docker Compose를 작성했습니다.

## docker-compose.yml 
``` yml
services:
  elasticsearch:
    image: docker.elastic.co/elasticsearch/elasticsearch:7.16.3
    container_name: elasticsearch
    environment:
      node.name: everyyoung
      cluster.name: everyyoung-cluster
      discovery.type: single-node
      bootstrap.memory_lock: true
      ES_JAVA_OPTS: "-Xms512m -Xmx512m"
      xpack.security.enabled: true
      xpack.security.http.ssl.enabled: false
      ELASTIC_PASSWORD: ${ES_PASSWORD}
    volumes:
      - esdata:/usr/share/elasticsearch/data
    ports:
      - 9200:9200
      - 9300:9300
    networks:
      - elastic

  kibana:
    image: docker.elastic.co/kibana/kibana:7.16.3
    container_name: kibana
    depends_on:
      - elasticsearch
    ports:
      - 5601:5601
    environment:
      ELASTICSEARCH_HOSTS: ${ES_HOST}
      ELASTICSEARCH_USERNAME: ${ES_USER}
      ELASTICSEARCH_PASSWORD: ${ES_PASSWORD}
    networks:
      - elastic

``` 

주석을 통해 설명을 추가한 docker-compose.yml은 아래와 같습니다.

``` yml
version: '3.8'
services:
  elasticsearch:
    image: docker.elastic.co/elasticsearch/elasticsearch:7.16.3  # 사용할 Elasticsearch Docker 이미지
    container_name: elasticsearch  # 컨테이너 이름
    environment:  
      node.name: everyyoung  # 노드 이름
      cluster.name: everyyoung-cluster  # 클러스터 이름
      discovery.type: single-node  # 단일 노드 클러스터 설정
      bootstrap.memory_lock: true  # 메모리 스왑 방지
      ES_JAVA_OPTS: "-Xms512m -Xmx512m"  # Java 힙 메모리 설정
      xpack.security.enabled: true  # X-Pack 보안 기능 활성화
      xpack.security.http.ssl.enabled: false  # HTTP SSL 보안 비활성화
      ELASTIC_PASSWORD: ${ES_PASSWORD}  # Elasticsearch 비밀번호 (.env 내 변수)
    volumes:
      - esdata:/usr/share/elasticsearch/data  # 데이터 저장을 위한 볼륨 마운트
    ports:
      - 9200:9200  # HTTP 통신용 포트
      - 9300:9300  # 노드 간 통신용 포트
    networks:
      - elastic  # 사용할 네트워크 이름

  kibana:
    image: docker.elastic.co/kibana/kibana:7.16.3  # 사용할 Kibana Docker 이미지
    container_name: kibana  # 컨테이너 이름
    depends_on:
      - elasticsearch  # elasticsearch 컨테이너를 의존함
    ports:
      - 5601:5601  # 포트
    environment:
      ELASTICSEARCH_HOSTS: ${ES_HOST}  # Elasticsearch 호스트 정보 (.env 내 변수)
      ELASTICSEARCH_USERNAME: ${ES_USER}  # Elasticsearch 사용자 이름 (.env 내 변수)
      ELASTICSEARCH_PASSWORD: ${ES_PASSWORD}  # Elasticsearch 비밀번호 (.env 내 변수)
    networks:
      - elastic  # 사용할 네트워크 이름

networks:
  elastic:  # 정의된 네트워크 이름
    driver: bridge  # 네트워크 드라이버

volumes:
  esdata:  # 정의된 볼륨 이름
    driver: local  # 볼륨 드라이버
``` 