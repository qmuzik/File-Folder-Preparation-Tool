"""
- File Folder Preparation Tool: Mocap Shoot Footage
- This script is designed to create a file/folder structure for recorded mocap shoot footage of various mocap systems
- By Quincy Muzik 5/26/2025
"""

# API's / Modules
import os

def mocapShootFootageFolderStructure():

    # Mocap Shoot Footage File Path(s) 
    optiTrackMocapShootFootageFilePath = "J:\Mocap\Mocap Shoot Footage\OptiTrack"
    viconMocapShootFootageFilePath = "J:\Mocap\Mocap Shoot Footage\Vicon"
    moveOneMocapShootFootageFilePath = "J:\Mocap\Mocap Shoot Footage\MoveOne"

    # Mocap Shoot Footage Folder Names
    foldersMocapShootFootage = ["Edited", "Misc", "Raw", "Reel"]

    # Loop to ensure the user selects a valid Mocap System
    while True:
        
        # Ask the user for the type of Mocap System they are using 
        mocapSystemResponse = input("\nWhat type of mocap system are you using? Please enter one of the following options: \n 1. OptiTrack \n 2. Vicon \n 3. MoveOne\n")

        # Break the loop if the user selects a valid Mocap System
        if mocapSystemResponse == "1" or mocapSystemResponse == 'OptiTrack' or mocapSystemResponse == 'optitrack' or mocapSystemResponse == "2" or mocapSystemResponse == 'Vicon' or mocapSystemResponse == 'vicon'or mocapSystemResponse == "3" or mocapSystemResponse == 'MoveOne' or mocapSystemResponse == 'moveone':
            break
        
        # Print an error message if the user enters an invalid option
        else:
            print("\nInvalid option selected. Please select a valid mocap system (OptiTrack, Vicon, or MoveOne)")
            continue
    
    # Loop to ensure the user provides a unique folder name and to handle existing directories
    while True:
        
        # If the user selects OptiTrack then
        if mocapSystemResponse == "1" or mocapSystemResponse == 'OptiTrack' or mocapSystemResponse == 'optitrack':

            # Ask the user for the name of the Project Root Folder
            newFileStructureName = input("\nPlease enter the name of the new file structure: \n")

            # Select the file path for QM Projects Drive Canon R8 Camera Album
            newFileDirectory = os.path.join(optiTrackMocapShootFootageFilePath, newFileStructureName)

            # Check if the root directory already exists
            if os.path.exists(newFileDirectory):
                print("\nThe file structure " + newFileStructureName + " already exists. Please choose a different name.")
                continue
            
            # If it does not exist, create the new root directory
            else:

                # Create the new root file structure
                os.mkdir(newFileDirectory)

                # Create the following folders in the Root Folder (Footage, Reel, and Thumbnails):
                for items in foldersMocapShootFootage:
                    os.mkdir(os.path.join(newFileDirectory, items))

                # Inform the user that the file structure has been created
                print("\nFile Structure " + newFileStructureName + " has been created successfully!")
                print("\nLocation: " + newFileDirectory)

                # Exit the loop after successful creation
                break

    # else if its Vicon then
        elif mocapSystemResponse == "2" or mocapSystemResponse == 'Vicon' or mocapSystemResponse == 'vicon':

            # Ask the user for the name of the Project Root Folder
            newFileStructureName = input("\nPlease enter the name of the new file structure:\n")

            # Select the file path for QM Projects Drive Canon R8 Camera Album
            newFileDirectory = os.path.join(viconMocapShootFootageFilePath, newFileStructureName)

            # Check if the root directory already exists
            if os.path.exists(newFileDirectory):
                print("\nThe file structure " + newFileStructureName + " already exists. Please choose a different name.")
                continue
            
            # If it does not exist, create the new root directory
            else:

                # Create the new root file structure
                os.mkdir(newFileDirectory)

                # Create the following folders in the Root Folder (Footage, Reel, and Thumbnails):
                for items in foldersMocapShootFootage:
                    os.mkdir(os.path.join(newFileDirectory, items))

                # Inform the user that the file structure has been created
                print("\nFile Structure " + newFileStructureName + " has been created successfully!")
                print("\nLocation: " + newFileDirectory)

                # Exit the loop after successful creation
                break

        # Else if its MoveOne then
        elif mocapSystemResponse == "3" or mocapSystemResponse == 'MoveOne' or mocapSystemResponse == 'moveone':

            # Ask the user for the name of the Project Root Folder
            newFileStructureName = input("\nPlease enter the name of the new file structure:\n")

            # Select the file path for QM Projects Drive Canon R8 Camera Album
            newFileDirectory = os.path.join(moveOneMocapShootFootageFilePath, newFileStructureName)

            # Check if the root directory already exists
            if os.path.exists(newFileDirectory):
                print("\nThe file structure " + newFileStructureName + " already exists. Please choose a different name.")
                continue
            
            # If it does not exist, create the new root directory
            else:

                # Create the new root file structure
                os.mkdir(newFileDirectory)

                # Create the following folders in the Root Folder (Footage, Reel, and Thumbnails):
                for items in foldersMocapShootFootage:
                    os.mkdir(os.path.join(newFileDirectory, items))

                # Inform the user that the file structure has been created
                print("\nFile Structure " + newFileStructureName + " has been created successfully!")
                print("\nLocation: " + newFileDirectory)

                # Exit the loop after successful creation
                break