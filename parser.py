#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author jpuyy.com
# read hardware infomation and update to racktables

import json
import subprocess
import urllib
import urllib2
import httplib

subprocess.call("ansible -i hosts all -m setup --tree .",shell=True)

for line in open('hosts', 'r').readlines():
    line = line.strip('\n')
    fopen = open(line,'r')
    
    output = json.loads(fopen.read())
    
    product_model = output['ansible_facts']['ansible_product_name']
    serial = output['ansible_facts']['ansible_product_serial']
    cpu_model = output['ansible_facts']['ansible_processor'][1]
    cpu_num = output['ansible_facts']['ansible_processor_count']
    memory = output['ansible_facts']['ansible_memtotal_mb']
    hostname = output['ansible_facts']['ansible_fqdn']
    #system_version = output['ansible_facts']['ansible_lsb']['description']
    system_version = output['ansible_facts']['ansible_distribution_version']
    eth = {}
    mac = {}

    # get eth and mac address
    for interface in output['ansible_facts']['ansible_interfaces']:
        if(interface != 'lo'):
            int_key = interface.replace('_',':')
            ansible_int = 'ansible_' + interface
            if 'ipv4' in output['ansible_facts'][ansible_int]:
                int_value = output['ansible_facts'][ansible_int]['ipv4']['address']
                if(int_value):
                    eth[int_key] = int_value
            if 'macaddress' in output['ansible_facts'][ansible_int]:
                mac_value = output['ansible_facts'][ansible_int]['macaddress'].replace(':','')
                if(mac_value):
                    mac[int_key] = mac_value

    ethjson = json.dumps(eth)
    macjson = json.dumps(mac)
