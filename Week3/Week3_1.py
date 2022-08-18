# Q1. 숫자를 입력 받고 그 숫자의 구구단을 출력하는 함수 생성
# 조건
# 1 : 홀수 번째만 출력하기
# 2 : 값이 50 이하인 것만 출력하기

num = int(input("몇 단? : "))
print(num, "단")

for gugudan in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    if num * gugudan >= 50:
        if gugudan % 2 == 1:
            continue
    print(num, "X", gugudan, "=", num * gugudan)



