
card_list = []
drop_list = []
N = int(input())

for i in range(1, N + 1):
    card_list.append(i)

#카드를 버리고 뒤로 보내고 이 두가지의 반복
while card_list:
    # 카드 버리기
    drop_card = card_list.pop(0)
    drop_list.append(str(drop_card))
    if not card_list:
        break

    # 카드 뒤로 보내기
    back_to_list = card_list.pop(0)
    card_list.append(back_to_list)

    if not card_list:
        break


print(' '.join(drop_list))

    




