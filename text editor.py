import msvcrt
import os
import time
import sys

text = []
loaded = []
filename = "file.txt"


def open_text(name=filename):
	global text

	f = open(name, "r")
	text[:] = []
	for line in f:
		text.append(line.replace("\n",""))
	f.close()

def print_text():
	x = 0
	for line in text:
		print("    ", x, line)
		x+=1

def save_text(name=filename):
	f = open(name, "w")
	for line in text:
		f.write(line + "\n")
	f.close()

def interperit(command):
	global text
	global filename
	command_list = command.split(",")

	if command_list[0] == "change":
		try: text[int(command_list[1])] = command_list[2][1:],print("done!")
		except: print("\tCommand either missing arguments or one of the arguments are out of range")
	elif command_list[0] == "open":
		if len(command_list) > 1:
			filename = command_list[1][1:]
			open_text(filename)
			print("done!")
		else:
			open_text()
	elif command_list[0] == "save":
		if(len(command_list) > 1):
			save_text(command_list[1][1:])
			print("done!")
		else:
			save_text()
	elif command_list[0] == "new":
		filename = command_list[1][1:]
		save_text(command_list[1])
		text[:] = []
	elif command_list[0] == "print":
		if len(command_list) > 1:
			print(text[int(command_list[1])])
		else:
			print_text()
	elif command_list[0] == "new line":
		if len(command_list) > 2:
			text.insert(int(command_list[1]), command_list[2][1:]),print("done!")
		else:
			text.append(command_list[1][1:])
	elif command_list[0] == "clear": os.system("cls")
	elif command_list[0] == "remove":
		for b in range(0, len(text)):
			if not len(command_list) > 2: 
				text[b] = text[b].replace(command_list[1][1:], "")
			else:
				text[b] = text[b].replace(command_list[1][1:], command_list[2][1:])
				print("done")
def khat():
        z=0
        for line in filename :
                z += 1
        return z

l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
     '0','1','2','3','4','5','6','7','8','9','!','@','#','$','%','^','&','*','(',')','_','-','+','=','[',']','{','}',"\\","/","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

def safe():
    os.system("cls")
    
def mainLoop():
    Text = ""
    global filename

    if len(sys.argv) > 1:
    	filename = sys.argv[1]

    global text
    try: open_text(filename)
    except: print("Default file not found\n\t\"file.txt\" is missing")


    while True:
        if msvcrt.kbhit():
            key = msvcrt.getch()
            if 8 == ord(key):
                safe()
                Text = Text[:len(Text)-1]
                sys.stdout.write(Text)
                sys.stdout.flush()
            elif ord(key) == 27 :
                    quit()
            elif ord(key) == 32 :
                safe()
                Text = Text[:]+ " "
                sys.stdout.write(Text)
                sys.stdout.flush()
            elif ord(key) == 13 :
                safe()
                Text = Text[:]+ "\n"
                sys.stdout.write(Text)
                sys.stdout.flush()
            elif ord(key) == 46 :
                safe()
                Text = Text[:]+ "."
                sys.stdout.write(Text)
                sys.stdout.flush()
            elif key == "key_LEFT" :
                        print("done!")
                    
            elif key.decode("utf-8") in l :
                safe()
                Text += key.decode("utf-8")
                sys.stdout.write(Text)
                sys.stdout.flush()
            time.sleep(0.001)
    return
        
mainLoop()
