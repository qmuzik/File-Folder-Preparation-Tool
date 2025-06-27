"""
- File Folder Preparation Tool: Main Execution
- Main Execution for the File Folder Preparation Tool
- This script serves as the entry point for the file folder preparation tool
- By Quincy Muzik 5/26/2025
"""

#API's / Modules
import fileFolderPreparation

# Main Execution
if __name__ == '__main__':

    # Script runs the File Folder Preparation Tool
    fileFolderPreparation.FileFolderPreparation()

    while True:

        # Ask the user if they need to create another file structure
        endOfFileStructureCreationUserResponse = input("Do you need to create another file structure (Y or N)? \n")

        #  If yes, reset the app to defualt vaules
        if endOfFileStructureCreationUserResponse == 'Y' or endOfFileStructureCreationUserResponse == 'y':
            print("Resetting the File Folder Preparation Tool to default values. \n")
            fileFolderPreparation.FileFolderPreparation()

        #  If not, close the app and terminate execution
        elif endOfFileStructureCreationUserResponse == 'N' or endOfFileStructureCreationUserResponse == 'n':
            print("Exiting the File Folder Preparation Tool. Goodbye! \n")
            exit()

        #  If the user enters an invalid input, prompt them again
        else:
            print("Invalid input. Please enter 'Y' or 'N'. \n")
            continue