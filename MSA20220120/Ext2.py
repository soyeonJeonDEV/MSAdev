# while 문

grade = {'홍길동1' : {'국어':95, '영어':90, '수학':80, '과학':50},
         '홍길동2' : {'국어':100, '영어':50, '수학':90, '과학':90},
         '홍길동3' : {'국어':99, '영어':60, '수학':100, '과학':40},
         '홍길동4' : {'국어':55, '영어':80, '수학':80, '과학':60}}
         
resultInSum = []
resultInAvg = []
resultSum = 0
resultAvg = 0

i = 0

name = ['홍길동1','홍길동2','홍길동3','홍길동4']

while i < len(grade):
    sumIn = sum(grade[name[i]].values())
    resultInSum.append(sumIn)
    resultInAvg.append(sumIn/len(grade[name[i]]))
    resultSum = resultSum + sumIn
    i = i+1
    
resultAvg = resultSum/len(grade)

temp = 0