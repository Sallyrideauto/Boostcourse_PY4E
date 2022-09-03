import random

my = input("가위 바위 보! : ")
computer = random.randint(0, 2)

def rsp(my):
    if my == '가위':
        my == 0
        print("나 : 가위")
        if computer == 0:
            print("컴퓨터 : 가위")
            print("무승부")
        elif computer == 1:
            print("컴퓨터 : 바위")
            print("컴퓨터 승리!")
        elif computer == 2:
            print("컴퓨터 : 보")
            print("이겼습니다!")
    elif my == '바위':
        my == 1
        print("나 : 바위")
        if computer == 0:
            print("컴퓨터 : 가위")
            print("이겼습니다!")
        elif computer == 1:
            print("컴퓨터 : 바위")
            print("무승부")
        elif computer == 2:
            print("컴퓨터 : 보")
            print("컴퓨터 승리!")
    elif my == '보':
        my == 2
        print("나 : 보")
        if computer == 0:
            print("컴퓨터 : 가위")
            print("컴퓨터 승리!")
        elif computer == 1:
            print("컴퓨터 : 바위")
            print("이겼습니다!")
        elif computer == 2:
            print("컴퓨터 : 보")
            print("무승부")

rsp(my)