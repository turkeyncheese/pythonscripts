def life_path_number(birthdate):
    birthdate = birthdate.replace('-', '')
    res = 0
    for num in birthdate: 
        res += int(num)
      
        if res > 9: 
            res = res % 10 + res // 10
    return res
