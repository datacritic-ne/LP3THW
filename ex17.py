from sys import argv
#from os.path import exists

script, from_file, to_file = argv

#print(f"Copying from {from_file} to {to_file}.")

# Can the next 2 commands be on one line?
#in_file = open(from_file)
#indata = in_file.read()
# Shorter version
indata = open(from_file).read()
#print(f"The input file is {len(indata)} bytes long.")

#print(f"Does the output file exist? {exists(to_file)}")
#print("Ready, hit ENTER to continue, CTRL-C to abort.")
#input()

#out_file = open(to_file, 'w')
#out_file.write(indata)
#Shorter version
out_file = open(to_file, 'w').write(indata)

#print("All right, all done.")

out_file.close()
#in_file.close()

# one-line
from sys import argv ; script, from_file, to_file = argv ; indata = open(from_file).read() ; out_file = open(to_file, 'w').write(indata) ; out_file.close()


