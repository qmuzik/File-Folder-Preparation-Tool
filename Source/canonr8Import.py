"""
- File Folder Preparation Tool: Canon R8 Import
- This script is designed to create a file/folder structure for the Canon R8 camera photography album
- By Quincy Muzik 5/21/2025
"""

#API's / Modules
import os
import datetime

def createCanonR8FolderStructure():

    # Camera File Path
    canonR8FilePath = "J:\Photography\Albums\Canon R8 Album"

    # Camera Folder Names
    foldersCanonR8PicturesCR3Watermark = ["CR3","Non Watermarked", "Watermarked"]
    foldersCanonR8PicturesEssential = ["JPG", "TIFF", "PNG"]

    # Datetime Variable with custom formatting: (YYYY_MM_DD)
    format = "%Y_%m_%d"
    currentDate = datetime.datetime.now().strftime(format)

    # Check if the QM Projects Drive exists
    if not os.path.exists(canonR8FilePath):
        print("\nThe file path " + canonR8FilePath + " does not exist. Please check the path and try again.")
        return
    
    # If the QM Projects Drive exists, ask the user if they want to create a new file structure
    else:

        # Loop to ensure the user provides a unique folder name and to handle existing directories
        while True:

            # Ask the user for the name of the Root Folder
            newFileStructureName = input("\nPlease enter the name of the new file structure:\n")

            # Remove any leading or trailing whitespace
            newFileStructureName = newFileStructureName.strip()  

            # Add the current date to the new file structure name
            newFileStructureName = currentDate + " " + newFileStructureName
        
            # Select the file path for QM Projects Drive Canon R8 Camera Album
            newFileDirectory = os.path.join(canonR8FilePath, newFileStructureName)

            # Check if the root directory already exists
            if os.path.exists(newFileDirectory):
                print("\nThe file structure " + newFileStructureName + " already exists. Please choose a different name.")
                continue
            
            # If it does not exist, create the new root directory
            else:   
                
                # Create the new root file structure
                os.mkdir(newFileDirectory)

                # Create the Non Watermarked and Watermarked folders
                for items in foldersCanonR8PicturesCR3Watermark:
                    os.mkdir(os.path.join(newFileDirectory, items))

                # Folder Paths for Watermark and Non Watermarked Folders
                watermarkedFolderPath = os.path.join(newFileDirectory, "Watermarked")
                nonWatermarkedFolderPath = os.path.join(newFileDirectory,"Non Watermarked")

                # Create the following folders in the Non Watermarked and Watermarked folders (JPG, CR3, TIFF, and PNG):
                for items in foldersCanonR8PicturesEssential:
                    os.mkdir(os.path.join(watermarkedFolderPath, items))
                    os.mkdir(os.path.join(nonWatermarkedFolderPath,items))

                # Inform the user that the file structure has been created
                print("\nFile Structure " + newFileStructureName + " has been created successfully!")
                print("\nLocation: " + newFileDirectory)

                # Exit the loop after successful creation
                break 