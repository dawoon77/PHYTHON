# C:\Users\Administrator\AppData\Local\Programs\Python\Python312

# 파일 입출력

##파일 객체=open('파일명.확장자', '모드')
##file=open('test.txt', 'wt')
##wt 파일 쓰기 모드
##rt 파일 읽기 모드
##at 파일 이어쓰기 모드
##file.close()

##with문
##close()를 포함하는 문법
##with open('파일명','모드') as 파일객체:
##    pass

with open('test.txt','wt') as file:
    while True:
        tmp=input('입력: ')
        if not tmp:
            break
        file.write(tmp)
        file.write('\n')

with open('test.txt','rt') as file:
    tmp=file.read()
    print(tmp)








