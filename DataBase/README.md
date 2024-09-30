# 데이터베이스

[용어 정리](./TERM.md)   
[데이터베이스 입문](./pages/1.쉬운코드_데이터베이스_개론.md)   
[관계형 데이터베이스](./pages/1.쉬운코드_데이터베이스_개론.md#relational-database)

## 데이터베이스 기초 개념

**데이터베이스란.**  
데이터들을 저장하고 조회하는 프로그램이다. 쇼핑몰의 경우 상품 정보, 고객 정보, 주문 정보 데이터를 데이터베이스에서 가져와 조회하거나 정보를 저장하는 것이다.

<br>

**DBMS (database management systmes)**  
사용자에게 DB를 정의하고 만들고 관리하는 기능을 제공하는 소프트웨어 시스템

<br>

**통합된 언어**

- 오늘날의 DBMS는 DML, VDL, DDL이 따로 존재하기보다는 통합된 언어로 존재
  - 대표적인 예가 relational database language : SQL

---

## Relational Data Model

### key 설명 (기본키, 외래키 등)

**superkey**

- relation에서 tuples를 unique하게 식별할 수 있는 attributes set
  **primary key**  
  **unique key**  
  **foregin key**
- 다른 relation의 PK를 참조하는 attributes set

<br>

### constraints

relational database의 relations들이 언제나 항상 지켜줘야 하는 제약 사항

<br>

## SQL로 데이터 처리하기

### SQL (Structured Query Language)

- 현업에서 쓰이는 relational DBMS의 표준 언어
- 종합적인 database 언어 : DDL + DML + VDL

| relational data model | SQL    |
| --------------------- | ------ |
| relation              | table  |
| attribute             | column |
| tuple                 | row    |
| domain                | domain |

<br>

- **데이터베이스 확인하기** : SHOW DATABASES;
- **데이터베이스 생성하기** : CREATE DATABASE db명;
- **특정 데이터베이스 사용하기** : USE db명;
- **선택한 데이터베이스 확인하기** : SELETE database();
- **데이터베이스 삭제하기** : DROP DATABASE 테이블명;
- **TABLE의 SCHEMA를 변경하고 싶을 때 사용** : ALTER TABLE '테이블명' '무엇을 할 것인가'

- **데이터 조회** : SELECT \* FROM 테이블명;
  - **AS** : FROM 테이블명 `AS` 별칭이라고 적으면 테이블 별칭으로 사용 가능하다. /
    - 예시. FROM project WHERE project.ID = 2002 -> FROM project AS P WHERE P.ID = 2002
  - **LIKE** : 이름이 N으로 시작하거나 N으로 끝나는 ~의 값을 알고 싶다.
    - 예시. SELECT OOO FROM 테이블명 WHERE OOO LIKE 'N%' or ~ OOO LIKE '%N';
    - NG가 들어갔으면 좋겠다 : LIKE '%NG%';
- **데이터 추가** : INSER INTO 테이블명 VALUE();
- **데이터 수정** : UPDATE 테이블명 SET attribute = 값; / 조건 : UPDATE 테이블명 SET attribute = 값 WHERE attribute = 값;
- **데이터 삭제** : DELETE FROM 테이블명; / 조건 : DELETE FROM 테이블명 WHERE attribute = 값;

---

- **primary key** : table의 tuple을 식별하기 위해 사용, 하나 이상의 attribute로 구성 / 중복된 값, NULL 값을 가질 수 없다.
- **UNIQUE** : 중복된 값을 가질 수 없다. / 단, NULL은 중복을 허용할 수도 있다. (RDBMS마다 다름)
- **NOT NULL** : NULL을 값으로 가질 수 없다.
- **DEFAULT** : attribute에 대한 값이 없다면 default 값으로 저장. / `menu varchar(15) DEFAULT '짜장면'`
- **CHECK** : attribute의 값을 제한하고 싶을 때 사용 / `age INT CHECK(age >= 20)`
- **FOREIGN key** : attribute가 다른 table의 primary key나 unique key를 참조할 때 사용
  - **CASCADE** : 참조값의 삭제/변경을 그대로 반영
  - **SET NULL** : 참조값이 삭제/변경시 NULL로 변경
  - **RESTRICT** : 참조값이 삭제/변경되는 것을 금지
  - **NO ACTION** : RESTRICT와 유사
  - **SET DEFAULT** : 참조값이 삭제/변경시 default 값으로 변경
    <br>

<br>

<br>

<br>

<br>

<br>

<br>
