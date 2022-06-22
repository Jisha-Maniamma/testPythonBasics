data = [0, 1, 0.5, 3, 2.5, 2, 1.5]
for i in range(len(data)):
    for j in range(len(data) - 1):
        if data[j] > data[j + 1]:
            temp = data[j]
            data[j] = data[j + 1]
            data[j + 1] = temp


print(data)
