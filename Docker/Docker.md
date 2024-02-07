# 🐬 Docker

## ❓ Docker는 무엇인가?
Docker는 애플리케이션을 신속하게 구축, 테스트 및 배포할 수 있는 소프트웨어 플랫폼으로 컨테이너화된 애플리케이션을 생성, 배포, 실행 할 수 있다.

소프트웨어 이미지를 통해 컨테이너를 실행시키며, 컨테이너에는 라이브러리, 시스템 도구, 코드, 런타임 등 소프트웨어를 실행하는 데 필요한 모든 것이 포함되어 있다. 


## ❓ Docker는 왜, 언제 사용하는가?
Docker를 사용하면 환경에 구애받지 않고 애플리케이션을 빠르고 안정적으로 배포 및 확장할 수 있다. 

**운영 표준화** 
- 컨테이너식 애플리케이션을 통해 손쉽게 배포, 문제 파악하고 수정을 위해 롤백 가능

**원활한 이전** 

- 도커 기반 애플리케이션을 로컬 개발 시스템에서 프로덕션 배포로 원활한 이전 가능

**비용 절감**

- 도커 컨테이너 사용 시 각 서버에서 좀 더 쉽게 많은 코드를 실행하여 사용률을 높이고 비용 절감 가능


## ❓ Docker는 어떻게 작동되는가? (Docker VS VM)

![Docker_VM](https://github.com/Dayoung1014/TIL/assets/58163364/6a5ed213-0fde-49ad-a415-7fe13f19a84e)
[ 출처 [Docker is NOT a Hypervisor - by.mikesir87](https://blog.mikesir87.io/2017/05/docker-is-not-a-hypervisor/) ]

Docker와 VM(가상 머신)은 애플리케이션을 격리하여 실행하는 기술이다.

둘 다 애플리케이션을 격리된 환경에서 실행하며, 애플리케이션과 종속성을 함께 패키징하여 배포와 관리를 단순화하고, 다양한 환경에서의 일관된 실행을 보장 한다.

### 📦 Container vs 🤖 VM작동 차이

**Container**

- 호스트 OS의 커널을 공유하며, 각 컨테이너는 애플리케이션과 그 종속성만을 포함한다.
- 리소스 사용이 적고, 컨테이너의 시작이 빠르다.
- 애플리케이션 간의 격리는 VM보다 약간 낮지만, 서비스에게 필요한 충분한 격리는 제공된다.

**VM**

- 하이퍼바이저를 사용해 하드웨어 위에 완전히 분리된 가상의 환경을 생성힌디.
- 각 VM은 자신만의 OS, 애플리케이션, 라이브러리를 가진다.
- 리소스 사용이 많고 시작 시간이 길다.


## 🐬 Docker Image 🖼️ Container 📦

### 🖼️ Docker Image

Docker Container를 실행하는데 필요한 모든 파일, 설정, 라이브러리를 포함하고 있는 읽기 전용 템플릿이다.

Docker Hub에서 공유되고 있는 Image를 사용하거나 직접 Dockerfile을 만들고 빌드하여 Image를 만들 수 있다.

### 📦 Docker Container

Docker Image를 실행한 애플리케이션의 인스턴스이다.

격리된 파일 시스템, 네트워킹, 독립된 프로세스 공간을 갖는다. 그러므로 어떤 환경에서도 일관된 방식으로 실행될 수 있다.

Container는 생성, 시작, 정지, 이동, 삭제 등을 할 수 있다.

![Docker_container](https://github.com/Dayoung1014/TIL/assets/58163364/67b362c4-63a8-4441-a6df-482c27310414)
[ 출처 [도커와 컨테이너의 이해 (3/3) - by.cloudmt](https://tech.cloudmt.co.kr/2022/06/29/%EB%8F%84%EC%BB%A4%EC%99%80-%EC%BB%A8%ED%85%8C%EC%9D%B4%EB%84%88%EC%9D%98-%EC%9D%B4%ED%95%B4-3-3-docker-image-dockerfile-docker-compose/) ]

**Image (레시피) → Container (음식)**
- 하나의 Image로 여러 개의 Container를 만들 수 있다.
- 기존 Image를 수정하여도 이미 실행 중인 Container에 영향을 주지 않는다.


## 📝 Docker 명령어 
![Docker](https://github.com/Dayoung1014/TIL/assets/58163364/80162997-03f3-4e9a-b2ae-11cf0d8e0904)
[ 출처 [도커와 컨테이너의 이해 (3/3) - by.cloudmt](https://tech.cloudmt.co.kr/2022/06/29/%EB%8F%84%EC%BB%A4%EC%99%80-%EC%BB%A8%ED%85%8C%EC%9D%B4%EB%84%88%EC%9D%98-%EC%9D%B4%ED%95%B4-3-3-docker-image-dockerfile-docker-compose/) ]

### 기본

```bash
# Docker 버전 확인
docker -v 
```

### Image 관련

```bash
# Docker Hub에서 이미지를 받아옴
docker pull <이미지 이름>:<태그 이름>

# Docker 이미지 나열
docker images

# Docker 이미지 삭제
docker rmi <이미지 이름>
```

### Container 관련

```bash
# 컨테이너 생성 및 실행
docker run -dit \
–name <컨테이너 이름> \
-p <host port>:<container port> \
-e <env_key=env_value> \
<이미지 이름> \
<CMD(optional)>

# 컨테이너 나열 (-a : 정지된 컨테이너 포함) (status : 특정 상태에 있는 컨테이너 필터링)
docker ps (-a) (status={상태})

# 컨테이너 삭제 (-f : 실행 중인 컨테이너 강제 삭제)
docker rm (-f) <컨테이너 이름 또는 ID>

# 컨테이너 실행
docker start <컨테이너 이름 또는 ID>

# 컨테이너 중지
docker stop <컨테이너 이름 또는 ID>

# 컨테이너 로그 확인 (-f : 계속해서 follow 하여 로그를 실시간 스트리밍)
docker logs (-f) <컨테이너 이름 또는 ID>

# 실행 중인 컨테이너 내에서 명령어 실행 (-it : 인터렉티브 쉘 접근)
docker exec -it <컨테이너 이름 또는 ID> <CMD>
```

