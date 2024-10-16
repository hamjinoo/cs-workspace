# 디자인패턴

프로그램을 설계할 때 발생하는 문제점들을 객체 간의 상호 관계 등을 통해 해결할 수 있도록 하나의 '규약' 형태로 만들어놓은 것을 의미합니다.

- 예를 들어, 1만 줄의 코드를 하나의 파일에 작성할 수 있지만, 유지보수와 에러 처리 문제를 해결하기 위한 규약, 약속으로 디자인패턴이 만들어졌습니다.
- 디자인패턴은 라이브러리나 프레임워크를 설계하는 데 기초적인 원리로 활용됩니다.
  - **Vue.js**: MVVM 패턴
  - **Spring Web**: MVC 패턴

## 배우는 이유

디자인패턴을 배우면, 이를 기반으로 다양한 문제를 해결하는 데 영감을 받을 수 있고, 팀원들과 협업할 때 생길 수 있는 문제를 특정 패턴으로 빠르게 해결할 수 있습니다. 예를 들어, 특정 전략 패턴을 언급하며 빠르고 명확한 의사소통이 가능합니다.

## 디자인패턴의 종류

### 1. 생성패턴 (Creational Patterns)
- 객체 생성 방법에 대한 디자인패턴 // **객체를 어떻게 만들 것인가?**
- **우선 학습할 패턴**: `싱글톤(Singleton)`, `팩토리(Factory)`
- **추후 학습할 패턴**: 추상 팩토리(Abstract Factory), 빌더(Builder), 프로토타입(Prototype)

### 2. 구조패턴 (Structural Patterns)
- 객체와 클래스 등을 활용해 더 큰 구조를 유연하고 효율적으로 만드는 방법 // **생성된 객체를 기반으로 어떻게 구조를 형성할 것인가?**
- **우선 학습할 패턴**: `프록시(Proxy)`
- **추후 학습할 패턴**: 어댑터(Adapter), 브리지(Bridge), 복합체(Composite), 데코레이터(Decorator), 퍼사드(Facade), 플라이웨이트(Flyweight)

### 3. 행동패턴 (Behavioral Patterns)
- 객체나 클래스 간의 알고리즘과 책임 할당에 대한 디자인패턴 // **객체를 기반으로 어떻게 동작하게 할 것인가?**
- **우선 학습할 패턴**: `이터레이터(Iterator)`, `옵저버(Observer)`, `전략(Strategy)`
- **추후 학습할 패턴**: 책임연쇄(Chain of Responsibility), 커맨드(Command), 중재자(Mediator), 메멘토(Memento), 상태(State), 템플릿 메서드(Template Method), 비지터(Visitor)

## 참고 자료
[강의 링크](https://www.inflearn.com/course/lecture?inst=16252dc2&courseSlug=%EA%B0%9C%EB%B0%9C%EC%9E%90-%EB%A9%B4%EC%A0%91-cs-%ED%8A%B9%EA%B0%95&unitId=116050&tab=curriculum&subtitleLanguage=ko)
