age = int(input())
payment = input()

def bus_fare(age, payment):
    if age < 8:
        if payment == "카드":
            print("나이 : ", age, "세")
            print("지불유형 : 카드")
            print("버스요금 : 무료")
        else:
            print("나이 : ", age, "세")
            print("지불유형 : 현금")
            print("버스요금 : 무료")
    if age >= 8 and age < 14:
        if payment == "카드":
            print("나이 : ", age, "세")
            print("지불유형 : 카드")
            print("버스요금 : 450원")
        else:
            print("나이 : ", age, "세")
            print("지불유형 : 현금")
            print("버스요금 : 450원")
    if age >= 14 and age < 20:
        if payment == "카드":
            print("나이 : ", age, "세")
            print("지불유형 : 카드")
            print("버스요금 : 720원")
        else:
            print("나이 : ", age, "세")
            print("지불유형 : 현금")
            print("버스요금 : 1000원")
    if age >= 20 and age < 75:
        if payment == "카드":
            print("나이 : ", age, "세")
            print("지불유형 : 카드")
            print("버스요금 : 1200원")
        else:
            print("나이 : ", age, "세")
            print("지불유형 : 현금")
            print("버스요금 : 1300원")
    else:
        if payment == "카드":
            print("나이 : ", age, "세")
            print("지불유형 : 카드")
            print("버스요금 : 무료")
        else:
            print("나이 : ", age, "세")
            print("지불유형 : 현금")
            print("버스요금 : 무료")

bus_fare(age, payment)