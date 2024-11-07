def maximumSwap(num):
    if len(str(num)) <= 1 :
        return num
    else :
        temp = [int(i) for i in str(num)]
        if temp[0] == temp [1]:
            nums = int(''.join(map(str, temp)))
            return nums
        
        else : 
            temp[0],temp[1] = temp[1],temp[0]
            nums = int(''.join(map(str, temp)))
            formatted_num = "{:02}".format(nums)
            return formatted_num

num = 10

print(maximumSwap(num))
