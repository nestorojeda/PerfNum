def fileToArray(file):
    global int_list
    with open(file) as f:
        return [int(x) for x in f]