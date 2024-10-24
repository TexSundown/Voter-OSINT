This is a quick script to assist in OSINT pertaining to people registered to vote in the US.
The data is based on information on the target's registration, keep this in mind in case of discrepancies.


**DISCLAIMER: I am not advocating the usage of this tool for illegal purposes, only for educational purposes**





```
Usage: py voteref.py [flag] [search parameters if -s]

BASIC COMMANDS              DESC

-h                          Command to show this message

-a                          Shows all available states/state codes

-s                          Begin your search, retrieving records that match the request

-i                          Interactive mode (WIP)


SEARCH COMMANDS             DESC
-c                          State Code (AA for all states/Default)

-m                          Max number of results (High values may take longer; 25 Default)

-r                          Raw Mode (You get the full json (Make sure you save the output to a file))

-u                          Add URL to verify results(URL goes to voteref.com; Only in pretty mode)

-q                          Query String (Use quotes if more than one word)
```


##Upon downloading the tool, make sure to do pip install -r requirements.txt, since you'll need the requests-html library and the lxml html parser to make the requests.


Keep in mind as of October 2024, only 33/50 states allow the publication of their voter records, but the non profit running the site plans to have all of the states' records available. If you're not sure if the target's state is available, you can check with this tool too.