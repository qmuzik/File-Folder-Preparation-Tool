"""
- File Folder Preparation Tool: Blank Template
- Creates a file/folder structure for a Blank Project Template which the user can customize for project requirements
- By Quincy Muzik 5/22/2025
"""

# API's / Modules
import os
import datetime

def blankTemplateFolderStructure():
    # Path to the QM Projects Drive
    mainDrivePath = "J:"

    # Folder List for the Blank Template
    foldersBlankTemplate = ["Folder1", "Folder2", "Folder3", "Folder4"]

    # Loop to create a new file structure
    while True:

        # Ask the user for the name of the Project Root Folder
        newFileStructureName = input("\nPlease enter the name of the new file structure:\n")

        # Ask the user for the number of folders to create
        numFolders = input("\nHow many folders would you like to create in the " + newFileStructureName + " file structure?\n")

        # Validate the number of folders input
        while True:

            # Check to see if the user entered a number and not a string
            if numFolders.isdigit():

                # Convert the input to an integer
                numFolders = int(numFolders)

                # Check if the number of folders is zero or greater
                if numFolders >= 0:
                    break

                # If the user entered a negative number, prompt them again
                else:
                    print("\nInvalid input. Please enter a valid number (0 or greater).")
                    numFolders = input("\nHow many folders would you like to create in the " + newFileStructureName + " file structure?\n")
                    continue

            # If the user entered a string, prompt them again
            else: 
                print("\nInvalid input. Please enter a valid number (0 or greater).")
                numFolders = input("\nHow many folders would you like to create in the " + newFileStructureName + " file structure?\n")
                continue

        # Ask the user if the need a date in the file structure name
        dateNeeded = input("\nDo you need a date in the file structure name? (Y/N)\n")

        # Validate the dateNeeded input
        while True:

            # If the user needs a date in the file structure name, format it accordingly
            if dateNeeded == 'Y' or dateNeeded == 'y':
                # Datetime Variable with custom formatting: (YYYY_MM_DD)
                format = "%Y_%m_%d"
                currentDate = datetime.datetime.now().strftime(format)
                newFileStructureName =  newFileStructureName + " " + currentDate 
                break
        
            # If the user does not need a date, keep the file structure name as is
            elif dateNeeded == 'N' or dateNeeded == 'n':
                # If no date is needed, do not add it to the file structure name
                newFileStructureName = newFileStructureName
                break

            # If the user enters an invalid input, prompt them again
            else:
                print("\nInvalid input. Please enter 'Y' or 'N'.")
                dateNeeded = input("\nDo you need a date in the file structure name? (Y/N)\n")
                continue

        # Select the file path for QM Projects Drive
        newFileDirectory = os.path.join(mainDrivePath, newFileStructureName)

        # Check if the directory already exists
        if os.path.exists(newFileDirectory):
            print("\nThe file structure " + newFileStructureName + " already exists. Please choose a different name.")
            continue
        
        # If the directory does not exist, create it
        else:
            # Create the new root file structure
            os.mkdir(newFileDirectory)

            # If the user specified a number of folders, create that many folders
            if numFolders > 0:
                # Create the specified number of folders in the Root Folder
                for i in range(1, numFolders + 1):
                    folderName = f"Folder{i}"
                    os.mkdir(os.path.join(newFileDirectory, folderName))

            # If the user specified zero folders, inform them
            elif numFolders == 0:
                print("\nZero folders will be created.")
                    
            # If no specific number is given, create the default blank template folders
            else:  
                print("\nNo specific number of folders provided. Creating default blank template folders.")
                for items in foldersBlankTemplate:
                    os.mkdir(os.path.join(newFileDirectory, items))

            # Inform the user that the file structure has been created
            print("\nFile Structure " + newFileStructureName + " has been created successfully!")
            print("\nLocation: " + newFileDirectory)

            # Exit the loop after successful creation
            break