korea_king = "태조,혜종,정종,광종,경종,성종,목종,현종,덕종,정종,문종,순종,선종,헌종,숙종,예종,인종,의종,명종,신종,희종,강종,고종,원조,충렬왕,충선왕,충숙왕,충혜왕,충목왕,충정왕,공민왕,우왕,창왕,공양왕"
chosun_king = "태조,정종,태종,세종,문종,단종,세조,예종,성종,연산군,중종,인종,명종,선조,광해군,인조,효종,현종,숙종,경종,영조,정조,순조,헌종,철종,고종,순종"

def king(korea, chosun):

    king_dict = dict() # 왕 이름이 담길 딕셔너리

    # 왕의 이름들을 쉼표 단위로 분할한 뒤 리스트로 변경
    korea = korea_king.split(',')
    chosun = chosun_king.split(',')

    # print('고려시대 왕 :', korea)
    # print('조선시대 왕 :', chosun)

    # 왕들의 이름이 담긴 리스트를 합침
    kings = korea + chosun
    # print(kings)

    for king in kings:
        king_dict[king] = king_dict.get(king, 0) + 1
    # print('Kings', king_dict)

    # 중복되는 왕 이름을 삽입하는 리스트 생성
    King_list = []
    for (k, v) in king_dict.items():
        if v >= 2:
            King_list.append(k)

    count = 0 # 카운트 변수
    for king in King_list:
        print(f"조선과 고려에 모두 있는 왕 이름 : {king}")
        count = count + 1 # 존재하면 +1
    print("조선과 고려에 모두 있는 왕 이름은 총", len(King_list), "개 입니다.")

king(korea_king, chosun_king)
