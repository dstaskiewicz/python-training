import random

def monty_hall(strategy):
    # set the prize behind a random door
    prize = random.randint(0, 2)
    doors = [0, 1, 2]

    door_chosen = strategy[0]

    doors_not_chosen = doors
    doors_not_chosen.pop(door_chosen)

    if prize == door_chosen:
        # prize behind chosen door -> random door out of the other two
        doors_not_chosen.pop(random.randint(0, 1))
    else:
        # prize behind one not chosen door -> the other not opened door
        for door in doors_not_chosen:
            if door != prize:
                i = door
        doors_not_chosen.pop(doors_not_chosen.index(i))
    
    #open one door with no prize
    
    does_swap = strategy[1]

    # print(doors_not_chosen)

    if does_swap:
        door_chosen = doors_not_chosen[0]
    
    if door_chosen == prize:
        return 1
    else:
        return 0


def main():
    strategies = [
        {
            'name': 'Alice',
            'counter': 0,
        },
        {   
            'name': 'Bob',
            'counter': 0,
        },
        {   
            'name': 'Carol',
            'counter': 0,
        },
        {   
            'name': 'Dave',
            'counter': 0,
        },
        {   
            'name': 'Erin',
            'counter': 0,
        },
    ]

    # name = input('Choose your strategy (Alice, Bob): ')
    # for strat in strategies:
    #     if strat['name'] == name.lower():
    #         strategy = strat

    for _ in range(1000):
        strategies[0]['counter'] += monty_hall((0, False))
        strategies[1]['counter'] += monty_hall((0, True))
        strategies[2]['counter'] += monty_hall((random.randint(0, 2), random.choice((True, False))))
        strategies[3]['counter'] += monty_hall((random.randint(0, 2), False))
        strategies[4]['counter'] += monty_hall((random.randint(0, 2), True))
    for strategy in strategies:
        print(f'{strategy["name"]} won {strategy["counter"]} times.') 
    

if __name__ == '__main__':
    main()