import sys

_contacts = [line.strip() for line in open(".contacts", 'r')]

contacts = {}
for c in range(len(_contacts)):
    con = _contacts[c].split()
    contacts[con[0]] = con[1]

def add_contact(name, number):
    with open('.contacts', 'a') as file:
        file.write("\n" + name + "\t" + number)
        contacts[name] = number

def get_number(name):
    return contacts[name]


def main(argv):
    command = argv[0]
    if command == 'add':
        add_contact(argv[1], argv[2])

if __name__ == "__main__":
    main(sys.argv[1:])
