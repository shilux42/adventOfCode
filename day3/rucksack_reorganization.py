def rucksack_splitter(rucksack):
    # Split the "stringsack" in 2 string and return 2 compartment for a rucksack 
    last_item = len(rucksack)
    pointer = int(last_item / 2)

    first_compartment = rucksack[0:pointer]
    second_compartment = rucksack[pointer:last_item]

    return(first_compartment, second_compartment)

priorities = []

def matching_counter(first_compartment, second_compartment):
 
    # Check for the item present in both compartment
    for item in first_compartment:
        
        if item in second_compartment:

            if item not in in_both_compartment:
                in_both_compartment.append(item)

def priorities_counter(in_both_compartment):
    # Assign the priorities for every items
    if len(in_both_compartment) != 0:
        for item in in_both_compartment:
            if ord(item) > 90:
                item_priorities = ord(item) - 96
            else:
                item_priorities = ord(item) - 38

        priorities.append(item_priorities)
    return priorities
    
with open('day3/input.txt') as rucksacks_list:
    for rucksack in rucksacks_list:
        new_rucksack = rucksack.replace('\n', '')
        in_both_compartment = []

        first_compartment, second_compartment = rucksack_splitter(new_rucksack)
        matching_counter(first_compartment, second_compartment)
    
        priorities_counter(in_both_compartment)
    
    print(sum(priorities))