"""
- File Folder Preparation Tool: Podcast Folder Structure
- This script is designed to create a file/folder structure for the In depth with SCUBA Q Multimedia Podcast Folder
- By Quincy Muzik 5/21/2025
"""

# API's / Modules
import os
import datetime

def createPodcastFolderStructure():

    # Podcast File Path 
    podcastFilePath = "J:\Podcasts\In Depth with SCUBA Q Multimedia Podcast"

    # Podcast Folder Names
    foldersPodcast = ["Original Podcast Recording", "Finished Podcast Edit", "Notes", "Script"]

    # Datetime Variable with custom formatting: (Month Year)
    format = "%B %Y"
    currentDate = datetime.datetime.now().strftime(format)

    # Loop to ensure the user provides a unique folder name and to handle existing directories
    while True:
        
        # Ask the user for the name of the Project Root Folder
        newFileStructureName = input("\nPlease enter the name of the new file structure: \n")

        # Add the current date to the new file structure name
        newFileStructureName = newFileStructureName + " " + currentDate

        # Select the file path for QM Projects In Depth with SCUBA Q Multimedia Podcast folder
        newFileDirectory = os.path.join(podcastFilePath, newFileStructureName)

        # Check if the directory already exists
        if os.path.exists(newFileDirectory):
            print("\nThe file structure " + newFileStructureName + " already exists. Please choose a different name.")
            continue  
        
        else:
            # Create the new root file structure
            os.mkdir(newFileDirectory)

            # Create the following folders in the Root Folder (Finished Podcast Edit, Original Podcast Recording, Notes, and Script):
            for items in foldersPodcast:
                os.mkdir(os.path.join(newFileDirectory, items))

            # Inform the user that the file structure has been created
            print("\nFile Structure " + newFileStructureName + " has been created successfully!")
            print("\nLocation: " + newFileDirectory)

            # Exit the loop after successful creation
            break