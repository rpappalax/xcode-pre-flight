import json
from decimal import Decimal


import requests


URL = "https://xcodereleases.com/data.json"
DOMAIN = "https://download.developer.apple.com/Developer_Tools/"
MAX_VERSION = 11.3


# query API on a cron job
# store results in a pickle

# compare yesterday to today

# if diff, then download new xcode(s)
# handler for if more than one

# install xcode - silent install
# install xcode build tools - silent install

# git clone of firefox-ios

# ./bootstap.sh

# xcodebuild firefox-ioso

# message results somewhere???
# run this on Jenkins, we could message to slack

def version_num(item):
     return '{0}: {1}'.format(item['name'], item['version']['number'])


def release_info(item):
    v =item['version']['release']
    return next(iter(v))


def store():
    pass


def version_name(url):
    tmp =url.split(DOMAIN)[1].split('/')[0]
    return tmp.replace('.', '_')


def download(req, url, ver_name):
    f = requests.get(url)
    out_file = '{0}.xip'.format(ver_name)
    open(out_file, 'wb').write(f.content)


def printout(v, rel_info):
    print(v)
    print(rel_info)
    print('====================')

#def main():
r = requests.get(URL)

j = r.json()
d = json.dumps(j, sort_keys=True, indent=4)

for item in j:
   parts = item['version']['number'].split('.')
   v = '0'
   if len(parts) > 2:
       v = '{0}.{1}'.format(parts[0], parts[1])
  
   if Decimal(v) > MAX_VERSION:
       if item['name'] == "Xcode":


           # XCODE VERSION NUM
           v = version_num(item)

           # PRINT RELEASE INFO
           rel_info = release_info(item)
           printout(v, rel_info)

           # DOWNLOAD INSTALL FILE
           url = item['links']['download']['url']
           ver_name = version_name(url)
           download(r, url, ver_name)


