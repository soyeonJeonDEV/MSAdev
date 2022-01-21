import json

# \mydata.json 파일 읽어오기
try:
    jsonFile = open("MSA20220121\\mydata.json","rb")
    tempData = json.load(jsonFile)

    resultData1 = tempData["name"]
    resultData2 = tempData["age"]
    resultData3 = tempData["address"]
    resultData4 = tempData["email"]
    resultData5 = tempData["empcheck"]

except Exception as error:
    print("error : " + error)

else:
    jsonFile.close()

# JSON 데이터 
jsonData1 = {
        "empid": 12345678,
        "name" : "홍길동",
        "info" : [
            {"date1": "2022-01-21", "home": "서울시"},
            {"dep": "개발", "email": "aaa@aaa.co.kr"}
        ]
    }

# 한줄로 JSON 파일 만들기 \mydata2.json
try : 
    writeFile = open("MSA20220121\\mydat2.json","w")
    json.dump(jsonData1, writeFile)

except Exception as error:
    print("error : " + error)

else:
    writeFile.close()

# 한줄로 JSON 파일 + 한글 변환 \mydata3.json
try : 
    writeFile = open("MSA20220121\\mydat3.json","w", encoding='utf-8')
    json.dump(jsonData1, writeFile,ensure_ascii=False)

except Exception as error:
    print("error : " + error)

else:
    writeFile.close()

# JSON 파일 indent \mydata4.json
try : 
    writeFile = open("MSA20220121\\mydat4.json","w")
    json.dump(jsonData1, writeFile,ensure_ascii=False, indent=4)

except Exception as error:
    print("error : " + error)

else:
    writeFile.close()

# 한글 + indent \mydata5.json
try : 
    writeFile = open("MSA20220121\\mydat5.json","w", encoding='utf-8')
    json.dump(jsonData1, writeFile,ensure_ascii=False, indent=4)

except Exception as error:
    print("error : " + error)

else:
    writeFile.close()


temp = 0
