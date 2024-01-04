# Monolithic Architecture vs Microservice Architecture
 
## Monolithic Architecture
소프트웨어 개발 기법 중 하나로, 모든 구성 요소가 하나로 통합 되어있다.

**장점**
- 소규모 프로젝트에서는 간단하게 개발 및 운영이 가능하다.

**단점**
- 빌드/테스트 시간 증가 : 하나를 수정해도 전체를 빌드/테스트 해야한다.
- 작은 문제가 전체에 영향 : 하나의 서비스가 문제가 되면 모든 서비스 이용이 불가하다.
- 확장성 불리 : 하나의 서비스를 확장하기 위해 전체 프로젝트를 확장해야 한다.

## Microservice Architecture
소프트웨어 개발 기법 중 하나로, 기능(목적)별로 나눠서 운영, 배포하는 **웹 기반 분산 서비스 시스템 아키텍처**

기능(목적)별로 컴포넌트를 나누고 조합할 수 있다.

컴포넌트는 독립된 서버로 운영, 배포하여 서로 의존성이 없으며, API를 통해 다른 컴포넌트와 통신을 한다.

**장점**
- 약한 결합도와 강한 응집도
- 독립적 : 독립적 배포, 운영이 가능해 서비스에 문제가 생겨도 다른 서비스에 영향을 미치지 않는다.
- 확장성 : 서비스 별로 부분 확장이 가능하다.

**단점**
- 컴포넌트 별 호출 시 API를 사용하므로 Monolithic에 비해 **네트워크 레이턴시**와 **트래픽**이 **증가한다.**
- 컴포넌트 별 통신에 맞는 데이터로 맞추는 과정이 필요하다.
- DB도 개별 운영되므로 트랜잭션의 어려움이 있어 데이터의 정합성을 맞추기 위한 노력이 필요하다.

## Monolithic VS Microservice

![1](https://github.com/Dayoung1014/TIL/assets/58163364/c13e2614-ebd4-4878-8c61-89a80bad86a4)
![2](https://github.com/Dayoung1014/TIL/assets/58163364/0bb4671a-075b-49b7-b2a1-eaf87c654a5c)


### MSA 언제 사용해야할까?
MSA를 통해 얻을 수 있는 장점도 있지만 체계적으로 준비돼 있지 않으면 오히려 프로젝트 성능이 떨어질 수도 있다. 정답이 정해져 있는 것이 아니라, 프로젝트 목적, 현재 상황에 맞는 아키텍처 방식이 무엇인지 설계 시 고민하여 선택하여야 한다.


#### 출처
https://www.popit.kr/마이크로-서비스-관련-글-총정리/

https://shaul1991.medium.com/초보개발자-일지-대세-msa-너-뭐니-efba5cfafdeb

https://www.redhat.com/ko/topics/microservices/what-are-microservices

http://guruble.com/마이크로서비스microservice-아키텍처-그것이-뭣이-중헌디/