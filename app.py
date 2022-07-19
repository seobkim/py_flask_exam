from flask import Flask, request, jsonify, make_response
from pywinauto import Application

from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/py/ereport/decrypt', methods=['POST'])
def decryptFunc():
    param = request.get_json()

    print(param)
    resultValue = decryptFile(param)

    if (resultValue["success"]):
        response = {"resultMsg": resultValue["resultMsg"], "succesCode": "Y"}
        return jsonify(response)

    else:
        response = {"resultMsg": resultValue["resultMsg"], "succesCode": "N"}
        return jsonify(response)


def decryptFile(param):
    app = Application(backend="uia").start(r"C:/DreamSecurity/NTSFileDecrypt/ntsfdec.exe")
    dialogs = app.windows()

    """
    Dialog - '국세청 세무자료 복원(복호화) 프로그램'    (L1573, T949, R2269, B1162)
['국세청 세무자료 복원(복호화) 프로그램', '국세청 세무자료 복원(복호화) 프로그램Dialog', 'Dialog']
child_window(title="국세청 세무자료 복원(복호화) 프로그램", control_type="Window")
   | 
   | Edit - ''    (L1745, T995, R2163, B1021)
   | ['Edit', '암호화된 파일 경로Edit', 'Edit0', 'Edit1']
   | child_window(auto_id="1005", control_type="Edit")
   | 
   | Button - '찾기...'    (L2176, T995, R2251, B1021)
   | ['찾기...Button', 'Button', '찾기...', 'Button0', 'Button1']
   | child_window(title="찾기...", auto_id="1007", control_type="Button")
   | 
   | Edit - ''    (L1745, T1029, R2163, B1055)
   | ['Edit2', '복원된 세무자료 경로Edit']
   | child_window(auto_id="1006", control_type="Edit")
   | 
   | Edit - ''    (L1745, T1063, R2039, B1089)
   | ['비밀번호Edit', 'Edit3']
   | child_window(auto_id="1011", control_type="Edit")
   | 
   | Button - '세무자료 복원'    (L1845, T1119, R1991, B1145)
   | ['세무자료 복원', '세무자료 복원Button', 'Button2']
   | child_window(title="세무자료 복원", auto_id="1008", control_type="Button")
   | 
   | Static - '복원된 세무자료 경로'    (L1591, T1036, R1740, B1051)
   | ['Static', '복원된 세무자료 경로', '복원된 세무자료 경로Static', 'Static0', 'Static1']
   | child_window(title="복원된 세무자료 경로", auto_id="2000", control_type="Text")
   | 
   | Static - '암호화된 파일 경로'    (L1591, T1000, R1740, B1015)
   | ['암호화된 파일 경로', '암호화된 파일 경로Static', 'Static2']
   | child_window(title="암호화된 파일 경로", auto_id="2001", control_type="Text")
   | 
   | Static - '비밀번호'    (L1591, T1068, R1740, B1083)
   | ['비밀번호', 'Static3', '비밀번호Static', '비밀번호0', '비밀번호1']
   | child_window(title="비밀번호", control_type="Text")
   | 
   | Image - '비밀번호'    (L1591, T1104, R2250, B1107)
   | ['Image', '비밀번호2', '비밀번호Image']
   | child_window(title="비밀번호", control_type="Image")
   | 
   | TitleBar - ''    (L1598, T953, R2266, B982)
   | ['TitleBar']
   |    | 
   |    | Menu - '시스템'    (L1266, T767, R1288, B789)
   |    | ['시스템', 'Menu', '시스템Menu', '시스템0', '시스템1']
   |    | child_window(title="시스템", auto_id="MenuBar", control_type="MenuBar")
   |    |    | 
   |    |    | MenuItem - '시스템'    (L1266, T767, R1288, B789)
   |    |    | ['시스템2', '시스템MenuItem', 'MenuItem']
   |    |    | child_window(title="시스템", control_type="MenuItem")
   |    | 
   |    | Button - '닫기'    (L2223, T950, R2267, B983)
   |    | ['닫기', 'Button3', '닫기Button']
   |    | child_window(title="닫기", control_type="Button")
    """

    path = "Z:\\" + param["path"]
    pwd = param["pwd"]

    print(path)
    print(pwd)
    app['Dialog']['암호화된 파일 경로Edit'].set_edit_text(path)
    app['Dialog']['비밀번호Edit'].set_edit_text(pwd)

    app['Dialog']['세무자료 복원Button'].click()

    returnValue = ""
    print(app['Dialog2']['Static'].window_text())

    resultMsg = app['Dialog2']['Static'].window_text()

    if (app['Dialog2'].exists() and app['Dialog2']['Static'].window_text().find('세무자료 파일이 정상적으로 복원되었습니다.') == 0):
        print("success")
        app['Dialog2']['확인'].click()
        app.kill()
        returnValue = {
            "success": True,
            "resultMsg": resultMsg
        };
    else:
        print(app['Dialog2']['Static'].window_text())
        app.kill()
        returnValue = {
            "success": False,
            "resultMsg": resultMsg
        };

    return returnValue


if __name__ == '__main__':
    # app.run()
    app.run(threaded=True, host='0.0.0.0')



