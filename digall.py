#!/usr/bin/env python
#Copyright (c) 2018 Julian Klaiber

import sys
import dns.resolver
import dns.query
import dns.zone
import socket
from optparse import OptionParser

parser = OptionParser(usage="%prog [-f] [-q]", version="%prog 1.0")
parser.add_option("-d", "--domain", help="the domainname you want to lookup")
parser.add_option("-i", "--ipadress", help="the ip adress you want to lookup")
parser.add_option("-n", "--nameserver", default="8.8.8.8", help="take another nameserver default is 8.8.8.8 from google")
parser.add_option("-f", "--file", help="filename")
parser.add_option("-p", "--path", help="path to the reportfile (use only with -f)")

(options, args) = parser.parse_args()


myResolver = dns.resolver.Resolver()
myResolver.nameservers = [options.nameserver]


print "Digall Tool for easier domain lookups. Written in the beautiful Python Language."
print "Copyright (c) 2018 Julian Klaiber\n"
print '\x1b[5;30;44m' + 'DNS lookup <' + options.domain + '>' + '\x1b[0m''\n'

try:
        myIP = socket.gethostbyname(options.domain)
        print '\x1b[0;32;40m' + 'IP Adress:' + '\x1b[0m'
        for rdata in myIP:
                print rdata

try:
        myAnswers = myResolver.query(options.domain, "SOA")
        print '\x1b[0;32;40m' + 'SOA:' + '\x1b[0m'
        for rdata in myAnswers:
                print rdata
except:
        print '\x1b[0;31;40m' + 'SOA Record Query failed:' + '\x1b[0m'

try:
        myAnswers = myResolver.query(options.domain, "NS")
        print ""
        print '\x1b[0;32;40m' + 'Nameserver:' + '\x1b[0m'
        for rdata in myAnswers:
                print rdata
except:
        print ""
        print '\x1b[0;31;40m' + 'CNS Record Query failed:' + '\x1b[0m'

try:
        myAnswers = myResolver.query(options.domain, "MX")
        print ""
        print '\x1b[0;32;40m' + 'MX Server:' + '\x1b[0m'
        for rdata in myAnswers:
                print rdata
except:
        print ""
        print '\x1b[0;31;40m' + 'MX Record Query failed:' + '\x1b[0m'

try:
        myAnswers = myResolver.query(options.domain, "A")
        print ""
        print '\x1b[0;32;40m' + 'A Records:' + '\x1b[0m'
        for rdata in myAnswers:
                print rdata
except:
        print ""
        print '\x1b[0;31;40m' + 'A Record Query failed:' + '\x1b[0m'

try:
        myAnswers = myResolver.query(options.domain, "CNAME")
        print ""
        print '\x1b[0;32;40m' + 'CNAME Records:' + '\x1b[0m'
        for rdata in myAnswers:
                print rdata
except:
        print ""
        print  '\x1b[0;31;40m' + 'CNAME Record Query failed:' + '\x1b[0m'

try:
        myAnswers = myResolver.query(options.domain, "TXT")
        print ""
        print '\x1b[0;32;40m' + 'TXT Records:' + '\x1b[0m'
        for rdata in myAnswers:
                print rdata
except:
        print ""
        print '\x1b[0;31;40m' + 'TXT Record Query failed:' + '\x1b[0m'

try:
        myAnswers = myResolver.query(options.domain, "PTR")
        print ""
        print '\x1b[0;32;40m' + 'PTR Records:' + '\x1b[0m'
        for rdata in myAnswers:
                print rdata

except:
        print ""
        print '\x1b[0;31;40m' + 'PTR Record Query failed:' + '\x1b[0m'
