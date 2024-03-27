# We use the built-in open() to open files.

#file = open('nameoffile', 'r')
# content = file.read()
# file.close

with open('skinnyfile.txt', 'r') as file:
    contents = file.read()
    print(contents)

with open('skinnyfile1.txt', 'w') as file:
    contents = file.write('Hello Skinny')
    print(contents)

    file.seek(0)
    updated_content = file.write('File 101.')
    print(updated_content)
    file.close()

