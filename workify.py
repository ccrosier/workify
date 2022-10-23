import zipfile
import os
import sys

# optional if tkinter is installed with python
try:
    from tkinter import Tk
    from tkinter.filedialog import askopenfilename
    gui = True
except ImportError:
    gui = False

# constants
SUBMISSIONS = 'submissions'
DEPENDENCIES = {'submissions.zip', 'OsuCseWsTemplate.zip'}
OPTIONS = ['-t', '-h']

def main():

    # selected options
    selected = {'-t': False, '-h': False}

    # assert all required files exist
    if not has_dependencies():
        print('aborting... type \'py workify.py -h\' for help')
        return

    # verify arguments are legitimate
    for arg in sys.argv[1:]:
        if not arg in OPTIONS:
            print('' + arg + ' is an unknown argument')
            print('aborting...')
            return
        selected[arg] = True
        
    if selected['-h']:
        print_help()
        return

    # prompt for input
    project = input('Enter workspace name: ')
    prj_name = input('Enter the EXACT name of of the project: ')
    
    if '-t' in sys.argv:
        if not gui:
            test_path = input('Enter path to test case: ')
        else:
            Tk().withdraw()
            print('select file')
            test_path = askopenfilename(filetypes=[('java files', '.java')])
            Tk().destroy()
        if not os.path.exists(test_path):
            print('invalid path')
            print ('aborting...')
            return

    # extract OsuCseWorkspaceTemplate to project workspace
    with zipfile.ZipFile('OsuCseWsTemplate.zip', 'r') as zip_ref:
        zip_ref.extractall(project)

    workspace = project + '//workspace'

     # extract the original submissions zip file
    with zipfile.ZipFile('submissions.zip', 'r') as zip_ref:
        zip_ref.extractall(SUBMISSIONS)

    # get list of all sub-directories of extraction
    sub_dir = os.listdir(SUBMISSIONS)

    prj_zips = []

    # iterate over sub-directories to find zip files
    for item in sub_dir:
        if ('' + item).endswith('.zip'):
            prj_zips.append(item)

    # unzip projects into workspace
    for folder in prj_zips:
        # get folder name
        folder_name = ('' + folder)[0:6] + '_' + ('' + folder)[6:8]

        # unzip project and move to workspace
        print('importing ' + prj_name + ' project from group ' + folder_name + '... ', end='')
        folder_path = workspace + '//' + folder_name
        with zipfile.ZipFile(SUBMISSIONS + '//' + folder, 'r') as zip_ref:
            zip_ref.extractall(folder_path) 
        os.system('mv ' + folder_path + '//' + prj_name + '//* ' + folder_path)
        os.system('mv ' + folder_path + '//' + prj_name + '//.checkstyle ' + folder_path)
        os.system('mv ' + folder_path + '//' + prj_name + '//.classpath ' + folder_path)
        os.system('mv ' + folder_path + '//' + prj_name + '//.project ' + folder_path)

        if selected['-t']:
            os.system('rm ' + folder_path + '//test//*')
            os.system('cp ' + test_path + ' ' + folder_path + '//test')

        print('done')

    # copy components.jar to workspace
    os.system('cp ' + 'components.jar ' + workspace)

    print('All projects imported')

    # instructions for completing setup
    print('IMPORTANT: open eclipse, use the projectname/workspace as the new workspace. Then')
    print('select File->Import->Projects->ExistingProjects and select the same workspace folder')
    print('Press finish, and the workspace is ready. Unfortunately, projects MUST be imported')
    print('this way for eclipse to show them in the file explorer. Finally, remember to set the')
    print('path of components.jar and enable assertions')

    # remove unzipped submissions
    clean_up()

# checks for required files in dependencies list
def has_dependencies():
    ready = True
    for dep in DEPENDENCIES:
        if not dep in os.listdir('.'):
            print(dep + ' not found')
            ready = False
    return ready

# cleans up unecessary files
def clean_up():
    os.system('rm -r ' + SUBMISSIONS)
    print('Temporary files removed')

# gets path for test file
def get_test_path():
    # if tkinter is installed, a window will open instead of manual path entry
    if not gui:
        test_path = input('Enter path to test case: ')
    else:
        Tk().withdraw()
        print('select file')
        test_path = askopenfilename(filetypes=[('java files', '.java')])
        Tk().destroy()


def print_help():
    print('WORKIFY')
    print('This program extracts and imports eclipse projects from a specified')
    print('zip directory into an eclipse workspace. It expectes the format')
    print('to be as retrieved from CarmenCanvas. It requires that a copy of')
    print('the OsuCseWorkspaceTemplate.zip and submissions.zip be in the current')
    print('working directory. Python 3.x is required.')
    print('\nOPTIONS:')
    print('\t-h:')
    print('\t\tPrints this message.')
    print('\n\t-t:')
    print('\t\tPrompts for the path of a test file to be added to each student project')
    print('\t\tThis will also remove any student created test files')

if __name__ == '__main__':
    main()

