import base64
import hashlib
import dpkt


def compute_key(key1, key2):
    combined = list(key1 + key2)
    combined.sort(reverse=True)
    combined = bytes(combined)
    return base64.b64encode(hashlib.sha1(combined).digest())


def xor(message, key):
    """ XOR two byte strings """
    res = b''
    counter = 0
    for b in message:
        res += bytes([b ^ key[counter % len(key)]])
        counter += 1
    return res


def main():
    filename = 'iftpp_challenge.pcap'
    pcap = dpkt.pcap.Reader(open(filename, 'rb'))

    skey = None
    ckey = None
    shared_key = None

    data = b''

    for timestamp, buf in pcap:

        # Unpack the Ethernet frame (mac src/dst, ethertype)
        eth = dpkt.ethernet.Ethernet(buf)

        # Make sure the Ethernet data contains an IP packet
        if not isinstance(eth.data, dpkt.ip.IP):
            print('Non IP Packet type not supported %s\n' % eth.data.__class__.__name__)
            continue

        # Now grab the data within the Ethernet frame (the IP packet)
        ip = eth.data

        # Now check if this is an ICMP packet
        if isinstance(ip.data, dpkt.icmp.ICMP):
            icmp = ip.data

            iftpp = icmp.data.data
            sid_field = iftpp[:4]

            remain = iftpp[4:]
            limiter = remain.find(b'\x1a\x08')

            if limiter > 0:
                payload_field = remain[:limiter]
                try:
                    checksum_field, flag_field = remain[limiter + 2:].split()
                except ValueError:
                    checksum_field = remain[limiter + 2:]
                    flag_field = None

                # voluntary misconception ?
                if flag_field == b'\x05':
                    payload_field = payload_field[1:]

                checksum = base64.b64encode(hashlib.sha1(payload_field).digest())
                if checksum_field != checksum[-9:-1]:
                    print("Checksum error")
                    print(checksum_field)
                    print(checksum)
            else:
                # ignore acknowledgement
                payload_field, flag_field = remain.split()

            if flag_field == b'\x02':
                ckey = payload_field
            elif flag_field == b'\x03':
                skey = payload_field
            elif flag_field == b'\x04':
                filename = payload_field.decode()
                print("Requesting file : " + filename)
                print("Value of ckey : " + str(ckey))
                print("Value of skey : " + str(skey))
                print("Computing shared key...")
                shared_key = compute_key(ckey, skey)
                print("Shared key : " + str(shared_key))
            elif flag_field == b'\x05':
                data += xor(payload_field, shared_key)
            elif flag_field == b'\x06':
                with open(filename, 'wb') as f:
                    f.write(data)
                data = b''


if __name__ == '__main__':
    main()
