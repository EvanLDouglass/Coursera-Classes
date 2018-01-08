choose = input("Enter file name: ")
in_file = open(choose)

senders = dict()
for line in in_file:
    if line.startswith("From "):
        line = line.split()
        senders[line[1]] = senders.get(line[1], 0) + 1

bigword = ''
bigcount = 0
for key, value in senders.items():
    if value > bigcount:
        bigword = key
        bigcount = value

print(bigword, bigcount)
