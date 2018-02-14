
import requests
import re





def osrs_request(playername):
    API_ENDPOINT = "http://services.runescape.com/m=hiscore_oldschool/index_lite.ws"
    PARAMS = {'player':playername}
    r = requests.get(url=API_ENDPOINT, params=PARAMS)
    content = (r.text)
    #print(content)
    lines = content.split('\n')

    datatable = []

    for line in lines:
        dataline=[]
        txtline = line.split(',')
        for s in txtline:
            try:
                dataline.append(int(s))
            except:
                continue
        datatable.append(dataline)

    message = playername + "'s OSRS Hi Scores \noverall rank : "+ str(datatable[0][0]) + "\n" +"total level : " + str(datatable[0][1]) + "\n" + "total xp: " + str(datatable[0][2]) + "\n"
    return message

#print(osrs_request('Klassi'))
