total_sum = 0
last_num = None
for _ in range(5):
    num = int(input("Enter a integer: "))
    if last_num != None and (last_num < 0) != (num < 0):
        total_sum = 0
    total_sum += num
    last_num = num
    print("Current sum:", total_sum)