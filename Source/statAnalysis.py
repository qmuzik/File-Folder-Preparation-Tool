"""
- File Folder Preparation Tool: Statistics Analysis Folder Structure
- This script is designed to create a file/folder structure for the Statistics Analysis Folder 
- By Quincy Muzik 5/21/2025
"""

# API's / Modules
import os

def createStatAnalysisFolderStructure():

    # Stat Analysis File Path
    statisticalAnalysisFilePath = "J:\Statistical and Data Analysis"

    # Stat Analysis Folder Names
    foldersStatisticalAnalysis = ["Code", "Graphs", "Analysis Report", "Data"]

    # Loop to ensure the user provides a unique folder name and to handle existing directories
    while True:

        # Ask the user for the name of the Project Root Folder
        newFileStructureName = input("\nPlease enter the name of the new file structure:\n")

        # Select the file path for QM Projects Drive Canon R8 Camera Album
        newFileDirectory = os.path.join(statisticalAnalysisFilePath, newFileStructureName)

        # Check if the directory already exists
        if os.path.exists(newFileDirectory):     
            print("\nThe file structure " + newFileStructureName + " already exists. Please choose a different name.")
            continue
        
        # If it does not exist, create the new root directory
        else:
            
            # Create the new root file structure
            os.mkdir(newFileDirectory)

            # Create the following folders in the Root Folder (Footage, Reel, and Thumbnails):
            for items in foldersStatisticalAnalysis:
                os.mkdir(os.path.join(newFileDirectory, items))

            # Inform the user that the file structure has been created
            print("\nFile Structure " + newFileStructureName + " has been created successfully!")
            print("\nLocation: " + newFileDirectory)

            # Exit the loop after successful creation
            break