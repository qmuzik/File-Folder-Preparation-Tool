"""
- File Folder Preparation Tool: Mocap Data
- This script is designed to create a file/folder structure for recorded Mocap Data of various Mocap Systems
- By Quincy Muzik 5/26/2025
"""

# API's / Modules
import os

def mocapDataFolderStructure():

    # Mocap Data File Paths
    optiTrackMocapDataFilePath = "J:\Mocap\Mocap Data\OptiTrack"
    viconMocapDataFilePath = "J:\Mocap\Mocap Data\Vicon"
    moveOneMocapDataFilePath = "J:\Mocap\Mocap Data\MoveOne"

    # Mocap Data Folder Names
    foldersMocapData = ["Data Only", "Reel", "Renders", "With Geometry"]

    # Loop to ensure the user selects a valid Mocap System
    while True:
        
        # Ask the user for the type of Mocap System they are using 
        mocapSystemResponse = input("What type of Mocap System are you using? Please enter one of the following options: \n 1. OptiTrack \n 2. Vicon \n 3. MoveOne \n")

        # Break the loop if the user selects a valid Mocap System
        if mocapSystemResponse == "1" or mocapSystemResponse == 'OptiTrack' or mocapSystemResponse == 'optitrack' or mocapSystemResponse == "2" or mocapSystemResponse == 'Vicon' or mocapSystemResponse == 'vicon'or mocapSystemResponse == "3" or mocapSystemResponse == 'MoveOne' or mocapSystemResponse == 'moveone':
            break
        
        # Print an error message if the user enters an invalid option
        else:
            print("Invalid option selected. Please select a valid Mocap System (1. OptiTrack, 2. Vicon, or 3. MoveOne). \n")
            continue
    
    # Loop to ensure the user provides a unique folder name and to handle existing directories
    while True:
    
        # If the user selects OptiTrack then
        if mocapSystemResponse == "1" or mocapSystemResponse == 'OptiTrack' or mocapSystemResponse == 'optitrack':
                
            # Ask the user for the name of the Project Root Folder
            newFileStructureName = input("Please enter the name of the new file structure: \n")

            # Select the file path for QM Projects Drive Canon R8 Camera Album
            newFileDirectory = os.path.join(optiTrackMocapDataFilePath, newFileStructureName)

            # Check if the root directory already exists
            if os.path.exists(newFileDirectory):
                print("The file structure " + newFileStructureName + " already exists. Please choose a different name. \n")
                continue
    
            # If it does not exist, create the new root directory
            else:
                
                # Create the new root file structure
                os.mkdir(newFileDirectory)

                # Create the following folders in the Root Folder (Footage, Reel, and Thumbnails):
                for items in foldersMocapData:
                    os.mkdir(os.path.join(newFileDirectory, items))

                # Inform the user that the file structure has been created
                print("File Structure " + newFileStructureName + " has been Created Successfully! \n")
                print("Location: " + newFileDirectory + "\n")

                # Exit the loop after successful creation
                break

        # else if its Vicon then
        elif mocapSystemResponse == "2" or mocapSystemResponse == 'Vicon' or mocapSystemResponse == 'vicon':

            # Ask the user for the name of the Project Root Folder
            newFileStructureName = input("Please enter the name of the new file structure: \n")

            # Select the file path for QM Projects Drive Canon R8 Camera Album
            newFileDirectory = os.path.join(viconMocapDataFilePath, newFileStructureName)

            # Check if the root directory already exists
            if os.path.exists(newFileDirectory):
                print("The file structure " + newFileStructureName + " already exists. Please choose a different name. \n")
                continue
            
            # If it does not exist, create the new root directory
            else:

                # Create the new root file structure
                os.mkdir(newFileDirectory)

                # Create the following folders in the Root Folder (Footage, Reel, and Thumbnails):
                for items in foldersMocapData:
                    os.mkdir(os.path.join(newFileDirectory, items))

                # Inform the user that the file structure has been created
                print("File Structure " + newFileStructureName + " has been Created Successfully! \n")
                print("Location: " + newFileDirectory + "\n")

                # Exit the loop after successful creation
                break

        # Else if its MoveOne then
        elif mocapSystemResponse == "3" or mocapSystemResponse == 'MoveOne' or mocapSystemResponse == 'moveone':

            # Ask the user for the name of the Project Root Folder
            newFileStructureName = input("Please enter the name of the new file structure: \n")

            # Select the file path for QM Projects Drive Canon R8 Camera Album
            newFileDirectory = os.path.join(moveOneMocapDataFilePath, newFileStructureName)

            # Check if the root directory already exists
            if os.path.exists(newFileDirectory):
                print("The file structure " + newFileStructureName + " already exists. Please choose a different name. \n")
                continue
            
            # If it does not exist, create the new root directory
            else:
                # Create the new root file structure
                os.mkdir(newFileDirectory)

                # Create the following folders in the Root Folder (Footage, Reel, and Thumbnails):
                for items in foldersMocapData:
                    os.mkdir(os.path.join(newFileDirectory, items))

                # Inform the user that the file structure has been created
                print("File Structure " + newFileStructureName + " has been Created Successfully! \n")
                print("Location: " + newFileDirectory + "\n")

                # Exit the loop after successful creation
                break