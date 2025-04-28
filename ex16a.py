from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here's your new file {filename}.")
print(txt.read())

txt.close()
