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


def hamming_distance(s1, s2):
    """Return the Hamming distance between equal-length sequences"""
    if len(s1) != len(s2):
        #print("Undefined for sequences of unequal length")
        return None
    return sum(el1 != el2 for el1, el2 in zip(s1, s2))

distances = []
for element in answers:
    if len(answers[element]) == None:
        pass
    elif len(answers[element]) > 1:
        sub_distances = []
        for i in answers[element]:
            sub_distances.append(hamming_distance(element,i))
        if sub_distances:
            sub_distances = [x for x in sub_distances if x is not None]
            distances.append(min(sub_distances))
    else:
        distance = hamming_distance(element,answers[element][0])
        distances.append(distance)

distances = [x for x in distances if x is not None]
print(distances)
print(sum(distances)/len(distances))



