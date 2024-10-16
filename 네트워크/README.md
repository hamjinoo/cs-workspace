# 네트워크

## 네트워크란
| 네트워크는 우리 생활의 모든 상황에 존재한다. 친구 네트워크, 통신 및 교통 네트워크, 웹은 모두 우리가 외부에서 경험하는 예이고, 뇌의 뉴런과 몸 안의 단백질은 지능과 생존을 결정하는 네트워크를 만든다. 이번 네트워크에서는 컴퓨터 네트워크를 주제로 작성하였다.

## 컴퓨터 네트워크란
컴퓨터 네트워크란 컴퓨터와 컴퓨터를 연결하여 노드들이 자원을 공유할 수 있게 하는 시스템이다.
<br>
- **노드란** : 네트워크를 이루는 장치 (컴퓨터, 공유기, 스위치 등등)
    - **END SYSTEM, 호스트** : 네트워크의 끝에 있는 노드 / 네트워크를 사용하기 위해 연결된 노드 / 클라이언트와 서버로 나뉨


작동하는 컴퓨터 네트워크에서 노드는 링크를 통해 전자 데이터를 전송하고 수신하는 방법을 정의하는 일련의 규칙 또는 [프로토콜](./pages/프로토콜(통신규약).md)을 따릅니다. [컴퓨터 네트워크 아키텍처]()는 이러한 물리적 및 논리적 구성 요소의 디자인을 정의하며, 네트워크의 물리적 구성 요소, 기능 조직, 프로토콜 및 절차에 대한 사양을 제공합니다.

### 결론 : 네트워크 = 프로토콜의 집합체 + 물리적 장치 + 네트워크 구성 + 보안 요소
1. **`프로토콜의 집합체`** : 데이터가 전송될 때 **어떤 규칙 절차**에 따라 움직이는지 정의
   - **OSI 7계층 모델**에서 각 계층에 맞는 프로토콜이 사용됩니다. 
   - 예시. IP, TCP, HTTP 등
2. **`물리적 장치`** : 데이터를 전송하기 위한 **물리적 장치**들
   - 데이터를 실질적으로 전송하고, 라우팅 및 스위칭을 통해 패킷을 목적지로 보냅니다.
   - 예시. 라우터, 스위치, 무선 안테나 등
3. **`네트워크 구성`** : 혼잡을 방지하기 위해 효율적으로 관리
   - 네트워크에는 어떤 **토폴로지**(구조)로 연결되어 있는지, 어떻게 **트래픽을 관리**할 것인지에 대한 설계가 포함됩니다.
4. **`보안`** : 네트워크의 신뢰성 유지, 데이터의 무결성, 기밀 보장
   - 외부 위협으로부터 안전하게 운영되기 위해 **보안 프로토콜**과 **방화벽, 암호화, 접근제어**