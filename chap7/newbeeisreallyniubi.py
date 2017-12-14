def sum _to_even(lst):
    mysum = 0
    for i in lst:
        if i % 2 ==0:
            break
        mysum += i
        return mysum
    
def sum(lst):
    count = 1
    for i in lst:
        if i == "Sum":
            count += 1
            break
        count += 1
    return count


test_suite()
