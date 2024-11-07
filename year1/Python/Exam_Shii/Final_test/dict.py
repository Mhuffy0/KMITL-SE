def find_r(start, routes):
    result_value = 0
    result_routes = []
    
    for i,j in routes:
        if start == i :
            for k,v in routes:
                result_routes.append(k)
                result_value += v
                
routes = {"a": 1,
          "b": 2,
          "c": 3
          }

print(find_r("a",routes)) #กูแตก ไอสัด