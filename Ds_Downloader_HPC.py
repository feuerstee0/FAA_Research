#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Download Dataset from Google Drive
from google_drive_downloader import GoogleDriveDownloader as gdd
# Unzipping the file
import tarfile


# In[2]:


def download_dataset(gd_public_file_id, destination_path):
    
#     Nine_Videos_Training_Data_ID = "1O8aWq4FV6U3l-Dg7rTmJ10NkrNJuOh24"
#     Eleven_Videos_Training_Data_ID = "1Xq3gV5vAWGk4OBh7QE6jjQiLkDMLMlpH"
    
    
#     https://drive.google.com/open?id=1QYSNxS-Ge_q6uHetXZLfXIrRfR41zpyP
#     gd_public_file_id = All_Guages#"1Xq3gV5vAWGk4OBh7QE6jjQiLkDMLMlpH"
    # gd_Eval_file_id = "1_LV9IuQ2JUeVt_lRN9vGKxqxqKnf9OgX"
#     gd_public_file_id = gd_Eval_file_id
#     destination_path = "./Training.tar.gz"
    gdd.download_file_from_google_drive(file_id=gd_public_file_id,
                                        dest_path=destination_path,
                                        unzip=False)


    tar = tarfile.open(destination_path, "r:gz")
    tar.extractall()
    tar.close()


# In[3]:


if __name__ == "__main__":
    #All_Guages = "1qDy84Nb9XLEy0BDlbc82yJjqH2QT3dmR"
    #destination_path = "./Training.tar.gz"
   # download_dataset(gd_public_file_id=All_Guages, destination_path=destination_path)

#     Testing_Videos = "1gqe9K1WVxAbtrNVr-uishxyfB6vKEBXS"
#     destination_path = "./Testing.tar.gz"
#     download_dataset(gd_public_file_id=Testing_Videos, destination_path=destination_path)

#     G_Masks = "1HMjoEaD9vvR0FAs52NeJ3FSwJX9BjOFk"
#     destination_path = "./G_Masks.tar.gz"
#     download_dataset(gd_public_file_id=G_Masks, destination_path=destination_path)
    
    
#     G_Training_Clean = "1VDXbjg07LWGOmtzd55Q0TWlfrOt4bJZ4"
#     destination_path = "./Training.tar.gz"
#     download_dataset(gd_public_file_id=G_Training_Clean, destination_path=destination_path)



#     This also contains the Attitude Data with Threshold 6
#     G_Training_With_CI_3 = "1ABm9pjMsV8aZHxECijZyWDv9D_bLMNeo"
#     destination_path = "./Training_CI_3.tar.gz"
#     download_dataset(gd_public_file_id=G_Training_With_CI_3, destination_path=destination_path)
    

    
#     G_Training_With_CI_5 = "1WjeuWKQy7GRFQlHH9mzKr7v-_XhV95mw"
#     destination_path = "./Training_CI_5.tar.gz"
#     download_dataset(gd_public_file_id=G_Training_With_CI_5, destination_path=destination_path)
    
    
#     Training_Parallel_2_Attitude_Degree_3 = "1_7KGUR1jBOIPxsMZzg7OPtA0YudJLATB"
#     destination_path = "./Training_Parallel_2_Attitude_Degree_3.tar.gz"
#     download_dataset(gd_public_file_id=Training_Parallel_2_Attitude_Degree_3, destination_path=destination_path)
    
#     Training_Parallel_2_Attitude_Degree_4 = "13gFJfjO1tBF5LWDd1_AQWxe5kWfhKiDX"
#     destination_path = "./Training_Parallel_2_Attitude_Degree_4.tar.gz"
#     download_dataset(gd_public_file_id=Training_Parallel_2_Attitude_Degree_4, destination_path=destination_path)
        
#     Training_Parallel_2_Attitude_Degree_5 = "1BcUXWRc7doPtZzQedUhkvorTtWJy6sMI"
#     destination_path = "./Training_Parallel_2_Attitude_Degree_5.tar.gz"
#     download_dataset(gd_public_file_id=Training_Parallel_2_Attitude_Degree_5, destination_path=destination_path)
    
 
    # HPC Deployment 
    Training_Data_Pilot = "1hNs4qxG-q2GNgFrWaNrNQ7baIebGjqQg"
    destination_path = "./Pilot_TrainingData.tar.gz"
    download_dataset(gd_public_file_id=Training_Data_Pilot, destination_path=destination_path)
    
    
    
    


# In[3]:


#python


# In[ ]:



