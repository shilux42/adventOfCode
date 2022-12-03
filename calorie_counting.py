with open('day1/test_input.txt') as rations:

    calories_list = []

    for line in rations:
        calories_list.append(line.replace('\n', ''))

    ration_list = []
    calories_sum = []

    for el in calories_list:
        if el != '':
            el = int(el)
            calories_sum.append(el)

        if el == '':
            ration = sum(calories_sum)
            ration_list.append(ration)
            calories_sum = []
  
    print (calories_list[-1])
    print(ration_list)