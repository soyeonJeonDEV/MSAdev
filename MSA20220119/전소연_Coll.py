# 1. 딕션어리를 이용해서 평균 점수 구하기
grade = {'국어':95, '영어':90, '수학':80, '과학':50}

resultAvgGrade = sum(grade.values())/len(grade)

# 2. set 을 이용해서 1~100까지 숫자 중에 공배수를 구함 : 5와 3의 공배수를 구하고, 합집합 구하기
#    : 표현식을 이용하면 쉽다.
resultFive = {i for i in range(1,101) if i%5==0}
resultThree = {i for i in range(1,101) if i%3==0}

resultUnion = resultFive | resultThree

# 3. 리스트 데이터 : 7,5,3,1,-1,-3,-5,-7 출력 : range 활용하기
listData = [i for i in range(7,-8,-2)]

# 4. 3번째의 결과를 튜플로 변경(형변환)
tupleData = tuple(listData)

temp = 0
