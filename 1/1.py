inputfile = open('real_input.txt', 'r')
list = inputfile.readlines()
newList = [];
numbers = [];

for element in list:
    newList.append(element.strip())

for element in newList:
    numbers.append(int(element))

# PART 1
# increased = 0;
# for i in range(len(numbers)):
#     if numbers[i] > numbers[i - 1]:
#         increased += 1

# print(increased)

# PART 2
increased = 0;
for i in range(len(numbers)):
    if  len(numbers) <= i + 3:
        print('final count:', increased)
        break
    else:
        firstWindow = numbers[i] + numbers[i + 1] + numbers[i + 2];
        secondWindow = numbers[i + 1] + numbers[i + 2] + numbers[i + 3];
        print(f'{secondWindow} > {firstWindow}')
        if secondWindow > firstWindow:
            increased += 1;

print(increased)