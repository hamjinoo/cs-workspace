# 3-tier-architecture

# Client Server
| 실제 유저가 사용하는 곳이다.

- 클라이언트(웹 브라우저 또는 모바일 앱)는 사용자가 직접 상호작용하는 인터페이스다.
- 클라이언트는 사용자의 요청을 웹서버로 보내고, 서버로부터 받은 응답을 사용자에게 보여준다.

### CSR (Client Side Rendering)

-------------------------------------------
# WAS (Web Server + Application Server)


## Web Server
| 주로 HTTP/HTTPS 요청을 처리하며 정적 파일을 클라이언트 서버에게 전달하는 역할을 한다.

- 정적 파일(HTML, CSS, JavaScript)을 제공한다.
- 만약 클라이언트로부터의 요청이 데이터 조회나 처리를 요구할 경우 데이터베이스에 요청하여 데이터를 받아서 그 데이터를 바탕으로 클라이언트에게  제공합니다.
- 서버 사이드 렌더링의 경우 서버 사이드 스크립트를 실행하여 HTML로 변환하여 클라이언트에게 제공한다.
- 예시. Apache, Nginx, Microsoft IIS 등.

### SSR (Server Side Rendering)


## Application Server

-------------------------------------------
# Database
| 저장할 공간이 필요해지면서 데이터를 저장하고 관리하는 시스템이다.


- 예시. MySQL, PostgreSQL, MongoDB, Oracle 등