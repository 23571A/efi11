from time import strftime, sleep #For waiting and getting localtime
from getpass import getuser #for determining where files go
from platform import system
from pathlib import Path #to turn strings to paths
import os, itertools, json, sys, random #save system modules
from tkinter import * #gui
debug = True #in case of problems
new = False
pathm = getuser()
OS = system()
if OS == 'Windows':
    paths = 'C:\\Users\\'
    pathe = '\\Efi-11\\save.json'
    pathd = '\\Efi-11'
elif OS == 'Linux':
    paths = '/home/'
    pathe = '/Efi-11/save.json'
    pathd = '/Efi-11/'
elif OS == 'Darwin':
    paths = '/Users/'
    pathe = '/Efi-11/save.json'
    pathd = '/Efi-11/'
pathtf = Path("%s%s%s" % (paths, pathm, pathe))
if debug == True:
        print('File save.json should be located at', pathtf)
pathtd = ("%s%s%s" % (paths, pathm, pathd))
if not os.path.exists(pathtd):
        os.makedirs(pathtd)
        new = True
        if debug == True:
                print('Created folder Efi-11 at', pathtd)
if not pathtf.is_file():
        f = open(pathtf,'w')
        f.write('{"rtimes": 0}')
        f.close()
        new = True
        if debug == True:
                print('Created save.json in folder', pathtd)
if debug == True and new == False:
        print('Reading save.json at', pathtf)
save = open(pathtf, 'r')
initj = save.read()
save.close()
if debug == True:
        print('Converting JSON data to python dictionary')
initd = json.loads(initj)
if debug ==True:
        print('Initilizing variables')
locals().update(initd)
rtimes = rtimes + 1
tk = Tk()
win = Label(tk)
win.pack()

tk.update()
def wprint(t):
        win.config(text=str(t))
        if debug == True:
                print('Printing', t, 'to tk')
        tk.update()
def writee():
        d = {'rtimes':rtimes, 'name':name, 'isFeeling':isFeeling}
        dtop = json.dumps(d)
        f = open(pathtf, 'w')
        f.write(dtop)
        f.close()
sleep(1.5)
wprint('Loading Efi-11')
tk.update()
sleep(1.5)
wprint('Loaded')
sleep(1)
wprint('Hello!')
sleep(1)
if rtimes == 1:
    wprint('Let me introduce myself')
    sleep(2.08)
    wprint('I am Efi-11, a sort of smart AI (artafical intellegence)')
    sleep(4.09)
    wprint('What is your name?')
    sleep(1.21)
wprint('How are you feeling %s' % name)
isFeeling = input('')
