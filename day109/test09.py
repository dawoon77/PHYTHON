# 예외 처리
##try:
##    num=int(input('정수입력: '))
##    print('10 / %d = %d' % (num,10/num))
##except ValueError:
##    print('정수만 입력해주세요!!!')
##except ZeroDivisionError:
##    print('0으로는 나누기를 진행할수없습니다!')
##except Exception:
##    print('처리하지못하는 에러입니다.....')
##finally:
##    print('프로그램을 종료합니다.')

# 문제
'''
test.txt에 정수 1개 입력된 상황
읽어들일 파일의 이름을 입력>> apple
test.txt를 읽어들였습니다.
apple.txt는 없는 파일입니다!

1~100>> 50
DOWN!
1~49>> 25
UP!
26~49>> 32
32! 정답입니다! :D
test.txt
 3번만에 정답을 맞추셨습니다! :D

1~100>> 500
1~100이 아닙니다. 다시 입력해주세요!
(카운트에 포함되지않음)

1~100>> 오십
정수가 아닙니다. 다시 입력해주세요!
(카운트에 포함되지않음)
'''
try:
    fileName=input('읽어들일 파일의 이름을 입력>> ')
    fileName=fileName+'.txt'
    file=open(fileName,'rt')
except FileNotFoundError:
    print(fileName+'는 없는 파일입니다!')
else:
    print(fileName+'를 읽어들였습니다.')
    ans=file.read()
    file.close()
    ans=int(ans) # 정답 숫자
    cnt=0 # 시도 횟수
    L=1 # 시작 수
    H=100 # 끝 수
    while True:
        try:
            # 사용자가 입력하는 숫자
            num=int(input(str(L)+'~'+str(H)+'>> '))
        except ValueError:
            print('정수가 아닙니다. 다시 입력해주세요!')
            continue
        if num<L or H<num:
            print(str(L)+'~'+str(H)+'이 아닙니다. 다시 입력해주세요!')
            continue
        cnt+=1
        if num==ans:
            print(str(ans)+'! 정답입니다! :D')
            break
        elif num<ans:
            print('UP!')
            L=num+1
        else:
            print('DOWN!')
            H=num-1
    with open(fileName,'wt') as file:
        file.write(str(cnt)+'번만에 정답을 맞추셨습니다! :D')










    


