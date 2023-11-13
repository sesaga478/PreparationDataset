import os,sys

def rename_files_folder(folder,ext1,ext2):
  for filename in os.listdir(folder):
    infilename = os.path.join(folder,filename)
    if not os.path.isfile(infilename): continue
    oldbase = os.path.splitext(filename)
    newname = infilename.replace(ext1, ext2)
    output = os.rename(infilename, newname)
