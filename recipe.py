#%%
# Recipe for Creating a New Working Project Environment

# Step 1: Go to Github. Create or fork a repository. Forking a repository makes a copy of a pre-existing 
# repository and adds it to your GitHub account. Note: When making a repository, ensure that README file status 
# is turned on, so that we can access the “Code” button (for a later step). 

# Step 2: Once you reach the repository’s homepage, click the green “Code” button where you will be given the option to connect Codespaces onto main 
# – click that button to proceed. This should open a Visual Studio code tab on your web browser, however, it is recommended to do it on Visual Studio code 
# application downloaded to your computer instead of the web browser.

# Step 3: Open the Visual Studio Code application and click the “connect to…” button located in the start menu.
# Then, choose to connect to Codespace. In the search bar -- where it says “Select the codespace to connect to” -- your repository that you had 
# made in GitHub will be listed. 

# Step 4: Once you are in the project and see the start page, open the terminal and create a virtual environment. 
# Syntax for creating a virtual enviornment : `python -m venv “environment name of choice”`

# Step 5: Activate the virtual environment using the following code: `source "environment name of choice”/bin/activate` 

# Step 6: The virtual environment should not be in your repository, for that, we can use a `requirement.txt` file. 
# To do this, install a package that you would need for project. For example, if I wanted to install Plotly, I would 
# type the following syntax: `pip install plotly`. Optional component: You can check the version of a package by using 
# this command: `pip show plotly` this is transferable to any package, just replace the plotly with the respective package name.

# Step 7: To add the implemented package onto a `requirements.txt` file use the following command: `pip freeze > requirements.txt`. 
# This should create a new file titled `requirements.txt` – run that command for everytime you install or update a package.

# Step 8: Create a new Python file by doing option 1 or 2:
# 1. Click the icon with the paper located in the sidebar and type “filename”.py 
# 2. In the terminal, type the following command: `nano ‘file name’.py`

# Step 9: In the side menu, click the icon with 4 boxes -- this section lies all the extensions. There should be 4 tabs within 
# this: Local-Installed, Codespaces, Recommended, MCP Servers. From Local-Installed, you should have extensions that are 
# titled “Jupyter” and “Python” – download those. After installed, they should show up in the Codespace section. 
# If not, you can search them up in the Marketplace search tab. These extensions increase allow us to perform 
# more functions with the code. 

# Step 10: Once all your extensions are successfully installed, add your contents to the python file. 

# Step 11: Once you have finalized the contents of the python file, push it onto GitHub by young 
# the following commands into the terminal: 
#1. `git add .`
#2. `git commit -m ‘personalized message/changes made’`
#3. `git push origin main``
