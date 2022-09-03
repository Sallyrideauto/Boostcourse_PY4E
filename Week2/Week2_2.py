monthly_payment = int(input())
year_income = monthly_payment * 12

def yearly_payment(monthly_payment):
    if year_income <= 1200:
        reduce_tax = year_income - year_income * 6 / 100
        print("세전 연봉 : ", year_income, "만원")
        print("세후 연봉 : ", int(reduce_tax), "만원")
    elif year_income >= 1200 and year_income <= 4600:
        reduce_tax = year_income - year_income * 15 / 100
        print("세전 연봉 : ", year_income, "만원")
        print("세후 연봉 : ", int(reduce_tax), "만원")
    elif year_income >= 4600 and year_income <= 8800:
        reduce_tax = year_income - year_income * 24 / 100
        print("세전 연봉 : ", year_income, "만원")
        print("세후 연봉 : ", int(reduce_tax), "만원")
    elif year_income >= 8800 and year_income <= 15000:
        reduce_tax = year_income - year_income * 35 / 100
        print("세전 연봉 : ", year_income, "만원")
        print("세후 연봉 : ", int(reduce_tax), "만원")
    elif year_income >= 15000 and year_income <= 30000:
        reduce_tax = year_income - year_income * 38 / 100
        print("세전 연봉 : ", year_income, "만원")
        print("세후 연봉 : ", int(reduce_tax), "만원")
    elif year_income >= 30000 and year_income <= 50000:
        reduce_tax = year_income - year_income * 40 / 100
        print("세전 연봉 : ", year_income, "만원")
        print("세후 연봉 : ", int(reduce_tax), "만원")
    elif year_income > 50000:
        reduce_tax = year_income - year_income * 42 / 100
        print("세전 연봉 : ", year_income, "만원")
        print("세후 연봉 : ", int(reduce_tax), "만원")

yearly_payment(monthly_payment)