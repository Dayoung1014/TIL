# Kafka - windows 로컬 환경 실습
실행 환경: windows

설치 요소: Java(jdk11), Zookeeper, Kafka

# 설치 및 설정

## Java

Kafka는 Java로 작성되었으므로 JDK가 필요하다.

- https://www.oracle.com/java/technologies/downloads/#java17 에서Java 1.8 이상의 JDK 설치
    
    (실습 시 사용 - jdk 11.0.21)
    
- 환경 변수 등록
    - 참고 https://www.oracle.com/java/technologies/downloads/#java17

## **Kafka**

- https://kafka.apache.org/downloads Apache Kafka에서 버전 선택 후 원하는 디렉토리에 다운로드한다.
    
    (실습 시 사용 - 3.6.0 ********Binary downloads:Scala 2.12 - [kafka_2.12-3.6.0.tgz](https://downloads.apache.org/kafka/3.6.0/kafka_2.12-3.6.0.tgz))
    
- 다운 받은 디렉토리에서 압축을 푼다.
    
    ```bash
    #tgz압축 풀기
    tar -xvzf 파일명
    ```
    
- 디렉토리에 logs 폴더 생성 & config/server.properties 에서 log.dirs 변경
    
    ```bash
    #변경 전
    log.dirs=tmp/kafka-logs
    
    #변경 후
    log.dirs=설치된경로/logs
    ```
    

## **Zookeeper**

Kafka는 Zookeeper를 사용하여 클러스터 관리와 메타데이터 저장한다.

- https://archive.apache.org/dist/zookeeper/ Apache Zookeeper에서 버전 선택 후 원하는 디렉토리에 다운로드한다.
    
    (실습 시 사용 - [apache-zookeeper-3.8.3-bin.tar.gz](https://archive.apache.org/dist/zookeeper/stable/apache-zookeeper-3.8.3-bin.tar.gz))
    
- 다운 받은 디렉토리에서 압축을 푼다.
    
    ```bash
    #tgz압축 풀기
    tar -xvzf 파일명
    ```
    
- 디렉토리에 data 폴더를 생성한다. conf/zoo_sample.cfg 파일을 복제 후 zoo.cfg로 이름을 변경 후 dataDir 경로를 수정한다.
    
    ```bash
    #변경 전
    dataDir=tmp/zookeeper
    
    #변경 후
    dataDir=설치된경로/data
    ```
    

# 실행

## Zookeeper

![zookeeper1](https://github.com/Dayoung1014/TIL/assets/58163364/a892afa3-2bd4-4649-aaf1-4bd356920f94)
![zookeeper2](https://github.com/Dayoung1014/TIL/assets/58163364/39c9c526-0daf-46db-816f-51f2ded6a366)
![port1](https://github.com/Dayoung1014/TIL/assets/58163364/b3be3f73-7f70-4eea-a608-0498f0839a7c)
```bash
# zookeeper 실행 명령어
bin\windows\zookeeper-server-start.bat config\zookeeper.properties

# 2181포트 확인
netstat -na | findstr "2181"
```

## Kafka

![kafka1](https://github.com/Dayoung1014/TIL/assets/58163364/ef7bd1f3-b8a1-4784-bdc3-e805674c0e3e)
![kafka2](https://github.com/Dayoung1014/TIL/assets/58163364/3a058486-66d5-4653-a00b-c02f26ec5292)
![port2](https://github.com/Dayoung1014/TIL/assets/58163364/50eb326d-fb01-43ad-8848-db164775ad11)

```bash
# kafka 실행 명령어
bin\windows\kafka-server-start.bat config\server.properties

# 9092포트 확인
netstat -na | findstr "9092"
```

# 실습

## Topic 생성
kafka위치\bin\windows 에서 Topic을 생성하고 확인할 수 있다.
 
![create_topic](https://github.com/Dayoung1014/TIL/assets/58163364/56d7293d-5d2c-4d6f-b063-9f06fc100371)

```bash
#Topic 생성
kafka-topics.bat --create --bootstrap-server localhost:9092 --replication-factor 갯수 --partitions 갯수 --topic 토픽이름
Created topic kafka-test.
```

![list_topic](https://github.com/Dayoung1014/TIL/assets/58163364/a4e6bb5f-798a-4e57-afed-212609230949)

```bash
#Topic 리스트 확인
kafka-topics.bat --list --bootstrap-server localhost:9092
```

### Topic 생성, 확인 시 오류 해결 과정
    
Topic 생성 명령어를 실행했을 때 생성되지 않고 아래와 같은 오류가 발생하였다.
    
Kafka 서버가 정상적으로 실행중이었기 때문에 브로커와 연결이 되지 않아 발생하는 것 같았고 server.properties 설정 부분을 확인해봤다.
    
```bash
Error while executing topic command : Call(callName=createTopics, deadlineMs=1705386951608, tries=1, nextAllowedTryMs=1705386951729) timed out at 1705386951629 after 1 attempt(s)
[2024-01-16 15:35:51,636] ERROR org.apache.kafka.common.errors.TimeoutException: Call(callName=createTopics, deadlineMs=1705386951608, tries=1, nextAllowedTryMs=1705386951729) timed out at 1705386951629 after 1 attempt(s)
Caused by: org.apache.kafka.common.errors.DisconnectException: Cancelled createTopics request with correlation id 3 due to node 0 being disconnected
(kafka.admin.TopicCommand$)
```
    
아래와 같이 수정해주어 Kafka 클라이언트가 9092 포트를 통해 브로커와의 연결하는 것을 명시해주었고 오류를 해결하였다.

```bash
############################# Socket Server Settings #############################

# The address the socket server listens on. If not configured, the host name will be equal to the value of
# java.net.InetAddress.getCanonicalHostName(), with PLAINTEXT listener name, and port 9092.
#   FORMAT:
#     listeners = listener_name://host_name:port
#   EXAMPLE:
#     listeners = PLAINTEXT://your.host.name:9092
#listeners=PLAINTEXT://:9092 #수정 전 (주석 처리 되어 있었음)
listeners=PLAINTEXT://:9092 #수정 후

# Listener name, hostname and port the broker will advertise to clients.
# If not set, it uses the value for "listeners".
# advertised.listeners=PLAINTEXT://your.host.name:9092
```
참고

https://theserverside.tistory.com/630

https://blog.voidmainvoid.net/500


## **Kafka Python 클라이언트 설치**

Kafka와 상호 작용하기 위해 Python용 Kafka 클라이언트를 설치

```bash
pip install kafka-python
```

## Python Producer, Consumer 스크립트

Producer.py

```python
from kafka import KafkaProducer
from json import dumps
import time

producer = KafkaProducer(
    acks=0,  # 메시지 전송 완료에 대한 체크
    compression_type='gzip',  # 메시지 전달할 때 압축(None, gzip, snappy, lz4 등)
    bootstrap_servers=['localhost:9092'],  # 전달하고자 하는 카프카 브로커의 주소 리스트
    value_serializer=lambda x: dumps(x).encode('utf-8')  # 메시지의 값 직렬화
)

start = time.time()

for i in range(1000):
    data = {'str': 'result' + str(i)}
    producer.send('kafka-test', value=data)
    producer.flush()  #

print('[Done]:', time.time() - start)
```

![producer](https://github.com/Dayoung1014/TIL/assets/58163364/4eed4634-0bdb-409f-84d7-ff9b85df7615)
Consumer .py

```python
from kafka import KafkaConsumer
from json import loads

consumer = KafkaConsumer(
    'kafka-test',  # Topic name
    bootstrap_servers=['localhost:9092'],  # 카프카 브로커 주소 리스트
    auto_offset_reset='earliest',  # 오프셋 위치(earliest:가장 처음, latest: 가장 최근)
    enable_auto_commit=True,  # 오프셋 자동 커밋 여부
    group_id='test-group',  # 컨슈머 그룹 식별자
    value_deserializer=lambda x: loads(x.decode('utf-8')),  # 메시지의 값 역직렬화
    consumer_timeout_ms=1000  # 데이터를 기다리는 최대 시간
)

print('[Start] get consumer')

for message in consumer:
    print(
        f'Topic : {message.topic}, Partition : {message.partition}, Offset : {message.offset}, Key : {message.key}, value : {message.value}')

print('[End] get consumer')
```

![consumer](https://github.com/Dayoung1014/TIL/assets/58163364/993fbcc0-f7d7-497c-9c96-3345a6d01c58)