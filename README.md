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
