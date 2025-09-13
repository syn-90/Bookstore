import random
def create_ranom_code(size):
    var = ""
    for i in range(size):
        var +=str(random.choice(range(0,10)))
    return var


def group_list(seq , size):
    group = []
    coll = range(0 , len(seq) , size)
    for i in coll:
        group.append(seq[i : i + size])
    return group

