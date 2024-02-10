# docker-compose.yml

## 📁 docker-compose.yml

여러 Docker 컨테이너를 정의하고 실행하기 위한 도구이다.

애플리케이션의 서비스, 네트워크, 볼륨 등을 구성하고 다양한 컴포넌트를 연결 할 수 있다.  

(비유) 여러 Docker 컨테이너로 구성된 애플리케이션의 '조립 설명서' 역할 

### 📝 docker-compose.yml **구성**

| 명령 | 의미 | 설명 |
| --- | --- | --- |
| version | docker-compose 파일 버전 지정	 | 버전에 따라 사용할 수 있는 기능과 구문이 다르다 
(https://docs.docker.com/compose/compose-file/compose-versioning/) |
| services | 서비스(컨테이너화할 애플리케이션) 정의   | 하나의 서비스 == 하나의 컨테이너
이미지 환경 변수, 포트 등을 설정 |
| services - image | 서비스 이미지 지정 | 서비스 컨테이너를 실행시키기 위한 이미지 설정
이미지 이름, 이미지 ID로 설정
로컬에 있는 경우 해당 이미지 사용, 없는 경우 Docker Hub에서 받아옴 |
| services - build | 서비스 이미지를 빌드할 Dockerfile 경로 | Dockerfile을 사용하여 이미지를 빌드하는 경우 경로와 설정 |
| services - command/entrypoint | 컨테이너 안에서 작동할 명령 지정 | Dockerfile의 CMD, ENTRYPOINT와 동일
단, Dockerfile보다 docker-compose에서 정의하는 것이 우선 순위 |
| services - environment/env_file | 컨테이너 안의 환경 변수 설정/환경 변수 파일 지정 | environment 을 통해 환경 변수를 설정 
env_file을 통해 환경 변수 파일을 지정 |
| services - volumes | 데이터 볼륨을 컨테이너에 마운트 | Host Directory Path : Container Directory Path |
| services - ports | 호스트, 커테이너 간 매핑 | Host Port : Container Port  |
| services - depends_on | 서비스의 의존성을 정의 | 이를 통해 서비스 시작 순서를 제어 가능 |
| services - networks | 서비스가 연결될 네트워크 지정 | 컨테이너 그룹을 분리하고 필요한 컨테이너끼리만 통신 가능 |
| networks | 컨테이너 간의 네트워킹 정의 | 여러 서비스가 서로 통신할 수 있도록 설정 가능 |
| volumes | 데이터를 저장하기 위한 볼륨 정의 | 볼륨은 컨테이너가 삭제되어도 데이터가 유지됨 |
| configs | 구성 파일을 서비스와 공유하기 위한 선언 | Docker Swarm 모드에서 사용  |
| secrets | 민감한 정보를 안전하게 전달하고 저장하기 위한 선언 | Docker Swarm 모드에서 사용  |
 