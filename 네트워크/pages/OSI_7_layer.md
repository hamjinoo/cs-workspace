# OSI 7 Layer

### OSI Model이 생긴 이유

네트워크 통신을 위해 통신에 참여하는 주체들이 따라야 할 형식, 절차, 규약을 체계적으로 정의하기 위해 OSI 모델이 만들어졌습니다. 모든 통신 기능을 하나의 프로토콜로 구현할 수 없기 때문에, 각 기능을 모듈화하여 계층별로 나누는 것이 필요했습니다. 그래서 OSI 7계층 모델과 TCP/IP 스택(4계층)이 탄생하게 된 것입니다.

더 쉽게 설명하자면 각각의 계층이 서로 독립적인 성질을 띄기 때문에, 에러 발생 시에는 해당하는 계층의 장비 혹은 소프트웨어만 보수하면 됩니다.

우선 OSI 7 Layer를 배우는 이유부터 알아야겠죠?

<aside>
💡 결국 네트워크는 통신을 하기 위한 건데, 통신 기능이 제대로 동작하기 위해서는 네트워크만의 약속된 통신 방법이 있어야 한다.
</aside>

<br>

## 7. application layer
- 소프트웨어 응용 프로그램에 의해 생성되고 사용되는 데이터. 이 계층에서 사용하는 주요 프로토콜은 HTTP입니다.
- HTTP, DNS, SMTP, FTP

## 6 presentation layer
응용 프로그램이 수용할 수 있는 형태로 데이터가 변환됩니다. HTTPS 암호화 및 복호화가 이 계층에서 일어난다고 보는 전문가도 있습니다.
- 예: 인코딩 ↔ 디코딩, 암호화 ↔ 복호화, 압축 ↔ 압축 해제

## 5 session layer
컴퓨터 간의 연결(연결, 유지, 종료)을 제어합니다(계층 4에서 TCP 프로토콜이 처리하기도 합니다). 

## 4 transport layer
- 연결된 두 당사자 간의 데이터 전송 및 서비스 품질 관리 수단을 제공합니다. 이 계층의 주요 프로토콜에는 TCP와 UDP가 있습니다.

## 3 network layer
실제로 데이터를 목적지까지 안전하고 빠르게 찾아갈 수 있게 하는 프로토콜
- 데이터 패킷을 목적지까지 라우팅
- IP 주소 기반 통신
- 최적의 경로 결정 (라우팅)

**2 data link layer**   
 동일한 네트워크에 있는 장치 간의 통신을 처리합니다. 계층 3을 우편물의 주소로 생각하며 계층 2는 해당 주소에 있는 사무실 번호 또는 아파트 호수를 지시한다고 생각할 수 있습니다. 이 계층에서는 이더넷이 가장 많이 사용되는 프로토콜입니다.
물리 계층을 바탕으로 두 장치간에 데이터를 주고 받을 수 있도록 하는 계층 (투인트 투 포인트)
- 노드 간 데이터 전송, 오류 검출 및 수정
- 여기선 IP가 아닌 MAC 주소 기반 통신(ARP)
    - **ARP 프로토콜 :** IP주소를 MAC 주소로 변환해주는 프로토콜


**1 physical layer**   
패킷이 전기, 무선, 광학적 펄스로 전환되고 전선, 무선파, 케이블을 통해 비트(정보의 가장 작은 단위)로 전송됩니다.
- 물리적 매체를 통해 비트 단위 데이터 전송
- 케이블, 전파 등 실제 전송 매체
- 예. 허브, 리피터,, 네트워크 카드, 통신 케이블


**쉽게 요약해보기**   
데이터는 7계층부터 1계층까지 순서대로 포장됩니다. 그런 다음 데이터는 네트워크를 통해 전달되며, 중간에 있는 라우터는 1~3계층까지 확인하며 목적지 IP를 찾습니다. 목적지에 도달하면, 1계층부터 7계층까지 순서대로 포장을 풀어, 최종 데이터를 받는 것입니다.
