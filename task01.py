number_N = int(input("Enter integer number "))


def printing_N_numbers(N):
    if N == 1:
        print(N)
    else:
        print(N)
        printing_N_numbers(N - 1)


printing_N_numbers(number_N)
