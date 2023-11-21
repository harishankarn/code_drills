def convert_string_to_int_list(val):

    l = val.split(" ")
    l_int = [eval(k) for k in l]

    return l_int

# T stands for test cases
T = int(input())
answer = []

for i in range(T):

    lis = convert_string_to_int_list(input())

    # A is number
    A = lis[0]

    # N is number of times looped for power of A
    N = lis[1]

    if 2 <= N <= 10**9:
        if -10**9 <= A <= 10**9:
            if A != 0:
                # when A is negative
                if A < 0:
                    value = 1

                #when A is positive
                else:
                    value = A**(N/2)

                answer.append(int(value % ((10**9)+7)))


for i in range(len(answer)):
    print(answer[i])