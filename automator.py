import os
choice = str(input('How you want to download posts? (u/h) : '))
if choice == 'h':
    hashtag = str(input('Enter the hastag without # : '))
    count = str(input('Enter the no. of photos : '))
    command = 'instaloader #'+hashtag+' -c '+count
    os.system(command)
else:
    user = str(input('Enter the username : '))
    command = 'instaloader '+user+' -c '+count
    os.system(command)
import os
cnf = str(input('Do you want to upload the posts ?(y/n) : '))
if cnf == 'y':
	from instabot import Bot
	bot = Bot()
	usr = str(input('Enter your username : '))
	pwd = str(input('Enter your password : '))
	cap = str(input('Enter the caption : '))
	bot.login(username=usr, password=pwd)
	dic = os.getcwd()+'\\#'+hashtag
	for photos in os.listdir(dic):
	    if photos.endswith('jpg'):
	        if photos.endswith('pic.jpg'):
	            continue
	        else:
	            print('Uploading : ',photos)
	            path = dic+'\\'+photos
	            bot.upload_photo(photo=path, caption=cap)
	print('Deleting Folders and files...')
	for directories in os.listdir(os.getcwd()):
		if directories.endswith('.py'):
			continue
		else:
			fldl = 'rmdir '+directories
			os.system(fldl)
	print('Done..\nPress any key to continue')
	input()
else:
	print('Signing Out...')
	print('Press any key to continue')
	input()