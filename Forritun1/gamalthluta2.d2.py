
def open_file(filename):
    try:
        the_file = open(filename, 'r')
        return the_file
    except FileNotFoundError:
        return None

def proceess_file(the_file):
    messages = {}

    for line in the_file:
        recipient, nr, fragment = line.strip().split()

        if recipient not in messages:
            messages[recipient] = {'message':'', 'packs':[]}

        messages[recipient]['message'] += fragment
        messages[recipient]['packs'].append(int(nr))

    the_file.close()
    return messages

filename = input('Filename: ')
the_file = open_file(filename)

if the_file is not None:
    messages = proceess_file(the_file)

    for recipient in sorted(messages.keys()):
        print(f'{recipient}:', ' '.join(messages[recipient]['message'].split('_')))
        if len(messages[recipient]['packs']) < messages[recipient]['packs'][-1]:
            missing_packets = []
            for i in range(1,messages[recipient]['packs'][-1]+1):
                if i not in messages[recipient]['packs']:
                    missing_packets.append(i)
            print('Packets missing:', ', '.join([str(x) for x in missing_packets]))
            
else:
    print('Invalid filename')