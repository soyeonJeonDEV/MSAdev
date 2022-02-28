# 2022-02-28 수업 내용 정리

### OSI 7 LAYER
: 규약, 장애처리를 쉽게 하기 위해 

7계층  Application  
6계층  Presentation  
5계층  Seesion  
4계층  Transport  
3계층  Network  
2계층  DataLink  
1계층  Physical  


1 ~ 4계층을 합쳐서 DataFlow Layer 라고 부르기도 한다.  
5 ~ 7계층을 합쳐서 Application Layer 라고 부르기도 한다.   

#### 1계층 Physical Layer  
- 랜카드 -> 선으로 물리적으로 연결(NIC,허브...)
- 단지 데이터를 전달할 뿐, 데이터가 무엇인지, 어떤 에러가 있는지 신경쓰지 않는다.
- L1

#### 2계층 DataLink Layer
- MAC 주소를 가지고 통신
- 브리지, 스위치....

#### 3계층 Network Layer
- 공유기로부터 IP 주소를 받아옴
- 데이터를 목적지까지 가장 안전하고 빠르게 전달하는 기능(라우팅)
- 라우터...

라우터
- L3 장비
- IP Address를 포워딩해주는 역할

라우팅
- 어떤 네트워크 안에서 통신 데이터를 보낼 때 최적의 경로를 선택하는 과정

#### 4계층 Transport Layer
- TCP or UDP 결정

#### Application Layer
- HTTP or SSH 등 사용 결정

TCP/IP 4 Layer
Netwokr Interface = (OSI 7 LAYERS) Physical + Data Link  
Netwokr = (OSI 7 LAYERS) Netwokr  
Transport = (OSI 7 LAYERS) Transport  
Application = (OSI 7 LAYERS) Session + Presentation + Application
