answers = {}
with open('./results','r') as file1:
    lines = file1.readlines()
    for line in lines:
        print(line)
        key, value = line.split(' ')
        key, value = key[:],value[:-1]
        if key in answers:
            if value in answers[key]:
                continue
            else:
                answers[key].append(value)
        else:
            answers[key] = [value]
[print(element,answers[element]) for element in answers] 


result = 0
for element in answers:
    for value in answers[element]:
        print(value,element)
        if element == value:
            result += 1
print(result)
print(len(answers))
