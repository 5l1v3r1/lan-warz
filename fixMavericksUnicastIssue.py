bplist00�_WebMainResource�	
_WebResourceFrameName^WebResourceURL_WebResourceData_WebResourceMIMEType_WebResourceTextEncodingNameP_xhttps://gist.githubusercontent.com/blimmer/7242676/raw/3a2be9d1b1593c296360ee10dc73da8dcbef45d9/fixMavericksUnicastIssueOL<html><head></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">#!/bin/bash

# Mavericks has a nasty issue regarding ARPs in corporate networks.
# It appears that they have tried to reduce bandwidth utilization by caching
# the results of ARPs. Unfortunately, this causes big problems with corporate
# networks with Virtual IPs or other corporate network redundancy measures.

# There exist other patches for this issue
# (see https://github.com/MacMiniVault/Mac-Scripts/blob/master/unicastarp/unicastarp-README.md)
# but they write a value that will be pulled everytime the machine reboots. Because
# we are assuming Apple will fix this in a future Mavericks update, we don't want this
# setting to last after a reboot. This script writes the fix, but it doesn't persist past a reboot.

# Author: Ben Limmer | hello@benlimmer.com

if [[  $(sw_vers -productVersion | grep '10.9')  ]]; then
	if [ $(sysctl net.link.ether.inet.arp_unicast_lim | awk -F':' '{print $2}' | sed -e 's/^[ \t]*//') == "0" ]; then
		echo System is already properly configured.
		exit
	else
		if [ `whoami` != root ]; then
			echo Please run this script as root or using sudo
			exit
		fi

		sysctl -w net.link.ether.inet.arp_unicast_lim=0
		echo Fixed ARP issue
		return 0
	fi
else
	echo This patch does not apply to your operating system.
fi</pre></body></html>Ztext/plainUUTF-8    ( ? N ` v � �`k                           q