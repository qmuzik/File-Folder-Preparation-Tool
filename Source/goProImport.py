"""
- File Folder Preparation Tool: GoPro Import
- This script is designed to create a file/folder structure for the GoPro camera
- By Quincy Muzik 5/21/2025
"""

#API's / Modules
import os
import datetime

def createGoProFolderStructure():

    # General File Path
    generalFilePath = "J:\Videography\GoPro Footage"

    # GoPro Camera Folders Names
    foldersGoProCamera = ["Footage", "Reel", "Photos", "Thumbnails"]

    # Datetime Variable with custom formatting: (Month Year)
    format = "%B %Y"
    currentDate = datetime.datetime.now().strftime(format)

    # Loop to ensure the user provides a unique folder name and to handle existing directories
    while True:

        # Ask the user for the name of the Project Root Folder
        newFileStructureName = input("Please enter the name of the new file structure: \n")

        # Add the current date to the new file structure name
        newFileStructureName = newFileStructureName + " " + currentDate

        # Select the file path for QM Projects Drive 
        newFileDirectory = os.path.join(generalFilePath, newFileStructureName)

        # Check if the directory already exists
        if os.path.exists(newFileDirectory):
            print("The file structure " + newFileStructureName + " already exists. Please choose a different name. \n")
            continue

        # If it does not exist, create the new root directory
        else:
            
            # Create the new root file structure
            os.mkdir(newFileDirectory)

            # Create the following folders in the Root Folder (Footage, Reel, Photos, and Thumbnails):
            for items in foldersGoProCamera:
                os.mkdir(os.path.join(newFileDirectory, items))

            # Inform the user that the file structure has been created
            print("File Structure " + newFileStructureName + " has been Created Successfully! \n")
            print("Location: " + newFileDirectory + "\n")

            # Exit the loop after successful creation
            break