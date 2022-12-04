with open('day1/input.txt') as rations:

    calories_list = ''
    elf_bag = []
    first_bag = 0
    second_bag = 0
    third_bag = 0

    # append all the value to a list
    for line in rations:
        calories_list += line

    splitted_list = calories_list.split('\n')

    for line in splitted_list:
        if line != '':
            elf_bag.append(int(line))
        if line == '':

            calories_sum = sum(elf_bag)

            if calories_sum > first_bag:
                third_bag = second_bag
                second_bag = first_bag
                first_bag = calories_sum
            elif calories_sum > second_bag:
                third_bag = second_bag
                second_bag = calories_sum
            elif calories_sum > third_bag:
                third_bag = calories_sum

            elf_bag = []
        
    print(first_bag, second_bag, third_bag)
    print (first_bag + second_bag + third_bag)


