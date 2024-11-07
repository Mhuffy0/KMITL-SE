def find_int(str):
    digits = '0123456789'
    result = ""
    
    for i in str:
        if i in digits :
            result += i
    return result

print(find_int('23abd 888 fdfds25')) #FUCKK YEAHHHHH
print(find_int('no')) #
        