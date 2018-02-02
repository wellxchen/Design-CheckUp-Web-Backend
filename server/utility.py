import re
from categories import categories
import json

class utility ():
    def makeMap(rules, main, sub):
        res = ""
        for rule in rules:
            if sub > 0:
                res = res + "'" + rule + "' : ['" + main + "'," + str(sub) + "],\n"
            else:
                res = res + "'" + rule + "': ['" + main + "'],\n"

        return res

    def striphtml(self, data):
        p = re.compile(r'<.*?>')
        p = p.sub('', data)
        p = p.replace('&lt;', '<')
        p = p.replace('&gt;', '>')
        p = p.replace('&le;', '<=')
        p = p.replace('&ge;', '>=')
        return p

    def errHandler (self):
        data = {}
        data['err'] = "project not found"
        data['description'] = "please change the file name and extension for xml.txt to pom.xml and yml.txt to .gitlab-ci.yml"
        return json.dumps(data)

    def dataHandler(self, message, percentage):
        data = {}
        data['error'] = {}
        data['error']['Communication'] = {}
        data['error']['Communication']['Meaningful names'] = {}
        data['error']['Communication']['Meaningful names']["category description"] = categories().Communication_Sub[1]
        data['error']['Communication']['Meaningful names']["detail"] = message[0][0]

        data['error']['Communication']['No magic values'] = {}
        data['error']['Communication']['No magic values']["category description"] = categories().Communication_Sub[2]
        data['error']['Communication']['No magic values']["detail"] = message[0][1]

        data['error']['Communication']['Readable code'] = {}
        data['error']['Communication']['Readable code']["category description"] = categories().Communication_Sub[3]
        data['error']['Communication']['Readable code']["detail"] = message[0][2]

        data['error']['Communication']['Use scope wisely'] = {}
        data['error']['Communication']['Use scope wisely']["category description"] = categories().Communication_Sub[4]
        data['error']['Communication']['Use scope wisely']["detail"] = message[0][3]

        data['error']['Communication']['Same level code'] = {}
        data['error']['Communication']['Same level code']["category description"] = categories().Communication_Sub[5]
        data['error']['Communication']['Same level code']["detail"] = message[0][4]

        data['error']['Communication']['Concise code'] = {}
        data['error']['Communication']['Concise code']["category description"] = categories().Communication_Sub[6]
        data['error']['Communication']['Concise code']["detail"] = message[0][5]

        data['error']['Communication']['No warning'] = {}
        data['error']['Communication']['No warning']["category description"] = categories().Communication_Sub[7]
        data['error']['Communication']['No warning']["detail"] = message[0][6]

        data['error']['Modularity'] = {}
        data['error']['Modularity']['Data responsibility'] = {}
        data['error']['Modularity']['Data responsibility']["category description"] = categories().Modularity_sub[1]
        data['error']['Modularity']['Data responsibility']["detail"] = message[1][0]

        data['error']['Modularity']['No public instance variables'] = {}
        data['error']['Modularity']['No public instance variables']["category description"] = \
        categories().Modularity_sub[2]
        data['error']['Modularity']['No public instance variables']["detail"] = message[1][1]

        data['error']['Modularity']['No manager classes'] = {}
        data['error']['Modularity']['No manager classes']["category description"] = categories().Modularity_sub[3]
        data['error']['Modularity']['No manager classes']["detail"] = message[1][2]

        data['error']['Modularity']['No static variables'] = {}
        data['error']['Modularity']['No static variables']["category description"] = categories().Modularity_sub[4]
        data['error']['Modularity']['No static variables']["detail"] = message[1][3]

        data['error']['Modularity']['Active classes'] = {}
        data['error']['Modularity']['Active classes']["category description"] = categories().Modularity_sub[5]
        data['error']['Modularity']['Active classes']["detail"] = message[1][4]

        data['error']['Modularity']['Get method give minimum info'] = {}
        data['error']['Modularity']['Get method give minimum info']["category description"] = \
        categories().Modularity_sub[6]
        data['error']['Modularity']['Get method give minimum info']["detail"] = message[1][5]

        data['error']['Modularity']['Get method validate input'] = {}
        data['error']['Modularity']['Get method validate input']["category description"] = categories().Modularity_sub[
                                                                                               7],
        data['error']['Modularity']['Get method validate input']["detail"] = message[1][6]

        data['error']['Modularity']['Superclasses are their own class'] = {}
        data['error']['Modularity']['Superclasses are their own class']["category description"] = \
        categories().Modularity_sub[8]
        data['error']['Modularity']['Superclasses are their own class']["detail"] = message[1][7]

        data['error']['Flexibility'] = {}
        data['error']['Flexibility']['No duplicated code'] = {}
        data['error']['Flexibility']['No duplicated code']["category description"] = categories().Modularity_sub[1]
        data['error']['Flexibility']['No duplicated code']["detail"] = message[2][0]

        data['error']['Flexibility']['General type'] = {}
        data['error']['Flexibility']['General type']["category description"] = categories().Modularity_sub[2]
        data['error']['Flexibility']['General type']["detail"] = message[2][1]

        data['error']['Flexibility']['Single Purpose'] = {}
        data['error']['Flexibility']['Single Purpose']["category description"] = categories().Modularity_sub[3]
        data['error']['Flexibility']['Single Purpose']["detail"] = message[2][2]

        data['error']['Flexibility']['Behavior Driven Design'] = {}
        data['error']['Flexibility']['Behavior Driven Design']["category description"] = categories().Modularity_sub[4]
        data['error']['Flexibility']['Behavior Driven Design']["detail"] = message[2][3]

        data['error']['Flexibility']['Polymorphism'] = {}
        data['error']['Flexibility']['Polymorphism']["category description"] = categories().Modularity_sub[5]
        data['error']['Flexibility']['Polymorphism']["detail"] = message[2][4]

        data['error']['Java Notes'] = message[3]
        data['error']['Code Smells'] = message[4]
        data['percentage'] = {}
        data['percentage']['Communication'] = percentage[0]
        data['percentage']['Modularity'] = percentage[1]
        data['percentage']['Flexibility'] = percentage[2]
        data['percentage']['Java Notes'] = percentage[3]
        data['percentage']['Code Smells'] = percentage[4]

        return data