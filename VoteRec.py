#VoteRef.com CLI
#By Tex
from requests_html import HTMLSession
import sys
request = HTMLSession()

#Dependencies: requests-html   == 0.10.0
#              lxml_html_clean ==  0.3.1

#If state is specified, 'state' is appended to the url
def getStates():
    states = eval(request.get(url ='https://voteref.com/state/map').text)
    validStates = 'State Code           State Name\n\nAA                   All States\n'
    for state in states:
        if state['status'] == 2:
            validStates += f"{state['stateCode']}                   {state['stateName']}\n"
    print(f'{validStates}\nMore states will be added as laws are passed regarding publishing records')

def help():
    print('''This is a quick script to assist in OSINT pertaining to people registered to vote in the US.
The data is based on information on the target's registration, keep this in mind in case of discrepancies.

DISCLAIMER: I am not advocating the usage of this tool for illegal purposes, only for educational purposes

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
          ''')
    
def search(args):
    #Remove unnecessary args
    args.pop(0)
    args.pop(0)
        
    #Default for state code is left blank intentionally.
    sc = ''
    #If state is specified, 'state' is appended to the url
    url = 'https://voteref.com/voter/grid/'
    m = 25
    #Default value is false, so every state is searched
    singleState = False
    #Output will have name, address, and age only when pretty is true. Else will show every value retrieved from endpoint
    pretty = True
    #Additional line added to response where user can check url to verify data
    link = False
    query = ''
    while len(args) > 0:
        match args.pop(0):
            case '-c':
                sc = args.pop(0)
                singleState = sc != 'AA'
            case '-m':
                m = int(args.pop(0))
            case '-r':
                pretty = False
            case '-u':
                link = True
            case '-q':
                query = args.pop(0)
    payload = {"columns":[{"data":"fullName","name":"","searchable":True,"orderable":True,"search":{"value":"","regex":False}},{"data":"address","name":"","searchable":True,"orderable":False,"search":{"value":"","regex":False}},{"data":"dobOrAge","name":"","searchable":True,"orderable":False,"search":{"value":"","regex":False}},{"data":"numberOfTimesVoted","name":"","searchable":True,"orderable":False,"search":{"value":"","regex":False}},{"data":"party","name":"","searchable":True,"orderable":False,"search":{"value":"","regex":False}}],"draw":2,"length":m,"order":[{"column":0,"dir":"asc"}],"searchText":query,"start":0}

    if singleState:
        url += 'state/'
        payload["state"] = sc
    
    ask = request.post(url=url, json=payload)
    raw = eval(ask.text.replace('null', 'None'))
    verifyUrl = ''
    if pretty:
        for person in raw['data']:
            if link:
                verifyUrl = f"https://voteref.com/VoterDetails?personId={person['personId']}&state={person['state']}"
            print(f"{person['fullName']:30s}  {person['dobOrAge']}   {person['address']}     {verifyUrl}")
    else:
        print(raw)
        
    

def interactiveMode():
    pass

def main():
    try:
        x = sys.argv
        match x[1].lower():
            case '-h':
                help()
            case '-a':
                getStates()
            case '-s':
                search(x)
            case '-i':
                interactiveMode()
    except IndexError:
        help()
            
main()