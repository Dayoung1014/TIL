# Kafka의 개념, 특징, 동작 방식 

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
<sub>출처 https://www.confluent.io/blog/event-streaming-platform-1/</sub>


Kafka가 개발되기 전 링크드인의 데이터 처리 시스템이다. 데이터를 전송하는 Source application, 데이터를 받는 Target application이 많아지며 시스템 복잡도가 높아지게 되었고 아래와 같은 문제점이 발생하게 되었다.

- 데이터 처리가 파편화 되어있어 흐름을 파악하고 장애, 유지 보수에 대응하기 어려움
- 데이터 시스템마다 별도의 파이프라인이 존재하고 데이터 포맷,  프로토콜 등이 달라 유연성, 확장성이 떨어짐
- 또한 데이터 불일치 가능성이 있어 신뢰도 감소

이러한 문제를 해결하기 **모든 이벤트, 데이터의 흐름을 중앙에서 관리**하는 Kafka가 나오게 되었다.

## After Kafka
![After_Kafka](https://github.com/Dayoung1014/TIL/assets/58163364/9b28f846-998d-441b-9c6e-54d4b7be843d)
<sub>출처 https://www.confluent.io/blog/event-streaming-platform-1/</sub>

Kafka를 적용한 후 링크드인의 데이터 처리 시스템이다. Kafka를 기반으로 스트림 중심 데이터 아키텍처를 구축하였으며 위의 문제점들을 해결하고 아래와 같은 특징을 갖게 되었다.

- 모든 이벤트, 데이터의 흐름을 중앙에서 관리할 수 있게 됨
- 시스템이 추가되도 Kafka가 제공하는 표준 포맷으로 연결하므로  확장성과 신뢰성이 증가
- 개발자는 각 서비스간의 연결이 아닌, 서비스들의 비즈니스 로직에 집중 가능

## 동작 방식 
Kafka는 Pub-Sub 모델의 메시지 큐 형태로 동작한다.