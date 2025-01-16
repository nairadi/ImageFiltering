import os
rootdir = 'MLProjectSupport'
output = 'output.txt'

label = input('Enter the label to filter: ')
open(output, 'w+').close()

shouldAddFile = True
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        if 'classes.txt' in file:
            with open(os.path.join(subdir, file)) as classFile:
                contents = classFile.read()
                # print(contents)
                if label in contents:
                    shouldAddFile = True
                else:
                    shouldAddFile = False
        
        if shouldAddFile:
            if '.txt' in file or '.jpg' in file:
                with open(output, 'a') as outputFile:
                    filePath = os.path.join(subdir, file)
                    print(filePath)
                    outputFile.write(filePath + '\n')

