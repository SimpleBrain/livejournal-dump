import os, requests, sys
from os import path
##credit for the code goes to https://github.com/HarryC145/
topnumber = 1199999
##top number as of midnight 28th feb 2015 is 3542090
found = 0
currentnumber = 1100001
while currentnumber <= topnumber:
    checked = format(currentnumber)
    url = "http://ext-" + checked + ".livejournal.com/feed/"
    ##http://ext-NUMBER.livejournal.com/feed/
    request = requests.get(url, allow_redirects=False)
    if request.status_code == 200:
        SitePresent = open("present-1100001-1199999.txt", "a")
        SitePresent.write(url + '\n')
        SitePresent.close()
        print('I found a site, at', url)
        found = found + 1
        print(found)
    else:
        print('I looked for a site at', url, 'and I did not see anything')
        notfound = open("notfound-1100001-1199999.txt", "a")
        notfound.write(url + '\n')
        notfound.close()
    currentnumber = currentnumber + 1
