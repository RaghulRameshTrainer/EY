'''
modes:
-----
read(r) -> Read the file. File should be present to read the content of it.
            if the file does not exist , will get the FileNotFoundError
write(w)  -> Write the file. If the file exists then it will remove/clean the
            content of the file and start writing as a fresh file. If the file does not
            exists, it will create and write it
append(a) -> Append the file. If the file exists then it will NOT remove/clean the
            content of the file instead it start appending along with existing content.
             If the file does not exists, it will create and write it
read-write (r+) -> File must be there to read and write after you read. Instead of reading
                    first if you start writing into it, it will overwrite the existing content.
write-read(w+) -> need to write and read what is written.
read binary (rb) - to read the special file (Video, audio, image)
write binary (wb)   - to write a binary files  (Video, audio, image)

Read:
    read(), readline(), readlines()
write/append:
    write(), writelines()
'''

# with open(filename, mode) as file_object:
#     file_object.read/write
"""
with open('days.txt','r') as fo:
    #print(fo.read())
    # print(fo.readline(),end='')
    # print(fo.readline(),end='')
    # print(fo.readline())
    print(fo.readlines()[1:6])


with open('techology.txt','w') as fo:
    fo.writelines(['Python\n','Java\n','Spark\n','GenAI\n','AWS\n','Django'])

with open('techologys.txt','a') as fo:
    fo.writelines(['DevOps\n','Andoid\n','IOT\n','RPA'])

with open('days.txt','r+') as file_obj:
    print(file_obj.read())
    file_obj.write('JANUARY-1')

with open('days.txt','w+') as fo:
    fo.writelines(['India\n','America\n','Canada\n','Japan\n','England'])
    fo.seek(0,0)
    print(fo.read())



with open(r'C:\Users\DELL\Pictures\sunflower.jpg','rb') as fo:
    with open(r'C:\Users\DELL\Pictures\sunflower_16032024.jpg', 'wb') as wbf:
        wbf.writelines(fo.readlines())