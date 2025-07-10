"""
- File Folder Preparation Tool: Python Tool
- This script is designed to create a file/folder structure for a Python Tool
- By Quincy Muzik 5/22/2025
"""

#API's / Modules
import os

def createPythonToolFolderStructure():
    
    # Python Tool File Path
    pythonToolsFilePath = "J:\Software Engineering\Python Tools"

    # Folder List
    pythonTool = ["Source", "Documentation", "Exe", "Demo Reel","Logo"]  

    # Check if the QM Projects Drive exists
    if not os.path.exists(pythonToolsFilePath):
        print("\nThe file path " + pythonToolsFilePath + " does not exist. Please check the path and try again.")
        return
    
    # If the QM Projects Drive exists, ask the user if they want to create a new file structure
    else:

        # Loop to ensure the user provides a unique folder name and to handle existing directories
        while True:

            # Ask the user for the name of the Project Root Folder
            newFileStructureName = input("\nPlease enter the name of the new file structure:\n")

            # Remove any leading or trailing whitespace
            newFileStructureName = newFileStructureName.strip()
            
            # Select the file path for QM Projects Python Tools
            newFileDirectory = os.path.join(pythonToolsFilePath, newFileStructureName)

            # Check if the directory already exists
            if os.path.exists(newFileDirectory):
                print("\nThe file structure " + newFileStructureName + " already exists. Please choose a different name.")
                continue
            
            # If it does not exist, create the new root directory
            else:
                
                # Create the new root file structure
                os.mkdir(newFileDirectory)

                # Create the following folders in the Root Folder (Footage, Reel, and Thumbnails):
                for items in pythonTool:
                    os.mkdir(os.path.join(newFileDirectory, items))

                # Inform the user that the file structure has been created
                print("\nFile Structure " + newFileStructureName + " has been created successfully!")
                print("\nLocation: " + newFileDirectory)

                # Exit the loop after successful creation
                break