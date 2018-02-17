import requests
import json


class GrandExhangeService:
    baseurl = 'http://services.runescape.com/m=itemdb_oldschool'
    def __init__(self):
        fileObject = open('objects_87.json', "r")
        self.items = json.load(fileObject)
        fileObject.close()
    def parseCommand(self, command):
        itemname = command.replace("!osrsGE", "")
        itemname = itemname.strip()
        #print(itemname)
        return itemname
    '''
    Finds id for itemname
    '''
    def findIdForName(self, name):
        match = []
        ids = []
        for di in self.items:
            if (di['name'].lower().find(name.lower()) != -1):
                match.append(di)
                if di['name'].lower() == name.lower():
                    return [int(di['id'])]
        if (len(match) > 0):
            #print("got matches")
            for m in match:
                ids.append(int(m['id']))
            return ids
        else:
            return -1

    def fetchItem(self, itemId):
        url = self.baseurl +'/api/catalogue/detail.json'
        PARAMS = {'item':itemId}
        r = requests.get(url=url, params=PARAMS)
        if(r.status_code != 200):
            raise Exception ("Could not connect to API")
        #print(r.text)
        decoder = json.JSONDecoder()
        item = decoder.decode(r.text)
        #print(item)
        return item

    def message(self, command):
        itemname = self.parseCommand(command)
        ids = self.findIdForName(itemname)
        if (ids == -1):
            raise Exception("Malformed itemname")
            return
        if len(ids) < 11:
            items = []
            for id in ids:
                 item = self.fetchItem(id)
                 items.append(item)
            ms = ""
            if (len(items) > 1):
                ms = "Found {} items \n".format(str(len(items))) \
                + '------------\n'
            for item in items:
                ms = ms + item['item']['name'] + '\n' \
                + item['item']['description'] + '\n' \
                + 'Price :' + str(item['item']['current']['price']) + '\n'\
                + '-------------\n'
        else:
            ms = "Found {} items \n".format(str(len(ids))) \
            + "Please specify \n" \
            + '------------\n'
        return ms
