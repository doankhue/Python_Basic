numbers = [56, 14, 11, 756, 34, 90, 11, 11, 65, 0, 11, 35]

i = 0
while i<len(numbers):
    if numbers[i] == 11:
        i+=1
        continue
    j = i + 1
    while j < len(numbers):
        if numbers[j] == 11:
            j +=1
            continue
        if numbers[i] > numbers[j]:
            numberPresent = numbers[i]
            numbers[i] = numbers[j]
            numbers[j] = numberPresent
        j +=1
    i+=1
print(numbers)