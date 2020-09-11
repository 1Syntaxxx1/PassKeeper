import random, sys, time, argparse

##Telegram
##creator t.me/syntaxxxtechexpert
##This area checks to ensure you are using python3
if sys.version_info[0] !=3:
	print('''--------------------------------------
	REQUIRED PYTHON 3.x
	use: python3 'ps.py'
--------------------------------------
			''')

#colours
green     = '\033[92m'
cyan      = '\033[95m'
bold      = '\033[1m'
underline = '\033[4m'
end       = '\033[0m'
red       = '\033[91m'

print()
print(f"{bold}Coded by{end}", end="")
print(f"{green}{bold} >> {end}", end = "")
print(f"{cyan}{bold}Syntaxxx{end}")

print(f"{red}Don't Forget To...", end="")
print(f"{green}{bold}Follow Your Dreams", end="")

print(f"{bold}telegram{end}", end = "")
print(f"{green}{bold} >> {end}", end = "")
print(f"{cyan}{bold}@syntaxxxtechexpert{end}")
print()

parser = argparse.ArgumentParser(description="This a simple password storage program, that also helps you generate a very strong password!", usage="python/python3 %(prog)s")
parser.parse_args()


##This section you will be asked whether you want to end the program or continue
a = input("DO YOU WANT TO QUIT [y/n]?")
if a == "y":
    exit()
    print("Bye!!!")
elif a == "n":
    print("YOUR GOOD TO GO!!!")
    def get_random_string(length):
        # put your letters in the following string
        sample_letters = input('Characters: ')
        result_str = ''.join((random.choice(sample_letters) for i in range(length)))
        print("Filename should be in *.txt")
        with open(input('name of password file: '), 'a') as f:
            a = input("What are you generating the password for? ")
            print(a + " is :", result_str, file=f)

##Here is where a loop has been used to ensure the program will continue until a certain condition is met
while True:
    print(f"\n{red}{bold}Test if you are a robot!!!", end="")
    a = input("\nDO YOU WANT TO QUIT [y/n]?")
    if a == "n":
        get_random_string(int(input("Amount of Characters that should be in Password: ")))
        for i in range(101):
            time.sleep(0.001)
            sys.stdout.write("\r%d%%" % i)
            sys.stdout.flush()
    elif a == "y":
        print("Bye!!!")
        exit()
    else:
        print(f"{red}Invalid!!!", end="")
        quit()
