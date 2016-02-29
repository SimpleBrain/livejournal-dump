import os, requests, time, sys
from os import path
##credit for the code goes to https://github.com/HarryC145/
<<<<<<< HEAD
topnumber = 6999999
##top number as of midnight 28th feb 2015 is roughly 77536449
found = 0
currentnumber = 3000000
=======
total = len(sys.argv)
cmdargs = str(sys.argv)
print ("The total numbers of args passed to the script: %d " % total)
print ("Args list: %s " % cmdargs)
topnumber = sys.argv[2]
##top number as of midnight 28th feb 2015 is roughly 77536449
found = 0
currentnumber = int(sys.argv[1])
>>>>>>> 45132f770053d1c3f14f0647e6aa15575ed17289
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
        time.sleep(1.5)
    else:
        print(stcode + " Error " +  url + " Not there")
        notfound = open("Profile-notfound-" + stnumber + "-" + format(topnumber) + ".txt", "a")
        notfound.write(url + '\n')
        notfound.close()
        time.sleep(3)
    currentnumber = currentnumber + 1
