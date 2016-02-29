# livejournal-dump

This is a multi part site scrape

1. ext-NUMBER scrape (~3.5million id's) 1-3500000
2. profile id scrape (~77.5million id's) 1-77000000

Once those have been done, all the links will be tested to see if they have a journal. Once that has been filtered, a livejournal grab will be organised.

Current test shows if you grab 1 per 2 seconds, you wont get banned. Please adjust python scripts to suit your machine.  Line: time.sleep() 0.75 to 2 is fine.


# SubDomainHunt.py

Use the following command to run:
python SubDomainhunt.py startnumber endnumber
