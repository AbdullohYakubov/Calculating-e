user_input = input('Enter a number for n in 𝑒=∑𝑛=0∞ 1/𝑛!=1/0!+1/1!+1/2!+1/3!+⋯+1/n! formula to calculate the value of Euler\'s Number after n terms: ')
if user_input.isnumeric():
    user_input = int(user_input)
    running_total = 0
    for i in range(user_input + 1):
        if i == 0:
            factorial = 1
        else:
            factorial = i
            for j in range(1, i):
                factorial *= j
        running_total += 1/factorial
    print(running_total)
else:
    print('Invalid Input!')