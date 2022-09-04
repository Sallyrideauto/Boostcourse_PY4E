age = int(input("나이를 입력하세요 : "))
birth = int(input("생일이 지났습니까? 맞으면 0 아니면 -1 : "))

if birth == 0:
    print("미국식 나이로", age, "살 입니다.")
elif birth == -1:
    print("미국식 나이로", age + birth, "살 입니다.")
else:
    print("다시 입력하세요.")