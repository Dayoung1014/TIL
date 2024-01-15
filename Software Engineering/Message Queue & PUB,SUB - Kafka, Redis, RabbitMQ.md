# Message Queue & PUB/SUB - Kafka, Redis, RabbitMQ

## Message Queue (MQ, 메시지 큐)
![Message Queue](https://github.com/Dayoung1014/TIL/assets/58163364/a31dab7f-1a12-4dac-8e18-21d3b541d0e4)
<sub>출처 https://tecoble.techcourse.co.kr/post/2021-09-19-message-queue/</sub>

**Message Queue**는 프로세스 또는 프로그램 간에 데이터를 교환할 때 사용하는 통신 방법 중 하나로 메시지 지향 미들웨어(MOM:Message Oriented Middleware)를 구현한 시스템이다. 

Message Queue는 아래와 같은 특징을 갖는다.

- **비동기** : Queue라는 임시 저장소가 있기 때문에 나중에 처리 가능
- **낮은 결합도** : Application과 분리
- **확장성** : Producer / Consumer 확장 가능
- **탄력성** : Consumer 서비스가 다운되더라도 애플리케이션이 중단되는 것은 아니며 메시지는 지속하여 Queue에 있음
- **보장성** : Queue에 들어간다면 결국 모든 메시지가 Consumer 서비스에게 전달된다는 보장을 제공 

## PUB/SUB
![PUB SUB](https://github.com/Dayoung1014/TIL/assets/58163364/48108e3e-8ba1-4b4d-bb63-d0c6fb008f3b)

**PUB/SUB**은 비동기 메세징 전송 방식으로, 발신자의 메세지에는 수신자가 정해져 있지 않은 상태로 Publish(발행) 한다. 그리고 이를 Subscribe(구독)을 한 수신자만 정해진 메세지를 받을 수 있다.

Pub/Sub 모델의 구체적인 발행/구독 방식은 각 서비스 마다 다르다. 그 중 **Kafka, Redis, RabbitMQ**에서 사용하는 PUB/SUB을 비교해보려고 한다.

## Kafka, Redis, RabbitMQ

### Kafka
![Kafka](https://github.com/Dayoung1014/TIL/assets/58163364/dba906ea-0d84-4905-ae13-01cc67e80cb9)
<sub>출처 https://cloud.google.com/pubsub/docs/migrating-from-kafka-to-pubsub?hl=ko</sub>

**Kafka**는 LinkedIn에서 개발된 pub-sub 모델의 메시지큐 방식 기반, 분산 메시징 시스템이다.

**구성 요소**
- **Event** : kafka에서 producer 와 consumer가 데이터를 주고받는 단위. 메세지
- **Producer** : kafka에 이벤트를 게시(post, pop)하는 클라이언트 어플리케이션
- **Consumer** : Topic을 구독하고 이로부터 얻어낸 이벤트를 받아(Sub) 처리하는 클라이언트 어플리케이션
- **Topic** : 이벤트가 모이는 곳. producer는 topic에 이벤트를 게시하고, consumer는 - topic을 구독해 이로부터 이벤트를 가져와 처리. 게시판 같은 개념
- **Partition** : Topic은 여러 Broker에 분산되어 저장되며, 이렇게 분산된 topic을 partition이라고 함
- **Zookeeper** : 분산 메세지의 큐의 정보를 관리

**동작** 
1. Publisher는 전달하고자 하는 메세지를 topic을 통해 카테고리화 한다.
2. Subscriber는 원하는 topic을 구독(Subscribe)함으로써 메시지를 읽어온다.
3. Publisher와 Subscriber는 오로지 topic의 정보만 알 뿐, 서로에 대해 알지 못한다.
4. Kafka는 Broker들이 하나의 클러스터로 구성되어 동작하도록 설계되어 있다.
5. 클러스터 내, broker에 대한 분산처리는 ZooKeeper가 담당한다.

**장점**
- 대규모 트래픽 처리 및 분산 처리에 효과적
- 클러스터 구성, Fail-over, Replication 같은 기능이 있음
- 100Kb/sec 정도의 속도 (다른 메세지 큐 보다 빠름)
- 디스크에 메세지를 특정 보관 주기동안 저장하여 데이터의 영속성이 보장되고 유실 위험이 적다. 또한 Consumer 장애 시 재처리가 가능하다.

**단점**
- 구성 복잡도: 아파치 카프카는 구성이 복잡하며, 사용하기 위해서는 일정 수준의 기술적 이해와 노하우가 필요하다.
- 설정 오류의 위험성: 아파치 카프카는 다양한 설정 옵션을 제공하며, 설정을 잘못하면 시스템 동작에 오류를 유발할 수 있다.
- 서버 및 용량 비용: 아파치 카프카는 서버의 수와 스토리지의 용량에 따라 비용이 증가할 수 있다.

### Redis
![Redis](https://github.com/Dayoung1014/TIL/assets/58163364/458a2045-743c-4dbe-993a-98f73c985f21)
<sub>출처 https://medium.com/@saurabh.singh0829/redis-pub-sub-implementation-f3208e4625c7</sub>

**Redis**는 데이터베이스, 캐시, 메시지 브로커 및 스트리밍 엔진으로 사용되는 인메모리 데이터 구조 저장소이다.

**구성 요소**
- **Publisher** : 메세지를 게시(pub)
- **Channel** : 메세지를 쌓아두는 queue
- **Subscriber**: 메세지를 구독(sub)

**동작**
1. Publisher가 Channel에 메세지 게시
2. 해당 채널을 구독하고 있는 Subscriber가 메세지를 sub해서 처리 

**특징**
- Channel은 이벤트를 저장하지 않음.
- Channel에 이벤트가 도착 했을 때 해당 채널의 Subscriber가 존재하지 않는다면 이벤트가 사라짐
- Subscriber는 동시에 여러 Channel을 구독할 수 있으며, 특정한 Channel을 지정하지 않고 패턴을 설정하여 해당 패턴에 맞는 채널을 구독할 수 있다

**장점**
- 처리 속도가 빠름
- 캐시의 역할도 가능
- 명시적으로 데이터 삭제 가능

**단점**
- 메모리 기반이므로 서버가 다운되면 Redis 내의 모든 데이터가 사라짐
- 이벤트 도착 보장을 못함

### RabbitMQ
<img src="https://github.com/Dayoung1014/TIL/assets/58163364/a8d5a5e0-5e39-4607-ace3-0c7c6f4a6384" width="40%">
<img src="https://github.com/Dayoung1014/TIL/assets/58163364/c4e9c1f4-6c49-4e76-a55c-b96b0f547b0a" width="20%">
<img src="https://github.com/Dayoung1014/TIL/assets/58163364/8c67b299-b8b1-4a1b-acab-f5b95152fdbe" width="30%">

<sub>출처 https://www.cloudamqp.com/blog/part1-rabbitmq-for-beginners-what-is-rabbitmq.html</sub>

**RabbitMQ**는 AMQP 프로토콜을 구현한 메세지 브로커이다.

**AMQP(Advanced Message Queuing Protocol)** : 메세지 지향 미들웨어를 위한 개방형 표준 응용 계층 프로토콜

**구성 요소**
- **Producer** : 메세지를 보냄
- **Exchange** : 메세지를 목적지(큐)에 맞게 전달
- **Queue** : 메세지를 쌓아둠
- **Consumer** : 메세지를 받음

**동작**
1. Producer 가 Broker로 메세지를 보냄
2. Broker 내 Exchange(메세지 교환기) 에서 해당하는 key에 맞게 큐에 분배한다. (Binding or Routing 이라고 함)
    - topic 모드 : Routing Key가 정확히 일치하는 Queue에 메세지 전송 (Unicast)
    - direct 모드 : Routing Key 패턴이 일치하는 Queue에 메세지 전송 (Multicast)
    - headers 모드 : [Key:Value] 로 이루어진 header값을 기준으로 일치하는 Queue에 메세지 전송 (Multicast)
    - fanout 모드 : 해당 Exchange에 등록도니 모든 Queue에 메세지 전송 (Broadcast)
3. 해당 큐에서 Consumer가 메세지를 받는다.

**장점**
- Broker 중심적인 형태로 publisher와 consumer 간의 보장되는 메세지 전달에 초점을 맞추고, 복잡한 라우팅 지원
- 클러스터 구성이 쉽고 Manage UI 가 제공되며 플러그인도 제공되어 확장성이 뛰어남
- 20kb/sec 정도의 속도
- 데이터 처리 보단, 관리적 측면이다 다양한 기능 구현을 위한 서비스를 구축할 때 사용

**단점**
- MQ Server가 종류 후 재기동되면 기본적으로 Queue 내용은 모두 제거되어 데이터 손실의 위험성이 있다.
- Producer와 Consumer 간의 결합도가 높다

### Kafka, Redis, RabbitMQ 언제 무엇을 사용할까?
**Kafka** 
- 대용량 데이터 처리, 실시간, 고성능, 고가용성이 필요한 경우
- 저장된 이벤트를 기반으로 로그를 추적하고 재처리 하는게 필요한 경우

**Redis**
- 이벤트 데이터를 DB에 저장하기 때문에 굳이 미들웨어에 이벤트를 저장할 필요가 없는 경우
- Consumer에게 꼭 알람이 도착해야한다는 보장 없이 push 보내는것만 중요한 경우

**RabbitMQ** 
- 복잡한 라우팅을 유연하게 처리해야하고, 정확한 요청-응답이 필요한 경우
- 트래픽은 작지만 장시간 실행되고 안정적인 백그라운드 작업이 필요한 경우

### Kafka, Redis, RabbitMQ 비교

|  | Kafka | RabbitMQ | Redis Pub/Sub |
| --- | --- | --- | --- |
| 라우팅 | 기본기능으로 라우팅에 대해서 지원하지 않는다. Kafka Streams를 활용하여 동적라우팅을 구현할 수 있다. | Direct, Fanout, Topic, Headers의 라우팅 옵션을 제공하여 유연한 라우팅이 가능하다. | - |
| 프로토콜 | 단순한 메시지 헤더를 지닌TCP 기반 custom 프로토콜을 사용하기 때문에 대체가 어렵다. | AMQP, MQTT, STOMP 등 여러 메세징 플랫폼을 지원한다. | RESP (Redis Serialization Protocol) - TCP 통신 |
| 우선순위 | 변경 불가능한 시퀀스 큐로, 한 파티션 내에서는 시간 순서를 보장한다. 하지만 여러 파티션이 병렬로 처리할 때는 시간 순서 보장 못함 | priority queue를 지원하여 우선 순위에 따라서 처리가 가능하다. | 우선순위 처리는 커녕 이벤트가 도착할 지 보장도 못함 |
| 이벤트 저장 in Queue | 이벤트를 삭제하지 않고 디스크에 저장함으로 영속성(durability)이 보장되고, 재처리가 가능하다. | 메세지가 성공적으로 전달되었다고 판단될 경우 메세지가 큐에서 삭제되기 때문에 재처리가 어렵다 | 저장하지 않음. 심지어 channel에 이벤트가 도착했을 때 해당 채널의 subscriber가 존재하지 않으면 이벤트 사라짐 |
| 장점 | • 이벤트가 전달되어도 삭제하지 않고 디스크에 저장<br>• 고성능, 고가용성, 분산처리에 효과적<br>• producer 중심적 (많은 양의 데이터를 병렬 처리) | • 오래전에 개발되어 제품 성숙도가 크다<br>• 필요에 따라 동기/비동기식 가능<br>• 유연한 라우팅 • producer/consumer간의 보장되는 메세지 전달<br>• Manage UI 기본 제공<br>• 데이터 처리보단 관리적 측면이나 다양한 기능 구현을 원할 때 사용 | • channel을 구독하는 모든 subscriber가 이벤트를 받기 때문에 synchronization 문제에서 kafka보다 덜하다<br>• 미들웨어가 필요 없어서 가볍다 |
| 단점 | • 범용 메세징 시스템에서 제공되는 다양한 기능이 제공되지 않음 | • Kafka 보다 느림 | • 이벤트 도착 보장을 못함 |