#!/usr/bin/python3

import json


search = "04:92:26:da:f1:87"
search = "00:1B:C5:0C:91:87"


def maclookup(search):
    with open("macaddress.io-db.json", "r") as json_file:
        d = "[" + json_file.read()[:-1].replace("\n", ",\n") + "]"
        data = json.loads(d)
    
        ret = None
        for reg in data:
            if search.startswith(reg["oui"]):
                if ret == None:
                    ret = reg
                if len(ret["oui"]) < reg["oui"]:
                    ret = reg

        return ret
    return None


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print "Usage: " + sys.argv[0] + " address|test"
        sys.exit(1)

    if sys.argv[1] == "test":
        if maclookup("00:1B:C5:0C:91:87")["oui"] != "00:1B:C5:0C:9":
            print "FAIL"
        if maclookup("04:92:26:da:f1:87")["oui"] != "04:92:26":
            print "FAIL"
    else:
        print(maclookup(sys.argv[1]))

