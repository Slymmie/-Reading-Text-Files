
def read_file(filename):
    open_file = open ("C:/Users/user/Desktop/ZURI/PY/Reading-Text-Files/story.txt","r")
    read_file = open_file.read()

    new = read_file.split()

    count = {}
    for i in new:
        if i in count:
            count [i] += 1
        else:
            count[i] = 1
    return count
print(read_file("C:/Users/user/Desktop/ZURI/PY/Reading-Text-Files/story.txt"))