# 윈도우 서버를 이용한 홈택스 전자파일 복호화 기능

### 환경설정
- python 3.9
- window server2019 2Core 4GB

### 필요 패키지
click==8.1.3  
colorama==0.4.5  
comtypes==1.1.11  
Flask==2.1.2  
importlib-metadata==4.12.0  
itsdangerous==2.1.2  
Jinja2==3.1.2  
MarkupSafe==2.1.1  
pywin32==304  
pywinauto==0.6.8  
six==1.16.0  
Werkzeug==2.1.2  
zipp==3.8.0  

### 실행방법
cmd 에서 아래 구문입력  

#### 실행  
pythonw -u 파일네임.py > logfile.txt 2>&1  
    
#### 종료  
TASKKILL /F /IM pythonw.exe  


##
## flask로 간단한 API 서버를 구현하면서 왜 대부분의 사람들이 uwsgi 를 사용하고 웹 서버에서 nginx를 사용하는 이유에 대해서 알아보고자 한다.

웹 서버는 클라이언트에게 정적인 컨텐츠를 제공 즉 html,css javascript 를 제공하고 was는 웹 서버와 웹 컨테이너가 합친 개념 즉 웹 서버 단독으로는 처리 할 수 없고 데이터베이스에서 로직 처리가 필요한 동적 컨텐츠를 제공 함과 동시에 정적인 데이터도 제공한다.

### 정적,동적 데이터를 제공하는 was 만 사용하면 되는 것 아닌가?
- 물론 was만 사용 해도 되지만 was는 db 조회 및 다른 로직을 처리하는 일도 하기 때문에 정적인 컨텐츠를 웹 서버에 맡기고 기능을 분리시켜 두는 것이 서버 부하를 방지하고 효율성을 높일 수 있게 된다.

### 분산을 위해 웹 서버를 사용하고 그 예시중에 nginx, apache를 사용?
- 물론 분산을 제공하기도 하지만 둘 다 다양한 기능을 제공하며 필자는 nginx가 부가적으로 제공하는 기능 과 nginx 와 자주사용 되는 uwsgi에 대해 말하고자 한다.

### flask 단독 실행
- 우선적으로 flask로 만 배포하게 되고 app.py 파일을 실행하게 되면

```
DO NOT USE THIS SERVER IN A PRODUCTION SETTING. 
It has not gone through security audits or performance tests. 
(And that’s how it’s gonna stay. We’re in the business of making Web frameworks, not Webservers,
so improving this server to be able to handle a production
environment is outside the scope of Django.)
```

위와 같은 에러를 보게 될 것이다. 이는 곧 공식적으로 프러덕션을 사용하지 말라는 이야기 이다.
그 이유는 공식 document를 확인해도 알 수 있듯이 성능이 매우 느리고 보안에 대한 문제가 있고 또 한 분산처리에 대한 어려움이 있어 wsgi를 사용하라고 명시한다.

### 서비스는 초기 상태이며 wsgi를 사용안해도 되지 않을까
- 우선 wsgi를 이해하기에 앞서 CGI(Common Gateway Interface) 에 대한 이해가 필요하다. CGI는 앞에서 언급한 웹 서버와 was 사이의 interface를 제공한다. interface에 대해 가볍게 이해하기 위해서 웹 서버 종류에는 아파치, 엔진x 가 있고 파이썬 웹 프레임 워크에는 Python, Django 가 있고 더 많은 종류들이 있는데 이를 연결하는 하나의 규약을 제공하여 다른 프레임워크를 사용하게 되더라도 연결하는데 불편하지 않게 하기 위함이다. 또 연결만 도와 주는 것이 아닌 프로세스/ 쓰레드에 대해 설정 및 멀티쓰레드, 서버가 죽었을때 다시 키는 환경을 제공한다.

