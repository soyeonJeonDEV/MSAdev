#if문

grade = {'홍길동1' : {'국어':95, '영어':90, '수학':80, '과학':50},
         '홍길동2' : {'국어':100, '영어':50, '수학':90, '과학':90},
         '홍길동3' : {'국어':99, '영어':60, '수학':100, '과학':40},
         '홍길동4' : {'국어':55, '영어':80, '수학':80, '과학':60}}
         
resultInSum = []
resultInAvg = []
resultSum = 0
resultAvg = 0

def sumAvg(key):
    sumIn = sum(grade[key].values())
    resultInSum.append(sumIn)
    resultInAvg.append(sumIn/len(grade[key]))

for key in grade:
    if key == '홍길동1':
        sumAvg(key)

    elif key == '홍길동2':
        sumAvg(key)
        
    elif key == '홍길동3':
        sumAvg(key)

    elif key == '홍길동4':
        sumAvg(key)

resultSum = sum(resultInSum)
resultAvg = resultSum/len(grade)

temp = 0