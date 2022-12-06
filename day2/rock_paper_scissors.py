""" 
A = rock
B = paper
C = scissor

Y = draw
X = lose
Z = win

rock = 1
paper = 2
scissor = 3

lost = 0
draw = 3
win = 6"""

with open('day2/input.txt') as strategy_guide:
   
    player_point = 0

    for line in strategy_guide:
        elf_choise = line.split()[0]
        player_choise = line.split()[1]

        if elf_choise == 'A':
            # Y = draw X
            if player_choise == 'Y':
                # win point
                player_point += 3
                # choise point
                player_point += 1

            if player_choise == 'X':
                # win point
                player_point += 0
                # choise point
                player_point += 3

            if player_choise == 'Z':
                # win point
                player_point += 6
                # choise point
                player_point += 2
        
        if elf_choise == 'B':
            if player_choise == 'Y':
                # win point
                player_point += 3
                # choise point
                player_point += 2
            if player_choise == 'X':
                # win point
                player_point += 0
                # choise point
                player_point += 1
            if player_choise == 'Z':
                # win point
                player_point += 6
                # choise point
                player_point += 3

        if elf_choise == 'C':
            if player_choise == 'Y':
                # win point
                player_point += 3
                # choise point
                player_point += 3
            if player_choise == 'X':
                # win point
                player_point += 0
                # choise point
                player_point += 2
            if player_choise == 'Z':
                # win point
                player_point += 6
                # choise point
                player_point += 1

    print(player_point)