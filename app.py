from os import listdir
import os, requests, re
##

def is_broken(url):
    # return true or false depending if the link is broken
    pass

def get_file_links(file_path):
    links = []
    # given a file path, get file content and then get the links inside the content
    # return an array of url
    return links

def list_files(path):
    report = {
        "levels": 0, #LISTO
        "total_files_found": 0, #LISTO
        "total_folders_found": 0,#LISTO
        "broken_links_found": 0,#LISTO
        "links_found": 0, #LISTO
        "files_found": [],#LISTO
        "file_extentions_found": [],
    }
    # this function must loop all the files and directories and update the report 
    # variable accordingly
    #### FILES #####
    files = []
    extension_list=[]
    filesCont=0
    level=0
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            files.append(os.path.join(r, file))
            #print(file)
            extension=file.split('.')[1]
            extension_list.append(extension)
            filesCont=filesCont+1
        report["total_files_found"]=filesCont
        report["files_found"]=files
        report["file_extentions_found"]=extension_list
        level=level+1 

    report["levels"]=level    
    #### FOLDERS ######
    folderCont=0
    def listdirs(folder):
        return [d for d in os.listdir(folder) if os.path.isdir(os.path.join(folder, d))]
    
    totalFolder=listdirs(path)
    contFolder=0
    for x in totalFolder:
        contFolder=contFolder+1
    report["total_folders_found"]=contFolder                     
     
    #### LINKS FOUND HTTP OR HTTPS ######
    links = []
    links_count=0
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if ('.http' or '.https') in file:
                links.append(os.path.join(r, file))
                
    report["links_found"]=links_count      
    
    #### BROKEN LINKS FOUND HTTP OR HTTPS ######  
    if links_count==0:
        report["broken_links_found"]=0
         
    for x in  report:
        print(x,': ',report[x])
    
    #return report

list_files('./data-files')
#print(list_files('./data-files'))


    
    
