import requests

url = "https://learnpythonthehardway.org/python3/languages.txt"
response = requests.get(url)

if response.status_code == 200:
    with open("languages.txt", "wb") as file: # I need to understand better how this works
        file.write(response.content)
        print("File download successful!")
else:
    print("File download did not work.")

# THIS WORKS!