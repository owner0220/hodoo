### 영화정보서비스(WATCHA)\_2인프로젝트\_황인식 외 1인

- 언어 : Python3
- 프레임워크 : Django
- 구현기능
  - 로그인, 영화 등록, 댓글
  - 최신 영화정보 크롤링, 게임(이스터에그)
- 담당 역할
  - Bootstrap 기본 UI 세팅
  - 백엔드, 모델 구성, API활용 DB 세팅&관리, RESTful API



#### Live Demo : [클릭](http://movielists-dev4.ap-northeast-2.elasticbeanstalk.com/)

URL http://movielists-dev4.ap-northeast-2.elasticbeanstalk.com/  

```html
테스트 계정   /    PW 
test        /   qqqq123!
```



---

### 프로젝트 목적

- Rest API, CRUD 구현, 학습내용 복기
- 오픈소스, API 활용 (레퍼런스 보는 연습)

#### 프로젝트 개요

- 영화 정보 조회 서비스 WATCHA 구현, 영화 평점과 댓글을 등록할 수 있고, 시청 영화, 보고 싶은 영화로 개인 영화 기호를 저장 관리 할 수 있습니다.

#### 프로젝트 발표 자료

#### **PPT :**  [클릭](https://docs.google.com/presentation/d/1qQ0z4cxDtFp-fiubJw3VYT-mG6mh5_AgcudOraOvoBA/edit?usp=sharing)

URL https://docs.google.com/presentation/d/1qQ0z4cxDtFp-fiubJw3VYT-mG6mh5_AgcudOraOvoBA/edit?usp=sharing

#### 느낀점

- 프로젝트 의의, 목적이 없으면 프로젝트가 산으로 갈 수도 있기 때문에 결과를 최대한 구체화하고 시작해야겠다 느꼈습니다.
- 오픈소스나 외부 라이브러리를 사용하다 보니 영어로 된 레퍼런스와 용어가 의미하는 정확한 뜻을 모르거나 잘못 해석해서  삽질을 하는 경우들도 있었지만, 매개변수와 반환값을 잘 알지 못해서 발생하는 문제들로 에러가 발생하는 경우들이 있어서 그러한 부분들을 좀 더 유의깊게 봐야겠습니다.
- 처음엔 모델 구성을 좀 쉽게 생각했는데 관계 구성하는 부분들이 생각보다 복잡해서 효과적인 관계 설정을 고민되어 지금은 정보처리기사의 정규화 내용을 다시 보며 학습하고 있습니다.



---

### 상세설명

```python
C9, bash 환경에서 개발하였습니다.
pyenv 1.2.9-2-g6309aaf2
Python 3.6.7
Django 2.1.8
```

※ 페이지는 1920*1080 화면 비율에 맞게 제작되었습니다.(이외 해상도 지원 X)

#### 실행 화면

![Sample_gif](./Sample_gif.gif)





##### Home(인트로페이지)

`path`   /

![hodoo-home](./hodoo-home.png)



---

`@admin 유저만 접근 허용`

##### admin(관리자 페이지)

`path`   /admin

![hodoo-home](./hodoo-admin.png)



---

`@admin 유저만 접근 허용`

##### accounts(사용자 계정)

`path`   /accounts

현재 가입되어 있는 사용자 계정들을 보여줍니다.

실질적으로 관리자 페이지에서 계정 관리를 하기 때문에 뷰가 필요 없었습니다.

- **사용자 로그 인     :** /login

![hodoo-home](./hodoo-login.png)

- 사용자 로그 아웃 : /logout

- 사용자 계정 생성 : /create

- 사용자 계정 수정 : /update
- 사용자 계정 삭제 : /\<int:id>/delete
- 사용자 상세 정보 : /detail



---

##### movies(영화 정보 페이지)

`path`   /movies

영화 

- **영화 정보 목록 :** /list

![hodoo-home](./hodoo-movie_list.png)

- **영화 디테일 :** /\<int:id>

![hodoo-home](./hodoo-movie_detail.png)

- **개봉예정 영화 :** /preticket

![hodoo-home](./hodoo-preticket.png)



`@로그인된 유저만 접근 허용`

- **영화 정보 검색 :** /search

![hodoo-home](./hodoo-search.png)

- **보고 싶은 영화 목록 :** /like_post

![hodoo-home](./hodoo-later.png)

- **이미 본 영화 목록 :** /watched_post

![hodoo-home](./hodoo-seen.png)

- 영화 댓글 추가 : /\<int:id>/scores/new
- 영화 댓글 삭제 : /\<int:id>/scores/\<int:score_new_id>/delete
- 영화 댓글 수정 : /\<int:id>/scores/\<int:score_id>/update
- 보고 싶은 영화 추가 : /\<int:id>/like
- 이미 본 영화 추가 : /\<int:id>/whatched



`@admin 유저만 접근 허용`

- 영화 정보 추가 :  /create
  - 영화 정보를 따로 추가할 수 있는 화면을 만들까 하다가 크롤링 업데이트로 변경
- 영화 정보 삭제:  /\<int:id>/delete
- 영화 정보 수정:  /\<int:id>/update
- API 영화 추가 : /put_data/\<int:year>
  - 영진위 api
  - The MovieDb api



---

##### game(이스터에그 게임)

`path`   /game

건물 쌓기 게임(오픈소스)_일부 구성 변경, 장고와 호환성 매칭

> 참조 URL 유실 찾는 즉시 업데이트 예정

![hodoo-home](./hodoo-game.png)



---

##### api(RESTful API)

`path`   /api

RESTful API 제공

- 사용자 데이터
- 영화 데이터

`@일반적인 유저 접근`

![hodoo-home](./hodoo-user-api.png)

`@admin 유저 접근`

![hodoo-home](./hodoo-admin-api.png)



##### Kakao 플러스 친구 연결

![hodoo-home](./hodoo-kakao-plus.png)



---

### 사용 외부 라이브러리

- 크롤링
  - beautifulsoup4
  - bs4
  - requests
  - urllib3
- Bootstrap4_django폼
  - django-bootstrap4
- REST API
  - django-rest-swagger
  - djangorestframework
- 더미 데이터
  - Faker
  - django-seed
- 배포
  - AWS