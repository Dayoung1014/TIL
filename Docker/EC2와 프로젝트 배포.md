# EC2와 프로젝트 배포 

## 🟠 **Amazon EC2 (Amazon Elastic Compute Cloud)**

AWS가 제공하는 클라우드 기반의 컴퓨팅 서비스이다.

탄력있게(Elastic) CPU, 메모리,  스토리지 등을 구성하여 가상 머신(인스턴스)을 생성하고 인스턴스를 사용하여 웹 서버, 백엔드 서버, 데이터베이스 등을 구성하고 호스팅 할 수 있다.

## 🏃🏻‍♀️ 프로젝트 배포

### 배포 과정
**1️⃣ 인스턴스 접속**

```bash
# pem key 통해 EC2 인스턴스 접속
ssh -i {pem key 파일명.pem} ubuntu@{instance IP address}

#계정 변경
su - {계정명}
```

**2️⃣ 프로젝트 설정**

```bash
git pull {프로젝트 git https code}
```

**3️⃣ docker-compose up**

```bash
docker-compose -f {docker-compose 파일명.yml} up (-d) (--build)
```