name = input()
score = int(input())

def grader(name, score):
    if score >= 95 and score <= 100:
         print("학생이름 : ", name)
         print("점수 : ", score, "점")
         print("학점 : ", "A+")
    elif score >= 90 and score <= 94:
         print("학생이름 : ", name)
         print("점수 : ", score, "점")
         print("학점 : ", "A")
    elif score >= 85 and score <= 89:
         print("학생이름 : ", name)
         print("점수 : ", score, "점")
         print("학점 : ", "B+")
    elif score >= 80 and score <= 84:
         print("학생이름 : ", name)
         print("점수 : ", score, "점")
         print("학점 : ", "B")
    elif score >= 75 and score <= 79:
         print("학생이름 : ", name)
         print("점수 : ", score, "점")
         print("학점 : ", "C+")
    elif score >= 70 and score <= 74:
         print("학생이름 : ", name)
         print("점수 : ", score, "점")
         print("학점 : ", "C")
    elif score >= 69 and score <= 65:
         print("학생이름 : ", name)
         print("점수 : ", score, "점")
         print("학점 : ", "D+")
    elif score >= 60 and score <= 64:
         print("학생이름 : ", name)
         print("점수 : ", score, "점")
         print("학점 : ", "D")
    else:
        print("학생이름 : ", name)
        print("점수 : ", score, "점")
        print("학점 : ", "F")

grader(name, score)