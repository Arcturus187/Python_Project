text = input()
box = []

while True:
    counter = 0
    max_counter = len(text[1:])
    for i in text[1:]:
        if i.isupper():
            upper_index = text.index(i, 1)
            box.append(text[0:upper_index])
            text = text[upper_index:]
            break
        else:
            counter += 1
            if counter >= max_counter:
                box.append(text)
                break
    if counter >= max_counter:
        break
    
print('_'.join(box).lower())
