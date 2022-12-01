with open('input.txt', 'r') as f:
    lines = f.readlines()
    elfs = []
    counter = 0
    for l in lines:
        if l != "\n":
            counter += int(l)      
        else:
            elfs.append(counter)
            counter = 0
      
#part 1 output
print(max(elfs))

elfs.sort(reverse=True)
#part 2 output
print(elfs[0] + elfs[1] + elfs[2])