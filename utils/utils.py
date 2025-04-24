import random
def create_ranom_code(size):
    var = ""
    for i in range(size):
        var +=str(random.choice(range(0,10)))
    return var