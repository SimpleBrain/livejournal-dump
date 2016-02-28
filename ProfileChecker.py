import os, requests, time, sys
from os import path
##credit for the code goes to https://github.com/HarryC145/
topnumber = 20
##top number as of midnight 28th feb 2015 is roughly 77536449
found = 0
currentnumber = 1
stnumber = format(currentnumber)
while currentnumber <= topnumber:
    checked = format(currentnumber)
    url = "http://www.livejournal.com/profile?userid=" + checked + "&t=I"
    ##http://www.livejournal.com/profile?userid=77536449&t=I
    request = requests.get(url, allow_redirects=False)
    stcode = format(request.status_code)
    if request.status_code == 200:
        SitePresent = open("Profile-found-" + stnumber + "-" + format(topnumber) + ".txt", "a")
        SitePresent.write(url + '\n')
        SitePresent.close()
        print(format(found) +  "/" + checked + " (200) Site found: " + url)
        found = found + 1
        time.sleep(0.75)
    else:
        print(stcode + " Error " +  url + " Not there")
        notfound = open("Profile-notfound-" + stnumber + "-" + format(topnumber) + ".txt", "a")
        notfound.write(url + '\n')
        notfound.close()
        time.sleep(1)
    currentnumber = currentnumber + 1
