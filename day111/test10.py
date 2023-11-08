'''
1. csv 파일을 다뤄야한다!
2. .py 파일(모듈 파일, 동작시킬 스크립트 파일)과 같은 디렉터리에 csv 파일이 존재해야한다!
'''
import csv

with open('a.csv','r',encoding='cp949') as file:
    data=csv.reader(file,delimiter=',')

    # 헤더 별도로 저장하기
    header=next(data) # 이터레이터, rs.next()와 유사한 함수
    print(header)
    
    maxTemp=0.0
    maxDate=''
    for row in data:
        if row[4]=='': # ValueError 에러 처리 코드
            row[4]=0.0
        row[-1]=float(row[-1]) # 데이터 형 변환
        if maxTemp <= row[-1]:
            maxTemp=row[-1]
            maxDate=row[0]

print(maxTemp)
print(maxDate)





# 초급
# 최저기온은 언제였을까요?

# 중급
# 날짜를 입력하면 해당날짜의 평균기온을 출력해주세요!~~
# 단, "해당 날짜에는 데이터가 존재하지않습니다!"를 출력해주세요!~~

# 고급
# 데이터가 없는 날을 제외한 모든 날들의 평균 기온을 알려주세요!











    
