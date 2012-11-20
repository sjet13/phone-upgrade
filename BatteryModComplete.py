#imports
import time
import os
import platform
import shutil
import zipfile
import subprocess
import getpass
#Detects the users OS, Version, System Drive, and user name.
usros = platform.system()
usrver = platform.release()
print '%s %s Detected' % (usros, usrver)
usrdrive = os.getenv('SystemDrive')
usrname = getpass.getuser()

#extract and move then delete
zipfile.ZipFile('%s/temp/files.zip' % (usrdrive)).extractall('%s/temp/' % (usrdrive))
os.remove('%s/temp/127.apk' % (usrdrive))
os.remove('%s/temp/1.apk' % (usrdrive))

#Decompile
os.system('apktool d SystemUI.apk')

#Copy
print 'stat_sys_battery'
shutil.copy2('%s/temp/stat_sys_battery.xml' % (usrdrive), '%s/temp/SystemUI/res/drawable' % (usrdrive))

x = os.listdir('%s/temp/i' % (usrdrive))
for file1 in x:
    print file1
    shutil.copy2('%s/temp/i/' % (usrdrive) + file1, '%s/temp/SystemUI/res/drawable-xhdpi/' % (usrdrive))

time.sleep(2)

#compile
os.system('apktool b SystemUI almostdone.apk')

#copy files from Orginal APK to new APK
#Tried WinRar, else manually do it.
try:
    rar = '%s/Program Files/WinRAR/winRar.exe' % (usrdrive)  # Edit this to point to your favourite zip archiver.
    subprocess.Popen("%s %s" % (rar, '%s/temp/SystemUI.apk' % (usrdrive)))
    subprocess.Popen("%s %s" % (rar, '%s/temp/almostdone.apk' % (usrdrive)))
except:
    print 'Error! (Minor)'
    print 'WinRar not detected, manually copy files using your favourite zip archiver.'
raw_input('Copy Files then press any key... See README.TXT to see what files to copy.')
#De/comment line blow if you want winrar to close automatically
os.system("TASKKILL /F /IM winRar.exe")


#ZipAlign
#backs up the old system UI
shutil.copy2('%s/temp/SystemUI.apk' % (usrdrive), '%s/temp/SystemUI.apk.old' % (usrdrive))
time.sleep(2)
os.system('zipalign -f -v 4 almostdone.apk SystemUI.apk')
time.sleep(2)

#cleanup
shutil.copy2('C:/temp/SystemUI.apk', 'C:/dropbox/SystemUI.apk')
os.remove('%s/temp/stat_sys_battery.xml' % (usrdrive))
os.remove('%s/temp/zipalign.exe' % (usrdrive))
os.remove('%s/temp/apktool.bat' % (usrdrive))
os.remove('%s/temp/aapt.exe' % (usrdrive))
os.remove('%s/temp/apktool.jar' % (usrdrive))
os.remove('%s/temp/almostdone.apk' % (usrdrive))
shutil.rmtree('%s/temp/i/' % (usrdrive))
shutil.rmtree('%s/temp/SystemUI/' % (usrdrive))


print 'COMPLETED'
time.sleep(5)
