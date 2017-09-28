import argparse

from scapy.all import *

# Argparse setup
parser = argparse.ArgumentParser(description="Covert Channel Server")
parser.add_argument('-p', '--port', dest='port', help='Decode packets sent to this destination port only',
                    required=True)
parser.add_argument('-f', '--file', dest='filename', help='File to write', required=True)
args = parser.parse_args()


def parse(pkt):
    ip_address = pkt['IP'].src
    coded_message = ip_address.split('.')
    byt = chr(int(coded_message))
    filehandler = open(args.filename, 'a')
    filehandler.write(byt + '\n')
    filehandler.close()


def main():
    sniff(filter="dst port" + args.port, prn=parse)


if __name__ == '__main__':
    main()
