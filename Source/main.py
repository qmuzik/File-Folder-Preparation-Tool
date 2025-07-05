"""
- Project File Folder Preparation Tool: Main Execution
- Main Execution for the Project File Folder Preparation Tool
- This file serves as the entry point for the Proejct File Folder Preparation Tool
- By Quincy Muzik 5/26/2025
"""

#API's / Modules
import fileFolderPreparation

# Main Execution
if __name__ == '__main__':

    # Welcome the user to the script and its purpose
    print("\nProject File Folder Preparation Tool. SCUBA-Q Multimedia 2025.\n")

    # Script runs the File Folder Preparation Tool
    fileFolderPreparation.FileFolderPreparation()

# Loop to ask the user if they want to create another file structure
    while True:

        # Ask the user if they need to create another file structure
        endOfFileStructureCreationUserResponse = input("\nDo you need to create another file structure (Y or N)?\n")

        #  If yes, reset the app to defualt vaules
        if endOfFileStructureCreationUserResponse == 'Y' or endOfFileStructureCreationUserResponse == 'y':
            print("\nResetting the Project File Folder Preparation Tool to default values.\n")
            fileFolderPreparation.FileFolderPreparation()

        #  If not, close the app and terminate execution
        elif endOfFileStructureCreationUserResponse == 'N' or endOfFileStructureCreationUserResponse == 'n':
            print("\nExiting the Project File Folder Preparation Tool. Goodbye!\n")
            exit()

        #  If the user enters an invalid input, prompt them again
        else:
            print("\nInvalid input. Please enter 'Y' or 'N'.")
            continue