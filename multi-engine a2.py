import os, time
import win32api

a=[ '''http://npupt.com/torrents.php?search=%s&incldead=1&nodupe=1&sort=10''',

'''https://nanyangpt.com/torrents.php?search=%s''',

'''https://byr.pt/torrents.php?search=%s''',

'''https://www.tjupt.org/torrents.php?search=%s''',

'''https://pt.eastgame.org/torrents.php?search=%s''',

'''http://pt.zhixing.bjtu.edu.cn/search/x%s/''',

'''https://thepiratebay10.org/search/%s/'''

'''https://www.1377x.to/sort-search/%s/time/desc/1/'''

'''https://torrentgalaxy.mx/torrents.php?search=%s&lang=0&nox=2#results'''
]

searchword=''
while True:
    while searchword=='':
        searchword=input('Searching for:')

    ##if searchword=="":
    ##    searchword="matrix"
    ##    print ("You're leaving me no choice but to search for matrix.")

    #chrome = r'''C:\Users\CAM-3T\AppData\Local\Google\Chrome\Application\chrome.exe'''

    chrome = r'''"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"'''

    #chrome = '''chrome '''

    print('testing chrome')
    os.system(chrome)
    print ('testing complete.')


    for x in a[:3]:
        url=x%searchword
        cmd=chrome+' "'+x%searchword+'"'
        print(cmd)
        #os.system(cmd)
        win32api.ShellExecute(0, 'open', chrome, url , '', 1)

    f=open(r'c:\temp\multi-engine_log.txt','a')
    f.write(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    f.write("\n\n"+searchword+"\n\n")
    f.close()
    searchword=''





