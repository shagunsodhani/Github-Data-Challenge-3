#! /usr/bin/python
try:
    import pymongo
except ImportError as exc:
    print("Error: failed to import settings module ({})".format(exc))


try:
    import requests
except ImportError as exc:
    print("Error: failed to import settings module ({})".format(exc))


try:
    import ast
except ImportError as exc:
    print("Error: failed to import settings module ({})".format(exc))


try:
    import db
except ImportError as exc:
    print("Error: failed to import settings module ({})".format(exc))

try:
    import os
except ImportError as exc:
    print("Error: failed to import settings module ({})".format(exc))

try:
    from ConfigParser import ConfigParser
except ImportError as exc:
    print("Error: failed to import settings module ({})".format(exc))



#---------------------------------------------------------User  Class-------------------------------------------------------------------------#


class github:

    '''
    github class to fetch and process information from Github
    '''

    def __init__(self):
        self.url = "https://api.github.com"
        config=ConfigParser()
        config.read(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'config', 'config.cfg'))
        key = config.get('github','key')
    

    def userinfo(self, uname):
        # print "shagun"
        url = self.url + "/users/"+str(uname)
        r = requests.get(url)
        if(r.status_code!=200):
            print "\nError in fetching user info from Github. Error code : "+str(r.status_code)
            print "Error message was : "+str(r.json['message'])
            print "URL was : "+str(url)
            print "\n"
        else:
            print r.json
            print type(r.json)

