S = input()
arr = []
answer = ""
for string in S:
    str_to_ascii = ord(string)
    if str_to_ascii  in range(97, 123):
        if str_to_ascii in range(97, 110):
            asciiROT13 = (str_to_ascii)+13
            arr.append(chr(asciiROT13))
        elif str_to_ascii in range(110, 123):
            asciiROT13 = (str_to_ascii)-13
            arr.append(chr(asciiROT13))
    elif str_to_ascii  in range (65, 91):
        if str_to_ascii in range(65, 78):
            asciiROT13 = str_to_ascii+13
            arr.append(chr(asciiROT13))
        else:
            asciiROT13 = str_to_ascii-13
            arr.append(chr(asciiROT13))
        
    else :
        arr.append(chr(str_to_ascii))
        
print(answer.join(arr))