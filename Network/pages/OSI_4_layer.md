# OSI 4 Layer

### OSI 4 layer (TCP/IP stack)

- **Application Layer**: OSI의 7~5계층
- **Transport Layer**: OSI의 4계층
- **Internet Layer**: OSI의 3계층 (네트워크 계층)
- **Link Layer**: OSI의 2~1계층 (데이터 링크 및 물리 계층)

## 기본적인 4 계층
- **네트워크 인터페이크 계층(Link Layer)** : OSI 모델 물리 계층과 데이터 링크 계층을 합친 개념입니다. 데이터가 물리적으로 전송되고, 네트워크 장치들이 서로 연결되는 방식을 다루죠.
  - 주요 프로토콜 : Eternet, ARP, PPP
- **인터넷 계층 (Internet Layer) :** IP가 속한 계층으로, 데이터를 여러 네트워크를 거쳐 목적지로 보내는 일을 합니다. 패킷을 목적지로 라우팅하고, IP 주소를 통해 어디로 보낼지 결정합니다.
  - 주요 프로토콜 : IP, ICMP, IGMP
- **전송 계층 (Transport Layer) :** TCP와 UDP가 속한 계층입니다. 이 계층은 데이터가 정확하게 전달되도록 보장해요. TCP는 신뢰있고, 연결 지향적인 프로토콜이고, UDP는 빠르지만 신뢰성이 없는 프로토콜이죠.
- 주요 프로토콜 : TCP, UDO
- **응용 계층 (Application Layer) : **우리가 사용하는 애플리케이션과 직접적으로 상호작용해요. 웹 브라우저가 사용하는 HTTP, 파일 전송에 사용하는 FTP 등이 이 계층에 속합니다.
  - 주요 프로토콜 : HTTP, FTP, DNS, DHCP