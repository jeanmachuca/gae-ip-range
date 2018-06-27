# gae-ip-range
Author: Jean Machuca 

Gets the ip range used by google for apps in Google App Engine Standard (xxx.appspot.com)

App Engine does not currently provide a way to map static IP addresses to an application.
In order to optimize the network path between an end user and an App Engine application,
end users on different ISPs or geographic locations might use different
IP addresses to access the same App Engine application.
DNS might return different IP addresses to access App Engine over time or from different network locations.
This script does recursively performing DNS SPF lookups to resolve the entire list of IP ranges.
More info:
https://cloud.google.com/appengine/kb/#static-ip
