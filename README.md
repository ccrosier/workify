Author: Ryan Crosier

WORKIFY
This program extracts and imports eclipse projects from a specified
zip directory into an eclipse workspace. It expectes the format
to be as retrieved from CarmenCanvas. It requires that a copy of
the OsuCseWorkspaceTemplate.zip and submissions.zip be in the current
working directory. Python 3.x is required.

------------------------------------------------------------------
INSTALLATION
------------------------------------------------------------------
Windows:
If python is not already installed, you can download the installer
for windows from the python website or use a package manager like
choco and run 'choco install python3' from an elevated terminal

Mac:
If python is not already installed, you can download the installer
for mac from the python website or use a package manager like
homebrew and run 'brew install python' from a terminal

Ubuntu:
If python is not already installed, run 'sudo apt install python3'

GUI functionality is available and for the '-t' option and will
run if tkinter, which comes with most python releases is installed

------------------------------------------------------------------
USAGE
------------------------------------------------------------------
Windows:
In your grading directory, run 'py workify.py'

Mac/Linux:
In your grading directory, run 'python3 workify.py'

Whether you need to run using 'py', 'python' or 'python3' may be
dependant on your system

------------------------------------------------------------------
OPTIONS
------------------------------------------------------------------
There are currently three options you can run workify with:

-t: Prompts the user for a test case with a GUI file select if
tkinter is installed, otherwise will prompt for a full file path

-c: 'Cleans' the student test cases from each project, useful
for de-cluttering the workspace since a PDF of the test cases
should be available on CarmenCanvs anyways

-h: prints a help message













 
