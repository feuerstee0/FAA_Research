#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Download Dataset from Google Drive
from google_drive_downloader import GoogleDriveDownloader as gdd
# Unzipping the file
# import tarfile

# In[2]:

def download_dataset(gd_public_file_id, destination_path):
    
    gdd.download_file_from_google_drive(file_id=gd_public_file_id,
                                        dest_path=destination_path,
                                        unzip=False)

   # tar = tarfile.open(destination_path, "r:gz")
   # tar.extractall()
   # tar.close()

# In[3]:

if __name__ == "__main__":

    # HPC Deployment 
    Training_Data_Pilot = "1hNs4qxG-q2GNgFrWaNrNQ7baIebGjqQg"
    destination_path = "./Pilot_TrainingData.zip"
    download_dataset(gd_public_file_id=Training_Data_Pilot, destination_path=destination_path)

# In[3]:


#python


# In[ ]:



