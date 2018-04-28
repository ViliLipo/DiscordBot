

def parse_osrs_request(request):
    longOption = False
    request = request.replace("!osrsstats", "")
    request = request.replace("!osrsStats", "")
    if request.find(' -l ') != -1:
        longOption = True
        # print("long requested")
        request = request.replace('-l', "")
        # request = request.strip(" ")
        # print(request)
    if request.find('"') != -1:
        player = request.split('"')[1]
        # player = request.replace('"', "")
    else:
        player = request.strip()

    return player, longOption
