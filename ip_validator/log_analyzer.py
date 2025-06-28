with open("log.txt", "r") as log:
    for line in log:
        if "404" in line:
            print("Error Found: ", line.strip())

