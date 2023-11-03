# 실습 문제 진짜 해결 답안 ㅋㅋㅋㅋㅋ

##1. 랜덤으로 1~5 사이의 정수를 생성해주세요.
import random as r

def func(aList):
    return sum(aList)/len(aList) 

randNum=r.randrange(1,6)
print('randNum=',randNum)
##2. 3 -> 3개의 정수를 사용자가 직접 입력합니다.
##    이때 입력하는 값은 0이상 100이하의 정수이며,
##    이 입력은 절대 틀리지않습니다.
numList=[]
for i in range(randNum):
    num=int(input('0이상 100이하의 정수 입력: '))
    numList.append(num)
print(numList)
##3. 50 60 55 입력시,
##3-1. 60점 1등 2번학생
##3-2. 50점 3등 1번학생
numList.reverse()
maxIndex=randNum-numList.index(max(numList))
minIndex=randNum-numList.index(min(numList))
print('%d점 %d등 %d번학생' % (max(numList),1,maxIndex))
print('%d점 %d등 %d번학생' % (min(numList),randNum,minIndex))
numList.reverse()
##    이렇게 출력해주세요.
##    동점자 존재시 가장 마지막 학생을 출력합니다.
##4. 사용자 정의 함수 func()을 사용하여
##    3명의 평균점수는 55.0점입니다.
##    이렇게 출력해주세요.
avg=func(numList)
print('%d명의 평균점수는 %.1f점입니다.' % (randNum,avg))






