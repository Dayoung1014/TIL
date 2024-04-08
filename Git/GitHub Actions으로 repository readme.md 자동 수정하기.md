# GitHub Actions으로 repository readme.md 자동 수정하기
TIL(Today I Learn), Algorithm 등의 repository들은 readme.md에 디렉토리와 파일의 링크를 정리해두는 경우가 많다. 주로 공부를 위한 repository이므로 링크로 정리해두면 readme를 통해 모든 목차와 파일명을 한 눈에 볼 수 있고 링크를 통해 바로 확인해볼 수 있기 때문이다. 

현재 TIL repository readme 또한 그렇게 작성해주고 있는데 매번 커밋 후 이를 readme에 반영해주는 것이 번거로웠고 자동화해주고 싶다는 생각이 들었다. 

그래서 **repository에 커밋이 푸시되었을 때 현재 디렉토리와 파일의 링크를 readme에 자동으로 작성**해주는 `GitHub Actions`을 만들게 되었다.


## GitHub Actions   
GitHub에서 제공하는 CI/CD(Continuous Integration/Continuous Deployment) 기능이다. 주로 소프트웨어 개발 워크플로우를 자동화하는 데 사용된다. GitHub Actions을 이용해 push, pr 같은 이벤트 시점에서 테스트, 빌드, 배포 등의 작업을 자동으로 수행할 수 있다.  

### Workflow
- 하나 이상의 작업(job)을 정의하고, 이 작업들이 어떤 순서로 어떤 이벤트에 의해 실행될지 지정하는 자동화된 프로세스이다.
- 워크플로우는 `.github/workflows` 디렉토리에 YAML(YML) 파일 형식으로 저장된다.
- 워크플로우 파일은 GitHub 저장소에 추가되며, 특정 이벤트가 발생하거나 지정된 스케줄에 따라 자동으로 실행된다.
- 워크플로우 파일 내에서는 실행할 작업, 사용할 러너(작업 실행 환경), 필요한 변수 등을 정의할 수 있다.

### Action
- 워크플로우 내에서 실행되는 개별 작업 or 명령어이다. 
- 액션을 통해 스크립트를 실행하거나, 외부 서비스를 호출하고, 코드를 빌드하고 테스트하는 등의 작업을 할 수 있다.
- 사용자는 직접 액션을 작성할 수도 있고, 다른 사용자가 공유한 액션을 재사용할 수도 있다. 
- GitHub Marketplace에는 다양한 액션이 공개되어 있어서 필요에 따라 선택하여 사용할 수 있다.
- 액션은 컨테이너 또는 JavaScript로 작성할 수 있으며, 입력, 출력, 환경 변수 등을 정의할 수 있다.
GitHub Actions를 사용하면 개발 워크플로우를 더욱 자동화하고 최적화할 수 있으며, 코드 통합, 테스트, 배포 등이 훨씬 더 효율적이고 간편해진다.
