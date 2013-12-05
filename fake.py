#!/usr/bin/python

#This is a  PoC written by RAbimba Karanjai to obtain information from announce requests.
#urlsnarf by default only looks for data on tcp ports 80,3128 and 8080.  
#An announce requests could be on any port,  or even over udp. This is only a PoC!
#The info_hash is used to build RC4 keys in Message Stream Encryption
#The purpose of this is to obtain a list of info_hashes used by a specific client. 

#urlsnarf REQUIRES root!!!!

import subprocess
import sys
from MySQLdb import escape_string
import urllib
from myConnection import condb


var['test']=1
print var['test']
sys.exit()

myCon = condb()

def urldecode(query):
   d = {}
   query="server="+query
   query=query.replace("?","&",1)
   a = query.split('&')
   for s in a:
      if s.find('='):
         k,v = map(urllib.unquote, s.split('='))
         try:
            d[k].append(v)
         except KeyError:
            d[k] = [v]
   return d

#we are looking for url's like this
#url="http://192.168.1.197/announce?info_hash=%B4H%80%0F%9C%95.L%11%E9%FC%0D%B8%7D%7Fs%E3%A9%28%85&peer_id=M5-2-2--"

urlsnarf=subprocess.Popen('urlsnarf -i lo',shell=True, stdout=subprocess.PIPE)
url_snarf = urlsnarf.stdout.readline()
while url_snarf != '':
    url_start=url_snarf.split('"GET ')
    if len(url_start) >=2:#is it a get request? 
        url_end=url_start[1].split(" ")
        url=url_end[0]
        url_vars=urldecode(url)
        if 'info_hash' in url_vars:
            if 'peer_id' not in url_vars:
                url_vars['peer_id']=[]
                url_vars['peer_id'].append('')#this value will not be in scrape reqeusts,  but the info_hash will be. 
            myCon.execute("insert into infohash (announce_server,info_hash,peer_id)values('"+escape_string(url_vars['server'][0])+"','"+escape_string(url_vars['info_hash'][0])+"', '"+escape_string(url_vars['peer_id'][0])+"')")
    url_snarf = urlsnarf.stdout.readline()