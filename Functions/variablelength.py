def sum(*elements):  #* is used to variable length argruments elements became tuple
    res = 0
    for x in elements:
        res = res+x
    return res

print(sum(10,20))
print(sum(10,20,30))
print(sum(10))
print(sum())


def sum2(int_sum, *element):
    res = int_sum
    for x in element:
        res=res+x
    return res

print(sum2(10,20,30))


def printElements(*elements2):
    print(elements2)

printElements(101,"abc",100)  #traverse the tuple elements


#keyword variable length argruments
def printDetails(** details):
    for d, v in details.items():
        print(f"{d} is {v}")
