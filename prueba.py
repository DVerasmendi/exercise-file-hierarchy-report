from os import listdir
import os, requests, re
##

# def listdirs(folder):
#     return [d for d in os.listdir(folder) if os.path.isdir(os.path.join(folder, d))]

# listdirs('./data-files')
# print(listdirs('./data-files'))


path = './data-files'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        files.append(os.path.join(r, file))
 
extension_list=[]
for f in files:
    #print(f)
    extension=f.split('/')[1]
    extension=extension.split('.')[1]
    extension_list.append(extension)
    print(extension)
    
# print('HOLAAAA')    
# print(level)
# file2 = []
# # r=root, d=directories, f = files
# for r, d, f in os.walk(path):
#     for file in d:
#         file2.append(os.path.join(r, file))

# for f2 in file2:
#     print(f2)
    
# print('HOLAAAA2')    
# file3 = []
# # r=root, d=directories, f = files
# for r, d, f in os.walk(path):
#     for file in r:
#         file3.append(os.path.join(r, file))

# for f3 in file3:
#     print(f3)
