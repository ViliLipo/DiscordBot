


def parse_osrs_request(request):
    l = False
    request = request.replace("!osrsstats", "")
    requet = request.replace("!osrsStats", "")
    if request.find(' -l ') != -1:
        l = True
        #print("long requested")
        request = request.replace('-l', "")
        #request = request.strip(" ")
        #print(request)
    if request.find('"') != -1:
        player = request.split('"')[1]
        #player = request.replace('"', "")
    else:
        player = request.strip()

    return player, l




def testdriver():
    print(parse_osrs_request("!osrsStats -l Klassi"))
    print(parse_osrs_request('!osrsStats "vihaan mamui"'))
    print(parse_osrs_request('!osrsStats -l "vihaan mamui"'))

#testdriver()
