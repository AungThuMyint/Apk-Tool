import os
from colorama import Fore, Back, Style
text = """

	####################################################
	&&						  &&
 	&&   APK Extractor, Builder, KeyStore Generator   &&
        &&						  &&
	####################################################
"""
text2 = """
	             [*] Copyright @ TechLab [*]

	      [*] www.aungthumyint-mm.blogspot.com [*]

                      Release Date [9-11-2020]
"""

print(Fore.YELLOW + text)
print(Fore.GREEN + text2)

way = """
	[1] Extract APK Method 1 (Encrypt XML File & Extract)
	[2] Extract APK Method 2 (Decrypt XML File & Extract)
	[3] APK Combine (Build)
	[4] Create KeyStore
	[5] Sign APK With Original
	[6] Sign APK With Own Keystore
	[7] Exit
	[8] About
"""
print(Fore.CYAN + way)
print(Style.RESET_ALL)

def run(runfile):
	with open(runfile,"r") as rnf:
		exec(rnf.read())

try:
	method1 = int(input("[*] Choose Your Input Options [*] : "))
	print("\n")

	if method1==1:
		print(Fore.YELLOW + "[*] Using APK Extracting Using Method One\n")
		apk_name = input("Enter Your Application Name (example.apk) : ") 
		os.system("apktool d -f -r  "  +  apk_name)
		run('Apk-Tool.py')
		print(Style.RESET_ALL)
	elif method1==2:
		print(Fore.MAGENTA + "[*] APK Extracting Using Method Two\n")
		apk_name = input("Enter Your Application Name (example.apk) : ") 
		os.system("apktool d -f -o ApkExtractFiles " + apk_name)
		print(Style.RESET_ALL)
		run('Apk-Tool.py')
	elif method1==3:
		print(Fore.GREEN + "[*] APK Building\n")
		apk_name = input("Enter Your Application Folder (folder_name) : ") 
		os.system("apktool b " + apk_name)
		print(Style.RESET_ALL)
		run('Apk-Tool.py')
	elif method1==4:
		print(Fore.YELLOW + "[*] Keystore Creating\n")
		name=str(input("Save Keystore Name : "))
		os.system("keytool -genkey -V -keystore " +name+ ".keystore -alias alexis -keyalg RSA -keysize 2048 -validity 1000")
		print(Style.RESET_ALL)
		run('Apk-Tool.py')
	elif method1==5:
		print(Fore.MAGENTA + "[*] Sign Application\n")
		app_name=str(input("Enter Application Location (eg. /example/name.apk) : "))
		os.system("jarsigner -verbose -keystore debug.keystore -storepass android -keypass android -digestalg SHA1 -sigalg MD5withRSA " + app_name + " androiddebugkey")
		print(Style.RESET_ALL)
		run('Apk-Tool.py')
	elif method1==6:
		print(Fore.GREEN + "[*] Sign Application With Own Keystore\n")
		app=input(str("Enter App Location (eg. /example/name.apk) : "))
		key=input(str("Enter Your Keystore Location (eg. /example/name.keystore) : "))
		os.system("jarsigner -verbose -sigalg SHA1withRSA -digestalg SHA1 -keystore " + key + " " + app +  " alexis")
		print(Style.RESET_ALL)
		run('Apk-Tool.py')
	elif method1==7:
		print(Fore.RED + """
	############################
	* Exit The Program Bye Bye *
	############################
	""")
		quit()
	elif method1==8:
		print(Fore.CYAN + """
	#######################################################
	&						      &
	&	          Apk Tool Version 1.0	    	      &
	&          Coding By Aung Thu Myint @ TechLab	      &
	&     Feedback : www.aungthumyint-mm.blogspot.com     &
	&						      &
	#######################################################
	""")
		run('Apk-Tool.py')

	else:
		print(Fore.RED + """
	###################################
	*   Invalid Options ! Try Again   *
	###################################
	""")
		run('Apk-Tool.py')

except ValueError:
	print(Fore.RED + """
	##################################
	*   Invalid Options Choose 1:8   *
	##################################
""")

	run('Apk-Tool.py')
