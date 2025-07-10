"""
- File Folder Preparation Tool: fileFolderPreparation
- Main Function that creates a file folder structure based on the user's input
- By Quincy Muzik 5/26/2025
"""

#API's / Modules
import canonr8Import, goProImport, event, podcast, statAnalysis, mocapData, mocapShootFootage, pythonTool, blankTemplate

def FileFolderPreparation():

    # Loop for continuous execution 
    while True:

     # Ask the user what is the user creating a file/folder structure for
        fileStructureType = input("What do you need a new file structure created for? Please enter one of the following options: \n 1. Canon R8 Import \n 2. Go Pro Import \n 3. Event \n 4. Podcast \n 5. Stat Analysis \n 6. Mocap Data \n 7. Mocap Shoot Footage \n 8. Python Tool \n 9. Blank Template \n 10. Exit \n")

        # Remove any leading or trailing whitespace
        fileStructureType = fileStructureType.strip()

        # Canon R8 Import
        if fileStructureType == "1" or fileStructureType == 'Canon R8 Import' or fileStructureType == 'canon r8 import' or fileStructureType == 'Canon R8' or fileStructureType == 'canon r8':    
            canonr8Import.createCanonR8FolderStructure()
            break

        # Go Pro Import
        elif fileStructureType == "2" or fileStructureType == 'Go Pro Import' or fileStructureType == 'go pro import' or fileStructureType == 'Go Pro' or fileStructureType == 'go pro':
            goProImport.createGoProFolderStructure()
            break

        # Event
        elif fileStructureType == "3" or fileStructureType == 'Event' or fileStructureType == 'event':
            event.createEventFolderStructure()
            break

        # Podcast
        elif fileStructureType == "4" or fileStructureType == 'Podcast' or fileStructureType == 'podcast':
            podcast.createPodcastFolderStructure()
            break
            
        # Stat Analysis
        elif fileStructureType == "5" or fileStructureType == 'Stat Analysis' or fileStructureType == 'stat analysis' or fileStructureType == "Stat" or fileStructureType == 'stat': 
            statAnalysis.createStatAnalysisFolderStructure()
            break
        
        # Mocap Data
        elif fileStructureType == "6" or fileStructureType == 'Mocap Data' or fileStructureType == 'mocap data':
            mocapData.mocapDataFolderStructure()
            break

        # Mocap Shoot Footage
        elif fileStructureType == "7" or fileStructureType == 'Mocap Shoot Footage' or fileStructureType == 'mocap shoot footage' or fileStructureType == 'Mocap Shoot' or fileStructureType == 'mocap shoot':
            mocapShootFootage.mocapShootFootageFolderStructure()
            break

        # Python Tool
        elif fileStructureType == "8" or fileStructureType == 'Python Tool' or fileStructureType == 'python tool' or fileStructureType == 'Python' or fileStructureType == 'python':
            pythonTool.createPythonToolFolderStructure()
            break

        # Geeneric Blank Template
        elif fileStructureType == "9" or fileStructureType == 'Blank Template' or fileStructureType == 'blank template' or fileStructureType == 'Blank' or fileStructureType == 'blank':
            blankTemplate.blankTemplateFolderStructure()
            break

        # Exit
        elif fileStructureType == "10" or fileStructureType == 'Exit' or fileStructureType == 'exit':
            print("\nExiting the Project File Folder Preparation Tool. Goodbye! \n" )
            exit()

        # Invalid Input
        else:
            print("\nInvalid input. Please enter a valid option. \n")
            continue