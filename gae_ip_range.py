#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
gae_ip_range.py

Created on 06/27/2018

@author: jeanmachuca <correojean@gmail.com>

App Engine does not currently provide a way to map static IP addresses to an application.
In order to optimize the network path between an end user and an App Engine application,
end users on different ISPs or geographic locations might use different
IP addresses to access the same App Engine application.
DNS might return different IP addresses to access App Engine over time or from different network locations.

This script does recursively performing DNS SPF lookups to resolve the entire list of IP ranges.

More info:
https://cloud.google.com/appengine/kb/#static-ip


'''
import subprocess
cmd = "nslookup -q=TXT _cloud-netblocks.googleusercontent.com 8.8.8.8"
print cmd.split(' ')
process = subprocess.Popen(cmd.split(' '), stdout=subprocess.PIPE)
out, err = process.communicate()
nslist =[ns1.split(' ')[0] for ns1 in filter(lambda ns: ns.startswith('_cloud'),out.split('include:'))]

iplist = []
for ns2 in nslist:
    cmd2 = "nslookup -q=TXT "+ns2+" 8.8.8.8"
    process2 = subprocess.Popen(cmd2.split(' '), stdout=subprocess.PIPE)
    out2, err2 = process2.communicate()
    nslist2 = [ns3.split(' ')[0] for ns3 in filter(lambda ns: not ns.startswith('include:'),out2.split('text =')[1].split('v=spf1')[1].split('ip4:'))]
    iplist.extend(nslist2)

print '\n'.join(iplist)
