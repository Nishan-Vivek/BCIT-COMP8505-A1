# BCIT COMP8505 Assignment 1 - Cover Channel

## Objective

To become familiar with covert channels and to design a covert channel using the TCP/IP protocol suite.

## Pseudo Code

### Client
```
OPEN file
  FOR EACH char in file
    CONVERT char to int
    CREATEPACKET where last(1/2) octet of source IP is replaced with char/int
    SENDPACKET to specified destination/port	
  END FOR
```

### Server
```
LISTENFORPACKETS on specified port (loop)
 	 PARSE Source IP from packet to extract last octet
  	CONVERT octet to char
	 WRITE char to file
```

## Implementation

The project was implemented in Python using the Scapy library. The client and server were written in separate .py files. The client.py file takes the source text file, destination IP of the server, destination port of the server and a three octet subnet range as arguments. The source text file is read by char. The char is converted to its ANSI INT equivalent. This is used as the last octet of the crafted packet source IP. The first 3 octets are specified by arguments so a “realistic” subnet can be chosen. The server.py takes  
