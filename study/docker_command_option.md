# docker 옵션 정리

### -d 
컨테이너를 백그라운드에서 실행  

### -it
컨테이너를 종료하지 않은 채로, 터미널의 읿력을 계속해서 컨테이너로 전달하기 위해 사용  
특히, 쉘이나 CLI 도구를 사용할 때 매우 유용하게 사용  

### --name
컨테이너에 이름을 부여  

### -e
컨테이너의 환경변수를 설정  

### -p
호스트와 컨테이너 간의 포트 배포/바인드를 위해 사용  

### -v
호스트와 컨테이너 간의 볼륨 설정  
호스트 컴퓨터의 파일 시스템의 특정 경로를 컨테이너의 파일 시스템의 특정 경로로 마운트  

### --rm 
컨테이너를 일회성으로 실행  
컨테이너가 종료될 때 컨테이너와 관련된 리소스(파일 시스템, 볼륨)까지 깨끗이 제거  

### -w
Dockerfile의 WORKDIR 설정을 덮어쓰기 위해 사용  

### --entrypoint
Dockerfile의 ENTRYPOINT 설정을 덮어쓰기 위해 사용  

### --link
컨테이너 연결  

--net=”bridge”
컨테이너의 네트워크 모드를 설정
