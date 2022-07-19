
실행
pythonw -u app.py> logfile.txt 2>&1

종료
TASKKILL /F /IM pythonw.exe

파워쉘에서 로그 보기
Get-Content -Tail 1 .\\Log.txt -wait
