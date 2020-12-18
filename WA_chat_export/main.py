# opening the whatsapp chat export file
read = open("./input.txt", 'r')
lines = read.readlines()  # readind the individual lines of the text file

output = []  # this varianle contains a list of seperated datas
names = []  # this variable will store all names in the whatsapp chat export file
main_output = []
for line in lines:
    line = line.replace('\n', ' ')
    if line[0] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
        # checking if the first letter is a number
        if line.find(': ') != -1:  # checking if the line has ': '
            if line.find('AM - ') != -1 or line.find('PM - ') != -1:  # checking if the line has ' - '
                divide = line.split(': ',1)
                if divide[0].find('created group') != -1 or divide[0].find('changed the subject from ') != -1:
                    continue
                else:
                    try:
                        temp1 = []  # declaring a variable that will temporarily store datas in a line
                        temp2 = []  # declaring a variable that will temporarily store splitted datas
                        # splitting with respect to ', '
                        temp2 = line.split(', ', 1)
                        # appending the first part to temp1 and second part to line
                        temp1.append(temp2[0])
                        line = temp2[1]
                        # splitting with respect to ' - '
                        temp2 = line.split(' - ', 1)
                        # appending the first part to temp1 and second part to line
                        temp1.append(temp2[0])
                        line = temp2[1]
                        # splitting with respect to ': '
                        temp2 = line.split(': ', 1)
                        # appending the first part to temp1 and second part to line
                        temp1.append(temp2[0])
                        temp1.append(temp2[1])
                        # appending the information to output array
                        output.append(temp1)
                        if names.count(temp1[2]) == 0:
                            names.append(temp1[2])
                    except:
                        continue
    else:
        if len(output) != 0:
            output.append(['', '', '', line])
print('choose names from the following: ')
for i in range(0, len(names)):
    print(f'\t{i}. {names[i]}')
print(f'\t{i+1}. ALL')
numbers = input(
    'Enter numbers of the corresponding names\n(use comma for multiple numbers): ')
numbers = numbers.split(',')
required_names = []

for i in numbers:
    if int(i) == len(names):
        required_names = names
        break
    required_names.append(names[int(i)])

format = input('enter a file format([csv/txt]): ')
last_index = 0
if format == 'csv':
    main_output.append('Date`Time`Name`Message\n')
    for i in range(0, len(output)):
        if output[i][2] != '':
            last_index = i

        if required_names.count(output[i][2]) != 0:
            main_output.append(f'{output[i][0]}`{output[i][1]}`{output[i][2]}`{output[i][3]}\n')
        elif output[i][2] == '':
            if required_names.count(output[last_index][2]) != 0:
                main_output.append(f'{output[i][0]}`{output[i][1]}`{output[i][2]}`{output[i][3]}\n')
elif format=='txt':
    for i in range(0, len(output)):
        space = map(lambda x: len(x), required_names)
        space = list(space)
        space.sort(reverse = True)
        temp = ''

        if output[i][2] != '':
            last_index = i
        for j in range(0, space[0]):
            temp += ' '
        if required_names.count(output[i][2]) != 0:
            tem1 = ''
            for k in range(0,len(temp)-len(output[i][2])):
                tem1+= ' '
            main_output.append(f'{tem1}{output[i][2]}: {output[i][3]}\n')
        elif output[i][2] == '':
            if required_names.count(output[last_index][2]) != 0:
                main_output.append(f'{temp+"  "}{output[i][3]}\n')
else:
    print('[error] Invalid format')
# closing the file
read.close()
# opening the csv file (output file)
write = open('./output.csv' if format == 'csv' else './output.txt', 'w')
write.writelines(main_output)  # writing all the lines in the csv file
write.close()  # closing the csv file
print('success!!')
