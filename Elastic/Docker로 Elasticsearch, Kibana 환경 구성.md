# Docker로 Elasticsearch, Kibana 환경 구성 

## Docker Network 생성 
    
    Elasticsearch, Kibana 컨테이너 간 연결 위한 사용자 정의 도커 네트워크를 구성합니다. 
    ```bash
    docker network create ${네트워크 이름}
    ```
    

## Elasticsearch 
  ### Docker Image pull & Container run
  Elasticsearch의 도커 이미지를 받은 후 해당 이미지를 통해 컨테이너를 실행시킵니다.
  ```bash
    docker pull docker.elastic.co/elasticsearch/elasticsearch:${버전}
    docker run --name ${컨테이너 이름} --net ${네트워크 이름} -p 9200:9200 -it docker.elastic.co/elasticsearch/elasticsearch:${버전}
  ```
     
    
  ### Elasticsearch user password 변경 
  Elasticsearch 컨테이너가 실행되면 아래와 같이 elasitc user에게 기본으로 설정된 password가 나옵니다. 
    
  `ℹ️  Password for the elastic user (reset with bin/elasticsearch-reset-password -u elastic): password`
    
  이를 아래와 같이 변경하여 사용할 수 있습니다.

  ```bash
    docker exec -it ${컨테이너 이름} bin/elasticsearch-reset-password -u elastic
  ```
    
  ### elasticsearch 설치 확인 
  ```bash
  docker exec -it elastic curl --insecure -u elastic -X GET "https://localhost:9200/_cluster/health?pretty"
  ```
  ```
    {
      "cluster_name" : "docker-cluster",
      "status" : "green",
      "timed_out" : false,
      "number_of_nodes" : 1,
      "number_of_data_nodes" : 1,
      "active_primary_shards" : 2,
      "active_shards" : 2,
      "relocating_shards" : 0,
      "initializing_shards" : 0,
      "unassigned_shards" : 0,
      "delayed_unassigned_shards" : 0,
      "number_of_pending_tasks" : 0,
      "number_of_in_flight_fetch" : 0,
      "task_max_waiting_in_queue_millis" : 0,
      "active_shards_percent_as_number" : 100.0
    }
  ```


## Kibana 
  ### Docker Image pull & Container run 
  Kibana 도커 이미지를 받은 후 해당 이미지를 통해 컨테이너를 실행시킵니다.
  ```bash
    docker pull docker.elastic.co/kibana/kibana:${버전}
    docker run --name ${컨테이너 이름} --net ${네트워크 이름} -p 5601:5601 docker.elastic.co/kibana/kibana:${버전}
  ```
     
    
  ### Kibana 접속
  [http://localhost:5601/](http://localhost:5601/app/dev_tools#/console)
  
  #### Enrollment token  
  elasticsearch 컨테이너에서 Enrollment token을 받아 입력합니다.
  ```bash
    docker exec -it elastic /usr/share/elasticsearch/bin/elasticsearch-create-enrollment-token -s kibana
  ```
  </br>
  <img src="https://github.com/Dayoung1014/TIL/assets/58163364/13e3552a-c13a-4d81-96e6-d0835c29b86b" width="300">
  </br>
  
  #### Code 입력 
  Kibana 컨테이너 실행 완료 시 나왔던 code를 입력합니다.
  </br>
  `Go to http://0.0.0.0:5601/?code={code} to get started` 

  </br>
  <img src="https://github.com/Dayoung1014/TIL/assets/58163364/5ed59b9d-36c7-4e61-9f13-0d5d63022dff" width="300">
  </br>

  #### Login
  Elasticsearch 컨테이너에 설정한 계정으로 로그인합니다.
  </br>
  `Username : elastic`
  </br>
  `Password : ${Password}`

  </br>
  <img src="https://github.com/Dayoung1014/TIL/assets/58163364/6f1949d6-2a0f-43a6-bb46-e8d528b94655" width="300">
  </br>
 


#### 참고
https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html

https://esbook.kimjmin.net/

https://www.elastic.co/guide/en/kibana/current/docker.html
