# Kafka 개요 및 설명 

## 개념
**Kafka**는 빠르고 확장 가능한 작업을 위해 데이터 피드의 분산 스트리밍, 파이프 라이닝 및 재생을 위한 실시간 스트리밍 데이터를 처리할 목적으로 설계된 분산형 게시-구독 메시징 플랫폼이다.

## 특징
- **High throughput message capacity** 
    - 짧은 시간 내 많은 데이터를 컨슈머까지 전달 가능 (분산, 병렬 처리로 속도 증가)
- **Scalability & Fault tolerant** 
    - 확장성, 신규 브로커 서버를 추가해 수평 확장이 가능, 브로커가 죽더라도 레플리카로 복제된 데이터를 통해 복구 가능
- **Undeleted log** 
    - Kafka 토픽에 들어간 데이터는 컨슈머가 가지고 가더라도 데이터가 사라지지 않음

## Before Kafka
![Before_Kafka](https://github.com/Dayoung1014/TIL/assets/58163364/fee25e84-b64f-4786-8e07-9cf755ebf54b) 
<br><sub>출처 https://www.confluent.io/blog/event-streaming-platform-1/</sub>


Kafka가 개발되기 전 링크드인의 데이터 처리 시스템이다. 데이터를 전송하는 Source application, 데이터를 받는 Target application이 많아지며 시스템 복잡도가 높아지게 되었고 아래와 같은 문제점이 발생하게 되었다.

- 데이터 처리가 파편화 되어있어 흐름을 파악하고 장애, 유지 보수에 대응하기 어려움
- 데이터 시스템마다 별도의 파이프라인이 존재하고 데이터 포맷,  프로토콜 등이 달라 유연성, 확장성이 떨어짐
- 또한 데이터 불일치 가능성이 있어 신뢰도 감소

이러한 문제를 해결하기 **모든 이벤트, 데이터의 흐름을 중앙에서 관리**하는 Kafka가 나오게 되었다.

## After Kafka
![After_Kafka](https://github.com/Dayoung1014/TIL/assets/58163364/9b28f846-998d-441b-9c6e-54d4b7be843d)
<br><sub>출처 https://www.confluent.io/blog/event-streaming-platform-1/</sub>

Kafka를 적용한 후 링크드인의 데이터 처리 시스템이다. Kafka를 기반으로 스트림 중심 데이터 아키텍처를 구축하였으며 위의 문제점들을 해결하고 아래와 같은 특징을 갖게 되었다.

- 모든 이벤트, 데이터의 흐름을 중앙에서 관리할 수 있게 됨
- 시스템이 추가되도 Kafka가 제공하는 표준 포맷으로 연결하므로  확장성과 신뢰성이 증가
- 개발자는 각 서비스간의 연결이 아닌, 서비스들의 비즈니스 로직에 집중 가능

## 동작 방식 
**Kafka**는 Pub-Sub 모델의 메시지 큐 형태로 동작한다.

### [Message Queue & PUB/SUB - Kafka, Redis, RabbitMQ](https://github.com/Dayoung1014/TIL/blob/main/Software%20Engineering/Message%20Queue%20%26%20PUB%2CSUB%20-%20Kafka%2C%20Redis%2C%20RabbitMQ.md)

![Kafka](https://github.com/Dayoung1014/TIL/assets/58163364/dba906ea-0d84-4905-ae13-01cc67e80cb9)
<br><sub>출처 https://cloud.google.com/pubsub/docs/migrating-from-kafka-to-pubsub?hl=ko</sub>


## 구성 요소
- **Event** : kafka에서 producer 와 consumer가 데이터를 주고받는 단위. 메세지
- **Producer** : kafka에 이벤트를 게시(post, pop)하는 클라이언트 어플리케이션
- **Consumer** : Topic을 구독하고 이로부터 얻어낸 이벤트를 받아(Sub) 처리하는 클라이언트 어플리케이션
- **Topic** : 이벤트가 모이는 곳. producer는 topic에 이벤트를 게시하고, consumer는 - topic을 구독해 이로부터 이벤트를 가져와 처리. 게시판 같은 개념
- **Partition** : Topic은 여러 Broker에 분산되어 저장되며, 이렇게 분산된 topic을 partition이라고 함
- **Zookeeper** : 분산 메세지의 큐의 정보를 관리

## 동작 과정
1. Publisher는 전달하고자 하는 메세지를 topic을 통해 카테고리화 한다.
2. Subscriber는 원하는 topic을 구독(Subscribe)함으로써 메시지를 읽어온다.
3. Publisher와 Subscriber는 오로지 topic의 정보만 알 뿐, 서로에 대해 알지 못한다.
4. Kafka는 Broker들이 하나의 클러스터로 구성되어 동작하도록 설계되어 있다.
5. 클러스터 내, broker에 대한 분산처리는 ZooKeeper가 담당한다.

## 장점 
- 대규모 트래픽 처리 및 분산 처리에 효과적
- 클러스터 구성, Fail-over, Replication 같은 기능이 있음
- 100Kb/sec 정도의 속도 (다른 메세지 큐 보다 빠름)
- 디스크에 메세지를 특정 보관 주기동안 저장하여 데이터의 영속성이 보장되고 유실 위험이 적다. 또한 Consumer 장애 시 재처리가 가능하다.

## 단점
- 구성 복잡도: 아파치 카프카는 구성이 복잡하며, 사용하기 위해서는 일정 수준의 기술적 이해와 노하우가 필요하다.
- 설정 오류의 위험성: 아파치 카프카는 다양한 설정 옵션을 제공하며, 설정을 잘못하면 시스템 동작에 오류를 유발할 수 있다.
- 서버 및 용량 비용: 아파치 카프카는 서버의 수와 스토리지의 용량에 따라 비용이 증가할 수 있다.
