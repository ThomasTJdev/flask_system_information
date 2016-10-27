#!/bin/bash
/bin/cat /proc/net/dev \
| awk 'BEGIN {print "["} NR>2 {print "{ \"interface\": \"" $1 "\"," \
					" \"tx\": " $2 "," \
					" \"tx_packets\": " $3 "," \
					" \"drops\": " $5 "," \
					" \"rx\": " $10 "," \
					" \"rx_packets\": " $11 " }," } END {print "]"}' \
| /bin/sed 'N;$s/,\n/\n/;P;D'\
| /bin/sed ':a;N;$!ba;s/\n/ /g'
