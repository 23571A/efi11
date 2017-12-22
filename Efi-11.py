from time import strftime, sleep
from getpass import getuser
from platform import system
from pathlib import Path
import os, itertools, json, sys, random
debug = 1
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
pathtd = ("%s%s%s" % (paths, pathm, pathd))
if not os.path.exists(pathtd):
        os.makedirs(pathtd)
        new = 1
if not pathtf.is_file():
        f = open(pathtf,'w')
        f.write('{"rtimes": 0}')
        f.close()

save = open(pathtf, 'r')
initj = save.read()
save.close()
initd = json.loads(initj)
locals().update(initd)
rtimes = rtimes + 1
def writee():
        d = {'rtimes':rtimes, 'name':name, 'isFeeling':isFeeling}
        dtop = json.dumps(d)
        f = open(pathtf, 'w')
        f.write(dtop)
        f.close()
t = 0
sleep(1.5)
print('Loading Efi-11 ©')
while not t == 101:
        print("%d%%" % t)
        sleep(0.1)
        t = t + 1
print('Loaded')
hello = ['Hello...', 'Hi.', 'Hello there!', 'Hello!']
dk = ['Who are you?, I have no idea', '''I... don't know you''', '''I don't know you''', '''It seems that I do not know you''']
wiyn = ['What is your name?', 'Can you tell me your name?', 'Could you tell me your name?'] 
hatf = ['How are you feeling today', 'How are you', 'How you feelin today']
sleep(1)
dkd = random.choice(dk)
hellod = random.choice(hello)
wiynd = random.choice(wiyn)
hatfd = random.choice(hatf)
print("%s" % hellod)
sleep(0.8)
if rtimes == 1:
    print("%s" % dkd)
    sleep(1)
    print("%s" % wiynd)
    sleep(0.5)
    print("Be sure to type your name, your whole name, and nothing but your name")
    name = input('')
    print("OK then, %s" % name)
    writee()
    print("Please restart this script...")
    sleep(1000000000000)
print("%s, %s?" % (hatfd, name))
isFeeling = input('')
