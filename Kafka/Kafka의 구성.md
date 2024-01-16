# Kafka의 구성
<sub>[강의](https://www.youtube.com/watch?v=waw0XXNX-uQ&list=PL3Re5Ri5rZmkY46j6WcJXQYRlDRZSUQ1j&pp=iAQB)를 보며 정리한 내용입니다.</sub>

# Kafka Cluster (카프카 클러스터)
![Kafka Cluster](https://github.com/Dayoung1014/TIL/assets/58163364/931c1dc0-c097-41dc-a8bd-23a620167211)
<br><sub>출처 https://kafka.apache.org/090/documentation.html</sub>

**Kafka**는 고가용성을 위해 여러 개의 **Kafka 서버**와** Zookeeper**로 구성된 **클러스터 구조**로 이루어져 있다.

일반적으로 3개 이상의 **Kafka 서버(Broker, bootstrap server)**로 구성되며, 이러한 구조를 통해 Broker에 저장된 데이터를 다른 Broker에게 공유하고 하나의 Broker에 문제가 생겼을 때, 다른 Broker로 그 역할을 대체해서 시스템을 정상적으로 유지시키는 방식으로 동작한다.

**Zookeeper**는 분산 어플리케이션의 데이터 관리 기능을 가지고 있으며, 여러 개의 Broker 들 간 정보 변경 공유 및 동기화 등 컨트롤 해 주는 역할을 수행한다.
때문에 Zookeeper없이 kafka가 동작할 수 없다는 특징이 있다.

# Broker (브로커)
![Broker](https://github.com/Dayoung1014/TIL/assets/58163364/3a57218f-71c4-4668-8adb-7564e940c1e2)
<br>

**Kafka가 설치되어있는 서버 단위**

보통 3개 이상으로 구성하는 것을 권장한다.

# Topic (토픽)
![PTC](https://github.com/Dayoung1014/TIL/assets/58163364/ddf57fb9-c9af-4d63-9784-fbc009799908)
<br>

**데이터가 들어갈 수 있는 공간**

카프카 클러스터의 브로커에서 데이터를 관리할 때 기준이 된다. (DB의 테이블, 파일시스템의 폴더와 유사)

Topic 이름에 무슨 데이터를 담는지 명시하면 유시 보수 시 편하다. (ex. click_log, send_sms, location_log 등)

하나의 Topic은 1개 이상의 Partition으로 구성된다.

# Partition (파티션) 
![P1](https://github.com/Dayoung1014/TIL/assets/58163364/01ae1642-0384-4877-97fe-e156fa2f30e1)

**Topic 안에서 Record(데이터)를 처리하는 단위**

Partition 내부 번호는 Offset이라고 하며 0번부터 시작한다.
하나의 Partition은 Queue와 같이 Record가 쌓이고 Consumer는 가장 오래된 순서로 Record를 가져간다.
Consumer가 Record를 가져가도 Partition에서 삭제되지 않고 남아있는다.



<br>![P2](https://github.com/Dayoung1014/TIL/assets/58163364/a473cc96-2e7f-4127-abf0-fbf6461ab4bf)
<br>

Partition에 있는 동일한 데이터를 다른 그룹에 있는 Consumer가 사용할 수 있으며 이는 Kafka의 중요한 장점이다.

(ex. click_log Partition에 있는 Record를 분석하고 시각화하기 위해 Elasticsearch에 저장하는 Consumer / 백업하기 위해 Hadoop에 저장하는 Consumer)

Partition을 늘리는 것은 가능하지만 다시 줄이는 것은 불가능하기 때문에 주의해야 한다.

Partition을 늘리고 데이터를 가져가는 Counsumer의 개수 또한 늘려 처리를 분산시킬 수 있다.


<br>![P4](https://github.com/Dayoung1014/TIL/assets/58163364/64fd3f7d-d274-4d43-b89b-aa4d7161fad3)
<br>

Partition의 데이터의 저장되는 최대 시간 or 최대 크기를 옵션으로 정해 삭제할 수 있다.

## Partition에 Record가 들어가는 방식
![P3](https://github.com/Dayoung1014/TIL/assets/58163364/8247e2ee-153a-4b2c-b995-f426afb2ba24) 
<br>

**1. key가 null이고 기본 파티셔너 사용할 경우**
- Round robin (라운드 로빈)으로 할당되어 Partition에 번갈아가며 들어간다.

**2. key가 null이 아니고, 기본 파티셔너 사용할 경우**
- key의 hash(해시) 값을 구하고, 특정된 Partition에 할당된다.


## Replication Factor & Leader Partition, Follower Partition (파티션의 복제)
Partition의 고가용성을 위해 복제 할 수 있다.

이 때 원본을 Leader Partition, 복제본을 Follower Partition이라고 하며 이 둘을 합쳐 **ISR (In Sync Replica)이라고도 한다.**

Leader Partition이 있는 Broker에 장애가 발생하더라도 다른 Broker에 있는 Follower Partition이 Leader의 역할을 인계 받아 서비스의 연속성을 보장할 수 있다.

<br>![Replica](https://github.com/Dayoung1014/TIL/assets/58163364/bd1f55b8-b0c9-4e8c-8fcc-1e4eb43bdc00)
<br>

Producer의 Topic의 Partition의 데이터를 전달 받는 주체가 Leader이다.

Producer의 ack  옵션을 통해 Partition이 데이터를 잘 받고 있는지 확인할 수 있다.

**ack = 0**
- 리더에 전송하고 응답값 받지 않음
    - 리더에 잘 전달되었는지 나머지에 잘 복제되었는지 알 수 없고 보장할 수 없음
    - 속도는 빠르지만 데이터 유실 가능성 있음

**ack = 1**
- 리더에 전송하고 잘 받았는지 응답값 받음
    - 나머지에 잘 복제되었는지는 알 수 없음
    - 리더가 받은 즉시 리더에 장애가 난다면 데이터 유실 가능 

**ack = all**
- 리더, 팔로워에 데이터가 잘 전달되었는지 응답값을 받음 
    - 데이터 유실 없으나 속도가 느림


## Replication이 많을수록 좋은건가? 
브로커의 리소스 사용량도 그만큼 많아지므로 들어오는 데이터양과 저장 시간을 고려하여 설정해야 한다.
3개 이상의 브로커를 사용할 때 레플리케이션은 3으로 하는 것을 추천

**Replication Factor가 1인 경우**
- Leader(원본) 1 + Follower(복제) 0

**Replication Factor가 2인 경우**
- Leader(원본) 1 + Follower(복제) 1

**Replication Factor가 3인 경우**
- Leader(원본) 1 + Follower(복제) 2

# Producer (프로듀서)
![PTC](https://github.com/Dayoung1014/TIL/assets/58163364/ddf57fb9-c9af-4d63-9784-fbc009799908)
데이터를 프로듀싱(생산)하고 Topic의 Partition에 Publish(전송)하는 역할
- Topic에 해당하는 데이터 생성
- Topic으로 데이터를 Publish(전송)하며 이 때 key 설정을 통해 Topic의 Partition을 지정할 수 있다.
- Broker를 통해 처리 실패 확인 / 재시도

# Consumer(컨슈머)
![PTC](https://github.com/Dayoung1014/TIL/assets/58163364/ddf57fb9-c9af-4d63-9784-fbc009799908)
![Consumer1](https://github.com/Dayoung1014/TIL/assets/58163364/c430f1d4-500d-474a-9653-52e5acc0a011)
![Consumer2](https://github.com/Dayoung1014/TIL/assets/58163364/de8b51f1-c68c-4d63-a5b0-4ab2f038ce9c)

Topic의 Partition에 저장된 데이터를 Subscribe(구독)하여 가져가는 역할
데이터를 가져가는 행위를 Poolling(폴링)이라고 한다.
- Topic 내부의 파티션으로부터 데이터를 Ppolling
- Offset 위치를  카프카의 __consumer_offset 토픽에 Consumer의 그룹별 Topic별로 나눠져 기록(commit)하여 Consumer 마다 데이터를 어디까지 가져갔는지 알 수 있다. Consumer가 중지 되었을 때 __consumer_offset를 통해 중지 시점을 확인하고 처리 시점을 복구할 수 있는 고가용성을 가진다.
- Consumer의 개수는 Partition의 개수 보다 적거나 같아야 하고 여러 개인 경우 Consumer 그룹을 병렬 처리하며 속도가 빨라진다.

## Consumer의 Lag
![Lag](https://github.com/Dayoung1014/TIL/assets/58163364/fe7c9d0e-b518-4b8b-ab22-ec227fd67ee8)


**Topic의 Partition내에서 Consumer가 마지막으로 읽은 offset과 Producer가 마지막으로 넣은 offset의 차이**

이를 통해 Consumer의 상태를 볼 수 있다.

하나의 Topic에 여러 Partition이 존재하는 경우 lag 또한 각각 존재하며 이 중 가장 큰 값을 records-lag-max라고 한다.

### Burrow (Consumer의 Lag 모니터링) 

Consumer Lag 모니터링을 도와주는 독립적인 application으로 멀티 Kafka Cluster를 지원한다.

Sliding Window를 통해 Consumer의 status를 확인할 수 있다. (ERROR, WARNING, OK)

HTTP API를 제공한다.



#### 출처
https://kafka.apache.org/090/documentation.html
https://www.youtube.com/@DevWonYoung/playlists