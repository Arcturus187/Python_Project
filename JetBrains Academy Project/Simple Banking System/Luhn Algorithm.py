import random

def checksum(num):
    num = [int(x) for x in num]
    del_num = []
    app_num = []
    for x in num[::-2]:
        del_num.append(x)
        app_num.append((x * 2))
    for i in del_num:
        num.remove(i)
    for i in app_num:
        num.append(i)
    for x in num:
        if x > 9:
            num.remove(x)
            num.append(sum([int(i) for i in str(x)]))
    checksum_digit = str((10 - (sum(num) % 10)) % 10)
    return checksum_digit






tmp_list = []
for i in range(9):
    tmp_list.append(str(random.randint(0, 9)))
tmp_list = ''.join(tmp_list)
card_num = f"400000{tmp_list}" # No Checksum Digit
checksum(card_num)
card_num = card_num + checksum(card_num)


print(card_num)