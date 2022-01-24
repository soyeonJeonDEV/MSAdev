from flask import Flask
import json
import requests

app = Flask(__name__) 
app.config['JSON_AS_ASCII'] = False # 한글 변환
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True # json 깔끔하게 출력

@app.route("/") 
def FlaskLab(): 
    return "Flask 데이터 응답" 

@app.route("/data1")
def FlaskData():
    keyValue = r"p7zGkmRh2x32vu%2BuvThZkvgWgBnug8qu2YB%2F3AQHyOERlV3SqETp1UPGubmd5La2plHZDURFlgotkT1ctC6b2g%3D%3D"
    keyDeValue = r"p7zGkmRh2x32vu+uvThZkvgWgBnug8qu2YB/3AQHyOERlV3SqETp1UPGubmd5La2plHZDURFlgotkT1ctC6b2g=="

    dataURL = "http://api.odcloud.kr/api/apnmOrg/v1/list?"
    dataURL += "page=" + str(1) + "&perPage=" + str(10)
    dataURL += "&cond" + r"%5BorgZipaddr%3A%3ALIKE%5D=%EA%B0%95%EB%82%A8%EA%B5%AC" # 강남구
    dataURL += "&serviceKey=" + keyValue

    dataResult = requests.get(dataURL)

    # coronaData.json 파일 저장
    with open("coronaData.json","w", encoding="utf-8") as writeFile:
         json.dump(dataResult.text, writeFile, ensure_ascii=False, indent='4', separators=(',', ': '))
            
    # dataResult 화면 출력
    return json.loads(dataResult.text)


