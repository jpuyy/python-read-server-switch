#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author jpuyy.com

import json
import csv
import subprocess

subprocess.call("ansible -i hosts all -m setup --tree .",shell=True)

with open('result.csv','wb') as csvfile:
    serverwriter = csv.writer(csvfile, delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL)
    serverwriter.writerow(['ip','型号','序列号','cpu','cpu个数','内存MB','硬盘大小','系统版本'])

#with open('hosts', 'r') as f:
for line in open('hosts', 'r').readlines():
    line = line.strip('\n')
    fopen = open(line,'r')
    
    output = json.loads(fopen.read())
    
    print 'cpu'
    print output['ansible_facts']['ansible_processor'][1]
    
    print '---------'
    with open('result.csv','a') as csvfile:
        serverwriter = csv.writer(csvfile, delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL)
        #if output['failed']==true
        #    jump
        #serverwriter.writerow
        serverwriter.writerow([
            output['ansible_facts']['ansible_default_ipv4']['address'],
            output['ansible_facts']['ansible_product_name'],
            output['ansible_facts']['ansible_product_serial'],
            output['ansible_facts']['ansible_processor'][1],
            #output['ansible_facts']['ansible_processor_cores'],
            output['ansible_facts']['ansible_processor_count'],
            output['ansible_facts']['ansible_memtotal_mb'],
            'nonono',
            output['ansible_facts']['ansible_distribution']
        ])
