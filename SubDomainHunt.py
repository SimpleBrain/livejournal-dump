import os, requests, time, sys
from os import path
##credit for the code goes to https://github.com/HarryC145/
total = len(sys.argv)
cmdargs = str(sys.argv)
print ("The total numbers of args passed to the script: %d " % total)
print ("Args list: %s " % cmdargs)
topnumber = sys.argv[2]
##top number as of midnight 28th feb 2015 is 3542090
found = 0
currentnumber = int(sys.argv[1])
stnumber = format(currentnumber)
while currentnumber <= topnumber:
    checked = format(currentnumber)
    url = "http://ext-" + checked + ".livejournal.com/feed/"
    ##http://ext-NUMBER.livejournal.com/feed/
    request = requests.get(url, allow_redirects=False)
    if request.status_code == 200:
        SitePresent = open("found-" + stnumber + "-" + str(topnumber) + ".txt", "a")
        SitePresent.write(url + '\n')
        SitePresent.close()
        print('I found a site, at', url)
        found = found + 1
        print(found)
        time.sleep(0.25)
    else:
        print('I looked for a site at', url, 'and I did not see anything')
        notfound = open("notfound-" + stnumber + "-" + str(topnumber) + ".txt", "a")
        notfound.write(url + '\n')
        notfound.close()
        time.sleep(0.5)
    currentnumber = currentnumber + 1
