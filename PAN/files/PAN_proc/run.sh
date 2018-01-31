#set the folder locations
folder_home='/home/themba/Documents/PAN/files/PAN_proc'
folder_in='/home/themba/Documents/PAN/files/PAN_proc/input'			#folder where files are located
folder_proc='/home/themba/Documents/PAN/files/PAN_proc/proc'
folder_out='/home/themba/Documents/PAN/files/PAN_proc/output'
folder_unproc='/home/themba/Documents/PAN/files/PAN_proc/unproc'
outfile="/home/themba/Documents/PAN/files/PAN_proc/test.html"

# rm $folder_in/*.*
find /home/themba/Documents/PAN/files/ -maxdepth 1 -type f -name '*.xlsx' -mtime -1 -exec cp -a "{}" $folder_in \;

#cp ~/Desktop/GD/PAN/*.xlsx $folder_in
#cp ~/Desktop/GD/PAN/*.zip $folder_in


#first round go through all the files in input folder, rename and copy to proc folder
for file in $folder_in/*.xlsx ; do
 echo $file
 python /home/themba/Documents/PAN/files/PAN_proc/rename.py "$file" $folder_proc  
done

#copy all unprocessed files to unprocessed folder
mv $folder_in/*.* $folder_unproc  

rm $outfile

echo "<!DOCTYPE html>" >> $outfile
echo "<html>" >> $outfile
echo `date` >> $outfile
echo "<TABLE BORDER=4 CELLSPACING=4 CELLPADDING=4>" >> $outfile
echo "<TR><TH>VESSEL TYPE<TH>VESSEL NAME<TH>PORT<TH>ETA AT PORT (UTC)<TH>PREVIOUS PORTS<TH>CREW NATIONALITY DISTRIBUTION<TH>CREW GENDER DISTRIBUTION<TH>OTHER ON-BOARD<TH>SECURITY ON-BOARD<TH>CARGO<TH>WEAPONS</TR>" >> $outfile


for file in $folder_proc/*.xlsx ; do
  echo "processing file" $file
  python /home/themba/Documents/PAN/files/PAN_proc/proc.py "$file" $outfile 
done


echo "</TABLE>" >> $outfile
echo "</body>"  >> $outfile
echo "</html>"  >> $outfile

mv $folder_proc/*.* $folder_out  

