"""
- File Folder Preparation Tool: Event Folder Structure
- This script is designed to create a file/folder structure for the Event Folder
- By Quincy Muzik 5/21/2025
"""

# API's / Modules
import os
import datetime

def createEventFolderStructure():

    # Event Folder Path
    eventFilePath = "J:\Events"

    # Event Folder Structure
    foldersEvent = ["Footage", "Reel", "Photos", "Thumbnails"]

    # Loop to ensure the user provides a unique folder name and to handle existing directories
    while True:

        # Ask the user for the name of the Project Root Folder
        newFileStructureName = input("Please enter the name of the new file structure: \n")

        # Ask the user if the need a date in the file structure name
        dateNeeded = input("Do you need a date in the file structure name? (Y/N) \n")

        # Loop to handle the user's response regarding the date in the file structure name
        while True:

            # If the user needs a date in the file structure name, format it accordingly
            if dateNeeded == 'Y' or dateNeeded == 'y':
                format = "%B %Y"
                currentDate = datetime.datetime.now().strftime(format)
                newFileStructureName = newFileStructureName + " " + currentDate
                break
    
            # If the user does not need a date, keep the file structure name as is
            elif dateNeeded == 'N' or dateNeeded == 'n':
                newFileStructureName = newFileStructureName
                break

            # If the user inputs an invalid response, prompt them again
            else:
                print("Invalid input. Please enter 'Y' for Yes or 'N' for No.")
                dateNeeded = input("Do you need a date in the file structure name? (Y/N) \n")
                continue

        # Select the file path for QM Projects Drive Canon R8 Camera Album
        newFileDirectory = os.path.join(eventFilePath, newFileStructureName)

        # Check if the directory already exists
        if os.path.exists(newFileDirectory):
            print("The file structure " + newFileStructureName + " already exists. Please choose a different name. \n")
            continue
        
        # If it does not exist, create the new root directory
        else: 
            
            # Create the new root file structure
            os.mkdir(newFileDirectory)

             # Create the following folders in the Root Folder (Footage, Reel, Photos, and Thumbnails):
            for items in foldersEvent:
                os.mkdir(os.path.join(newFileDirectory, items))

            # Inform the user that the file structure has been created
            print("File Structure " + newFileStructureName + " has been Created Successfully! \n")
            print("Location: " + newFileDirectory + "\n")

            # Exit the loop after successful creation
            break