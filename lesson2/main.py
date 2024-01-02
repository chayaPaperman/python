def find_primes(num):
    mylist = []
    flag = False
    for num in range(num):
        flag = False
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    flag = True
            if not flag:
                mylist.append(num)
    return mylist


def sort_list(mylist):
    return sorted(mylist)

#def calculate_expression(expression):