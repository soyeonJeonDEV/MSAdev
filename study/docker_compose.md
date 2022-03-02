# Docker Compose
- 단일 서버에서 여러 컨테이너를 프로젝트 단위로 묶어서 관리
- docker-compose.yml YAML 파일을 통해 명시적 관리
- 손 쉬운 컨테이너 수평 확장

#### 프로젝트
- 워크스페이스 단위
- 함께 관리하는 서비스 컨테이너의 묶음

#### 서비스
- 컨테이너를 관리하기 위한 단위
- scale을 통해서 컨테이너의 수 확장 가능

#### 컨테이너
- 서비스를 통해 컨테이너 관리

##### 도커 호스트 : docker run 이 설치되어 있는 곳

#### docker-compose.yml
- version
- services
- container
  - ports
  - volumns
  - networks

#### docker-compose 설치
``` shell 
DOCKER_COMPOSE_VERSION=v2.2.3

sudo curl -L "https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_VERSION}/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

sudo chmod +x /usr/local/bin/docker-compose

sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose

docker-compose version
```

#### docker-compose command
``` shell 
# Dockerfile, docker-compose.yml 등의 파일들이 있는 곳에서 실행

docker-compose up # 포그라운드에서 실행
docker-compose up -d # 백그라운드에서 실행
docker-compose down # 전부 삭제
docker-compose stop # 컨테이너만 남아있음
docker-compose ls # docker-compose 상태
docker-compose -p bagic ps # bagic(폴더명)에서 뜨고 있는 컨테이너 확인
docker-compose up -d --scale was=3 # 3개의 was 컨테이너 생성
```

```
docker-compose up -d --scale was=3
```
- 자동으로 LB가 된다.
- 수동으로 scale-out 한 것
- auto-scale은 상태를 모니터링해서 자동으로 scale-out 한다.
- web service -> was service(LB) -> was container

컨테이너 이름은 폴더 + 서비스명 + 숫자  

컨테이너의 이미지를 보면 컨테이너 레파지토리를 알 수 있다.  

#### docker-compose web-was 연동
docker-compose.yml  
``` shell
version: '3.9'
services:
  web:
    image: wjsthdus36/msa:v3
    volumes:
    - ./conf:/etc/nginx/conf.d
    ports:
    - "80:80" # 외부 연결 가능
  was:
    image: wjsthdus36/msa:sysinfo_v1
    ports:
    - "80" # web으로 연결되도록
```

was.conf  
- docker-compose.yml 파일에서 web: volums: -./conf:/etc/nginx/conf.d (현재 디렉토리의 /conf 파일을 /etc/nginx/conf.d 와 매칭)
- ./conf 안에 들어갈 파일
``` shell
upstream was {
    ip_hash;
    server was:80; # 서비스이름
}

server {
    listen 80;
    server_name kbdev;
    access_log /var/log/nginx/test1.log;

location / {

        #root /usr/share/nginx/html;
        index index.html index.htm index.jsp;
        proxy_pass http://was; # 서비스이름
    }

    location ~ \.(css|js|jpg|jpeg|gif|htm|html|swf)$ {
        root /usr/share/nginx/html;
        index index.html index.htm;
    }

    location ~ \.(jsp|do)$ {
    index index.jsp;
        proxy_pass http://was;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-NginX-Proxy true;
        proxy_set_header Host $http_host;
    
    proxy_redirect off;
    charset utf-8;
    }

    error_page 500 502 503 504 /50x.html;
    location = /50x.html {
        root /usr/share/nginx/html;
    }
}
```

네트워크는 docker-compose up command를 쓸 때 자동으로 생성된다.  
