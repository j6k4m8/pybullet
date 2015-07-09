#!/usr/bin/env python

import pybullet
import sys
import contacts

def main(argv):
    contact = argv[0]
    try:
        int(contact)
    except ValueError:
        contact = contacts.get_number(contact)

    pybullet.push_sms(contact, argv[1])


if __name__ == "__main__":
    main(sys.argv[1:])
