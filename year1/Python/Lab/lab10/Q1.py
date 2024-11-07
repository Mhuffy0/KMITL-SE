def name_list(count):
    list = []
    for i in range(count):
        i+=1
        name = str(input(f"Enter name {i} : "))
        if name == "":
            break

        list.append(name)
        name = ""
    print(list)
    
name_list(5)