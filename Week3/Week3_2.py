import random

games = int(input("몇 판을 진행하시겠습니까? : "))

def rsp_advanced(games):

    my_score = []
    pc_score = []
    draw = []

    for i in range(games):
        my = input("가위 바위 보! : ")
        computer = random.randint(0, 2)

        if my == '가위':
            my == 0
            print("나 : 가위")
            if computer == 0:
                print("컴퓨터 : 가위")
                print(i + 1, "번째 판 무승부!")
                draw.append(i + 1)
            elif computer == 1:
                print("컴퓨터 : 바위")
                print(i + 1, "번째 판 컴퓨터 승리!")
                pc_score.append(i + 1)
            elif computer == 2:
                print("컴퓨터 : 보")
                print(i + 1, "번째 판 나의 승리!")
                my_score.append(i + 1)
        elif my == '바위':
            my == 1
            print("나 : 바위")
            if computer == 0:
                print("컴퓨터 : 가위")
                print(i + 1, "번째 판 나의 승리!")
                my_score.append(i + 1)
            elif computer == 1:
                print("컴퓨터 : 바위")
                print(i + 1, "번째 판 무승부!")
                draw.append(i + 1)
            elif computer == 2:
                print("컴퓨터 : 보")
                print(i + 1, "번째 판 컴퓨터 승리!")
                pc_score.append(i + 1)
        elif my == '보':
            my == 2
            print("나 : 보")
            if computer == 0:
                print("컴퓨터 : 가위")
                print(i + 1, "번째 판 컴퓨터 승리!")
                pc_score.append(i + 1)
            elif computer == 1:
                print("컴퓨터 : 바위")
                print(i + 1, "번째 판 나의 승리!")
                my_score.append(i + 1)
            elif computer == 2:
                print("컴퓨터 : 보")
                print(i + 1, "번째 판 무승부!")
                draw.append(i + 1)
        else:
            print("다시 입력하세요")

    print(my_score)
    print(pc_score)
    print(draw)

    print("나의 전적 : ", len(my_score), "승", len(draw), "무", len(pc_score), "패")
    print("컴퓨터의 전적 : ", len(pc_score), "승", len(draw), "무", len(my_score), "패")

rsp_advanced(games)