### 연습문제 1
##두자리 정수를 입력하세요.
##45
##십의 자리 4
##일의 자리 5
### 연습문제 2
##1번 점수: 20
##2번 점수: 30
##3번 점수: 40
##평균 __.__점이고, 합격입니다.
##(만약 평균이 60.0점 미만이라면 불합격)

num=int(input('두자리 정수를 입력하세요. '))
print('입력된 정수는 '+str(num)+'입니다.')
print('십의 자리 %d' % (num//10))
print('일의 자리',num%10)

print()
print()

total=0
for i in range(3):
    num=int(input('%d번 점수: ' % (i+1)))
    total+=num
print('평균 %.2f점이고, ' % round(total/3,2))
if total/3 >= 60.0 :
    print('합격입니다.')
else :
    print('불합격입니다.')

print() # 내장 함수
print()

score=[]
for i in range(3):
    score.append(int(input('%d번 점수: ' % (i+1))))
    # 메서드
avg=sum(score)/len(score)
print('평균 %.2f점이고, ' % avg)
if avg >= 60.0 :
    print('합격입니다.')
else :
    print('불합격입니다.')
















##for i in range(3):
##    print(i)
##
##    
##0
##1
##2
##aList=[10,20,30]
##for v in aList:
##    print(v)
##
##    
##10
##20
##30











##aList.append(4)
##aList.insert(0,100)
##aList
##[100, 10, 20, 30, 4]




sorted(aList)
[4, 10, 20, 30, 100]
