import os, itertools

def traverse(path):
    current = 0
    matches_dir = []
    matches_file = []
    for root, directory, file_name in os.walk(path, topdown=False):
        for namePath, nameFile in itertools.izip_longest(directory, file_name):
            if namePath != None:
                new_path = os.path.join(root, namePath)
                matches_dir.append(new_path)
            if nameFile != None:
                new_file = os.path.join(root, nameFile)
                matches_file.append(new_file)

    matches_dir = sorted(matches_dir)
    matches_file = sorted(matches_file)
    
    for dir_sub in matches_dir:
        amount =  len(dir_sub.split("/"))-1
        print "-" * amount, dir_sub.split("/")[-1]
        for dir_file in matches_file:
            if dir_file.split("/")[0:-1] == dir_sub.split("/"):
                print "--" * amount, dir_file.split("/")[-1]
    '''for dir_file in matches_file:
        print dir_file'''

dir_path = raw_input("Enter path: ")
print "Your path: " + dir_path
traverse(dir_path)
