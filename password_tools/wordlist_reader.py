with open("wordlist.txt", "r") as file:
    for line in file:
        print("Trying password: ", line.strip())

