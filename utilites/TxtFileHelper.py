import time

def AddLineBreaks():
    lines = []
    do_once = True
    with open("./templates/txt/default.txt", "r") as file:
        for line in file:
            if line.find("<br>") != -1 and do_once:
                do_once = False
                return
            else:
                lines.append(line+"<br>")
    
    with open("./templates/txt/default.txt", "w") as file:
        file.seek(0)
        file.truncate()
        for line in lines:
            print(line)
            file.write(line)


def DeleteLineBreaks():
    lines = []
    do_once = True
    with open("./templates/txt/default.txt", "r") as file:
        for line in file:
            if line.find("<br>") != -1 and do_once:
                do_once = False
                return
            else:
                real = str(line)
                real.replace("<br>", "")
                lines.append(real)
    
    with open("./templates/txt/default.txt", "w") as file:
        file.seek(0)
        file.truncate()
        for line in lines:
            print(line)
            file.write(line)