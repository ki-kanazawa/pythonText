number = [1,2,3,3,4,4,5,5,6,6,6,6,2,3,4,5,3,5]
count_disc = {}
for num in number :
    if num in count_disc:
        count_disc[num] += 1
    else :
        count_disc[num] = 1

print(count_disc)