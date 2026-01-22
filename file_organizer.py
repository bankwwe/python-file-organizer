import os
import shutil
def movefile():
    print(os.getcwd)
    folder = input(" : ")
    if not os.path.exists(folder):
        print("not found")
        return
    extensions = {
        'Documents': ['.pdf', '.docx', '.doc', '.txt', '.pptx', '.xlsx', '.csv', '.rtf'],
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.svg', '.webp', '.heic', '.psd'],
        'Videos': ['.mp4', '.mkv', '.mov', '.avi', '.wmv'],
        'Audio': ['.mp3', '.wav', '.flac', '.m4a'],
        'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
        'Programs': ['.exe', '.msi', '.dmg', '.pkg', '.apk'],
        'Code': ['.py', '.js', '.html', '.css', '.cpp', '.json']}
    read = open('text.txt','a',encoding='utf-8')
    f = os.listdir(folder)
    c = 0
    for i in f:
        src = os.path.join(folder,i)
        if not os.path.isfile(src):
            continue
        name,ext = os.path.split(i)
        ext = ext.lower
        for catalog in extensions:
            if ext in extensions[catalog]:
                d = os.path.join(folder,catalog)
                if not os.path.exists(d):
                    os.makedirs(d)
                shutil.move(src,d)
                read.write("Move" + i + " - " + catalog + "\n")
                c +=1
                break
    a = read.write("all move: "+str(c)+ "\n")
    read.close()
    return a
a = movefile()
print(a)
   
    
