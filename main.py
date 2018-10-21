import random as rd
import sys
from tempfile import mkstemp
from shutil import move
from os import fdopen, remove, system
from shutil import copyfile

USERNAME = 'johan'

#Colors are stored in this array, you can add or removes colors to your preference:
colors = ['fff9c7','38999c','52bec2','fefdef','fad3cf','a797c8','2776a5','1d1d1b','c50a66','edc613','ef790e','fff9c7','2c2457','223b6f','de7778','f3f0ef','11334c',
'155894','f5f6e7','ea6215','de0b3c','2089a8','164e5a','3097bb','f9f5c2','f1b876','d65969','263579','306ab2','3cbee9','bee3ef','f6a119','29a13d','26a8ac','2487c8',
'1fa1c3','f3c418','77b86d','ee713d','3b2257','bc0e74','eb5b2b','fae614','fab734','ee7338','67c3cc']

def replace(file_path, pattern, subst):
    """Replace line in file"""
    #Create temp file
    fh, abs_path = mkstemp()
    with fdopen(fh,'w') as new_file:
        with open(file_path) as old_file:
            for line in old_file:
                if pattern in line:
                    new_file.write(subst)
                else:
                    new_file.write(line)
    #Remove original file
    remove(file_path)
    #Move new file
    move(abs_path, file_path)

#Start

if len(sys.argv) == 1:
    print("Error no arguments specified:", "- bash: Change color every time the terminal is open", "- planned: Change color every week", sep='\n')
elif sys.argv[1] == "bash":
    #Choose a color
    color = colors[rd.randint(0,len(colors)-1)]
    #Copy the file as backup
    copyfile('/home/'+USERNAME+'/.config/i3/config', '/home/'+USERNAME+'/.config/i3/config.clbak')
    #Replace i3lock color
    replace('/home/'+USERNAME+'/.config/i3/config', "bindsym $mod+l exec i3lock -f -c", "bindsym $mod+l exec i3lock -f -c "+color+"\n")
    #Reload i3config
    system("i3-msg reload > /dev/null")
