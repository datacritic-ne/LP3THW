import sys

script, input_encoding, error = sys.argv

def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)
    
def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<=====>", cooked_string)

languages = open("languages.txt", encoding="utf-8")

main(languages, input_encoding, error)

# Things I haven't seen yet in this course:
# 1. Importing all of sys instead of just argv, and calling argv differently.
# 2. I get the script input to argv, but don't entirely understand what the input_encoding and error inputs are. input_encodoing apparently utf-8.
# 3. The if statement.
# 4. The "strip" function associated with the line object.
# 5. The "encode" and "decode" functions associated with the line.strip() command.
# 6. The "utf-8" encoding used in the open command on line 19.

# COME BACK TO THIS