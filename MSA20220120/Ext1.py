# 4개의 과목을 합계 + 평균(개인 평균 / 전체 평균)
# 홍길동1 {'국어':95, '영어':90, '수학':80, '과학':50}
# 홍길동2 {'국어':100, '영어':50, '수학':90, '과학':90}
# 홍길동3 {'국어':99, '영어':60, '수학':100, '과학':40}
# 홍길동4 {'국어':55, '영어':80, '수학':80, '과학':60}

# for /while /if / elif
# 5가지 방법으로 코드를 작성 : 결과는 모두 같아야함

grade = {'홍길동1' : {'국어':95, '영어':90, '수학':80, '과학':50},
         '홍길동2' : {'국어':100, '영어':50, '수학':90, '과학':90},
         '홍길동3' : {'국어':99, '영어':60, '수학':100, '과학':40},
         '홍길동4' : {'국어':55, '영어':80, '수학':80, '과학':60}}
         
resultInSum = []
resultInAvg = []
resultSum = 0
resultAvg = 0

for key,value in grade.items():
    sumIn = sum(value.values())
    resultInSum.append(sumIn)
    resultInAvg.append(sumIn/len(value))
    resultSum = resultSum + sumIn

resultAvg = resultSum/len(grade)

temp = 0
