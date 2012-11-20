#!/system/bin/sh
mount -o remount,rw -t yaffs2 /dev/block/mtdblk3 /system
cd /system/app
rm Calculator.apk
rm Calendar.apk
rm CMFileManager.apk
rm CMFileManagerThemes.apk
rm Email.apk
rm Exchange2.apk
rm Tag.apk
rm LatinIME.apk
rm VoiceDialer.apk
rm VideoEditor.apk
rm Trebuchet.apk
cp /sdcard/Cyandelta/bootanimation.zip /system/media/
cp /sdcard/SystemUI.apk /system/app/
chmod 777 /system/app/SystemUI.apk
chmod 777 /system/media/bootanimation.zip
rm /sdcard/SystemUI.apk
rm DeskClock.apk
cp DeskClockGoogle.apk Deskclock.apk
rm DeskClockGoogle.apk
reboot