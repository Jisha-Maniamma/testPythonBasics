def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mul(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


operator={}
operator["+"]=add
operator["-"]=sub
operator["*"]=mul
operator["/"]=div

print(operator)