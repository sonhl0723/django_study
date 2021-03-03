## Riot Api를 활용한 TFT 전적 검색

### 사전 준비
1. Riot Developer api key를 갱신한 아이디
1. 개인 django project 생성 후 django project settings.py의 SECRET_KEY 복사
1. __git clone__ -> requirements.txt를 본인의 django project로 복사 -> __pip install -r requirements.txt__
1. djtest 폴더 안 settings.py에 SECRET_KEY 붙여넣기
1. settings.py 77~82번째 줄 주석 해제 및 83번째 줄 주석 처리


### 구동 방식
+ Riot Developer 사이트 아이디 / 비밀번호 입력
+ 전적 확인 할 게임 아이디 입력
+ selenium + webdriver(chrome)으로 로그인 후 해당 아이디 api key 획득
+ Riot Api Key를 활용해 정보 획득
