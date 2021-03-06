import pydicom
import os
from subprocess import call

acquis_folder = os.getcwd()
# acquis_folder = '/home/p0054421/Downloads/temp_segment/AAA_YP/AAA_YP_20101104'
# get image size
im = acquis_folder + '/' + \
     [f for f in os.listdir(acquis_folder) if os.path.isfile(os.path.join(acquis_folder, f))][0]

imm = pydicom.read_file(im)
e = 0.5 * imm.SliceThickness

print 'Slice thickness is ', e, 'mm'

dx = imm.PixelSpacing[0]

output_fname = os.path.split(im)[0] + '.nrrd'
ddx = str(dx) + ' ' + str(dx) + ' ' + str(dx)

command = 'vmtkimagereslice -ifile ' + im + ' -ofile ' + output_fname + ' -spacing ' + ddx + ' -interpolation cubic'
print command
# quit()
if e >= 1.5*dx:
    print 'resliced file name will be', output_fname
    print 'reslicing'
    call(command, shell=True)
