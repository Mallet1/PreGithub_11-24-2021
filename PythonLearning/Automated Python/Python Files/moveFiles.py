import shutil

shutil.copy('C:\\Users\\Sam Mallet\\Desktop\\Testing\\spam.txt',
            'C:\\Users\\Sam Mallet\\Desktop\\Testing\\delicious')
# copies spam.txt to the folder delicious

shutil.copy('C:\\Users\\Sam Mallet\\Desktop\\Testing\\spam.txt',
            'C:\\Users\\Sam Mallet\\Desktop\\Testing\\delicious\\endochromatic system.txt')
# copies spam.txt to the folder delicious but renames it to endochromatic system

shutil.copytree('C:\\Users\\Sam Mallet\\Desktop\\Testing\\delicious',
                'C:\\Users\\Sam Mallet\\Desktop\\Testing\\delicious_backup')
# copies the delicious folder and its contents to delicious_backup

shutil.move('C:\\Users\\Sam Mallet\\Desktop\\Testing\\spam.txt',
            'C:\\Users\\Sam Mallet\\Desktop\\Testing\\delicious\\walnut')
# moves spam.txt into the walnut folder in the delicious folder

shutil.move('C:\\Users\\Sam Mallet\\Desktop\\Testing\\delicious\\walnut\\spam.txt',
            'C:\\Users\\Sam Mallet\\Desktop\\Testing')
# moves spam.txt back

shutil.move('C:\\Users\\Sam Mallet\\Desktop\\Testing\\spam.txt',
            'C:\\Users\\Sam Mallet\\Desktop\\Testing\\eggs.txt')
# renames the file
