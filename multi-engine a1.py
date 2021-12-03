import os, time

a=[ '''http://npupt.com/torrents.php?search=%s&incldead=1&nodupe=1&sort=10''',

'''https://nanyangpt.com/torrents.php?search=%s''',

'''https://byr.pt/torrents.php?search=%s''',

'''https://www.tjupt.org/torrents.php?search=%s''',

'''https://pt.eastgame.org/torrents.php?search=%s''',
'''http://pt.zhixing.bjtu.edu.cn/search/x%s/''',
'''https://thepiratebay10.org/search/%s/'''    
]

searchword=''
while True:
    while searchword=='':
        searchword=input('Searching for:')

    ##if searchword=="":
    ##    searchword="matrix"
    ##    print ("You're leaving me no choice but to search for matrix.")

    chrome = r'''C:\Users\CAM-3T\AppData\Local\Google\Chrome\Application\chrome.exe '''

    for x in a:
        cmd=chrome+'"'+x%searchword+'"'
        print(cmd)
        os.system(cmd)
        
        
    f=open(r'c:\temp\multi-engine_log.txt','a')
    f.write(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))     
    f.write("\n\n"+searchword+"\n\n")
    f.close()    
    searchword=''
    
    

    
    

