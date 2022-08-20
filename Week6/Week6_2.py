import numpy as np

member_names = ["갑돌이", "갑순이", "을돌이", "을순이", "병돌이", "병순이"]   # 이름
member_records = [[4, 5, 3, 5, 6, 5, 3, 4, 1, 3, 4, 5],
                  [2, 3, 4, 3, 1, 2, 0, 3, 2, 5, 7, 2],
                  [1, 3, 0, 3, 3, 4, 5, 6, 7, 2, 2, 1],
                  [3, 2, 9, 2, 3, 5, 6, 6, 4, 6, 9, 9],
                  [8, 7, 7, 5, 6, 7, 5, 8, 8, 6, 10, 9],
                  [7, 8, 4, 9, 5, 10, 3, 3, 2, 2, 1, 3]] # 실적을 나타내는 2차원 배열 리스트

def sales_management(member_names, member_records):

    # Numpy 배열 연산을 활용하여 판매원들의 실적 평균 구하기
    member_records = np.array(member_records)
    member_records = member_records.mean(axis = 1)
    member_records = member_records.astype(int)
    print(member_records)

    sales_dict = dict(zip(member_names, member_records)) # 판매원들의 정보가 담길 딕셔너리
    print(sales_dict)

    sales = []

    for k, v in sales_dict.items():
        sales.append((v, k))

    sales = sorted(sales, reverse = True) # 평균 실적이 높은 순부터 내림차순 정렬
    print(sales)

    for x, y in sales:
        if x >= 5:
            print("보너스 대상자", y)
        if x < 3:
            print("면담 대상자", y)

sales_management(member_names, member_records)