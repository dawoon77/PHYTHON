# 함수 3요소 == 메서드 시그니처(JAVA)
# 인자, 인수, input, 입력값, 매개변수, args, 파라미터, ...
# 반환값, 리턴값, return, 출력값, 결과값, output, ...
# 함수의 기능 == 함수명

# 사용자 정의 함수
# 함수 선언,정의
# 함수를 사용하려면 호출해야함
def printApple():
    print('apple')

# 함수의 장점
# 코드 재사용 용이
# 오류의 파급효과 절감
# 개발 시간,비용 절감
# 유지보수 용이

def funcA(a):
    print('a=',a)

def funcB(b):
    print('b=',b)
    return b
##funcB(-13)
##b= -13
##-13
### 에코
##banana=funcB(-13)
##b= -13
##banana
##-13

def funcC():
    return 1234

def funcD():
    for i in range(10):
        pass

def funcE(*a): # 애스터리스크 / 가변 매개변수
    print(a)
    print(type(a)) # 가변 매개변수는 튜플 타입으로 넘어옴
    for v in a:
        print (v)

def funcF(a,b='apple',c=123): # 디폴트 매개변수
    print('a=',a)
    print('b=',b)
    print('c=',c)






print('안녕하세요!',end=' ')
print('ㅎㅎㅎ')
print('파이썬 2일차입니다! :D')
# print() 함수에게는 end라는 인자값이 있었고,
# end는 디폴트 매개변수 값으로 '\n'를 갖고 있었다!





















