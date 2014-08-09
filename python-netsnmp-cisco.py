#!/usr/bin/env python
# by yangyang89
# using snmp get switch serial, model, manage ip ..
import netsnmp
import sys
import urllib
import urllib2

# reference python for linux and unix administration page 209
class Snmp(object):
    """A basic SNMP session"""
    def __init__(self,oid="sysDescr", Version=2):
        self.oid = oid
        self.version = Version
        self.destHost = sys.argv[1]
        self.community = sys.argv[2]

    def query(self):
        """Creates SNMP query session"""
        try:
            result = netsnmp.snmpwalk(self.oid, Version = self.version, DestHost = self.destHost, Community = self.community)
        except Exception, err:
            print err
            result = None
        return result

print sys.argv[1] + sys.argv[2]
if sys.argv[1] and sys.argv[2]:
    s = Snmp()
    #http://tools.cisco.com/Support/SNMP/do/BrowseOID.do

    s.oid = ".1.3.6.1.2.1.4.20.1.1" # manage ip ipAdEntAddr
    ip = s.query()
    telnet = ip[0]
    print "ip: " + telnet
    
    s.oid = ".1.3.6.1.4.1.9.3.6.3" # serial numbers chassisId
    serial = s.query()
    serial = serial[0]
    print "serial: " + serial
    
    s.oid = ".1.3.6.1.2.1.47.1.1.1.1" # product_model entPhysicalEntry
    product_model = s.query()
    product_model = product_model[1].split(' ')[0]
    print "product_model: " + product_model
    #print s.query()
    
    s.oid = ".1.3.6.1.4.1.9.2.1.3" # hostname hostName
    hostname = s.query()
    hostname = hostname[0]
    print "hostname: " + hostname
