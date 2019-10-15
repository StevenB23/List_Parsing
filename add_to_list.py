#this loop should append each line in our file to the list like saying file = open('log.txt','r') this operation will also auto close our file for us
with open('./pass.txt','r') as file: 
    for line in file:
        discovered_names.append(line.strip()) # Strip new line chars

# Add the collected items from teh pass.txt list and add them to our existing pass3.txt list if the don't already exist
for username in discovered_names:
    with open('./pass3.txt', 'a+') as file:#Read and Write data to end of file
        file.seek(0)
        if username not in file.read():
            file.write(f'{username}\n')
