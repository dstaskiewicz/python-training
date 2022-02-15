def happify(n):
    sum = 0
    for number in str(n):
        sum += int(number) ** 2
    return sum


def is_number_happy(number: int) -> bool:
    happy_number = True
    sequence = [number]
    while(happy_number and number != 1):
        number = happify(number)
        if number in sequence:
            happy_number = False
        sequence.append(number)
    
    #print(sequence)
    return happy_number

if __name__ == '__main__':
    # # Checking if one number is happy
    # number = int(input('Check if a number is happy: '))
    # is_happy = is_number_happy(number)
    # if is_happy:
    #     print('Number is not happy. :(')
    # else:
    #     print('Number is happy! :)')

    # Printing n first happy numbers
    num = int(input('How many happy numbers do you want?: '))
    happy_numbers = []
    i = 1
    while len(happy_numbers) < num:
        if is_number_happy(i):
            happy_numbers.append(i)
        i += 1
    print(f'The first {num} happy numbers are:')
    print(happy_numbers)
