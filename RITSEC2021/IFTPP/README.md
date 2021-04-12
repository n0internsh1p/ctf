Dang that's a big ping

-degenerat3

--- 

This challenge give us a pcap to analyse with a hint on the presence of a big ping. Using Wireshark we can easily find a document requested by the client with the ip 192.168.206.136.
This document is in fact a pseudo RFC which define a new protocol : IFTPP. We can then use the information given to implement a script that decode packet using this protocol and find the flag.
