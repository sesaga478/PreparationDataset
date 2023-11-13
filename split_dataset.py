import random
import glob, os
import shutil

random.seed(123)


def split_dataset(dataset_path,test_perc,valid_perc,img_ext,mask_ext, valid_fol,test_fol,train_fol):

  # Populate the folders
  pt = test_perc/100
  pv = valid_perc/100

  split_folders=[valid_fol,test_fol,train_fol,valid_fol+"/images", valid_fol+"/masks", 
                 test_fol+"/images", test_fol+"/masks", train_fol+"/images", train_fol+"/masks"]

  for fol in split_folders:
    if not os.path.exists(fol):
      os.makedirs(fol)

  for pathAndFilename in sorted(glob.iglob(os.path.join(dataset_path, "*."+img_ext))):
      title, ext = os.path.splitext(os.path.basename(pathAndFilename))
      if random.random() <=pv :
          shutil.copy(dataset_path+"/"+title+"."+img_ext, split_folders[3])
          shutil.copy(dataset_path+"/"+title+"."+mask_ext, split_folders[4])
      if random.random() <=pt :
          shutil.copy(dataset_path+"/"+title+"."+img_ext, split_folders[5])
          shutil.copy(dataset_path+"/"+title+"."+mask_ext, split_folders[6])
      else:
          shutil.copy(dataset_path+"/"+title+"."+img_ext, split_folders[7])
          shutil.copy(dataset_path+"/"+title+"."+mask_ext, split_folders[8])
