import os
list_of_possible_tags = ['JUDGMENT BY:', 'JUDGMENT OF:', 'JUDGE1', 'JUDGE2', 'CORAM:', 'THE']
for file in os.listdir('d:\\txt\\'):
    if file.endswith(".txt"):
        if os.path.isfile('d:\\txtutf\\' + file) == False:
            print('d:\\txt\\' + file)
            with open('d:\\txt\\' + file, 'rb') as f:
                with open('d:\\txtutf\\' + file, 'w+b') as dest_file:
                    contents = f.read()
                    dest_file.write(contents.decode('utf-16').encode('utf-8'))