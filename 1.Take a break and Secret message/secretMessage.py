"""
    A program to decrypt a secret message hidden in the prank original images.
    It renames the images by removing the numbers from them to reveal the secret message.
    Any one can create their own secret message using the alphabets provided.
"""

# import os for operating system functions
import os

# function declaration and definition
def renameFiles():
    # (1) get file names from a folder
    # check the folder path before running the program
    fileList = os.listdir(r"C:\Siddhesh\ACADEMIC\Programming Foundations with Python\prank"); # operating system function
    # display list of files in directory
    print(fileList);
    # what is the current working directory (cwd)?
    savedPath = os.getcwd(); # operating system function
    # display Current working directory
    print("Current working directory is " + savedPath)
    # change cwd
    os.chdir(r"C:\Siddhesh\ACADEMIC\Programming Foundations with Python\prank"); # operating system function
    # (2) for each file, rename filename
    for fileName in fileList:
        # this will run successfully in 2.7
        # display old filenames
        print("Old Name: "+fileName)
        # display new filenames
        print("New Name: "+fileName.translate(None, "0123456789")) # operating system function
        # change filenames
        os.rename(fileName, fileName.translate(None,"0123456789")) # operating system function
        # but in 3.6 run this
        # save renaming parameters in variable
        #pics = str.maketrans(dict.fromkeys('0123456789'))
        # display old filenames
        #print("Old Name: "+fileName)
        # display new filenames
        #print("New Name: "+fileName.translate(pics)) # operating system function
        # change filenames
        #os.rename(fileName, fileName.translate(pics)) # operating system function
    # reset the cwd
    os.chdir(savedPath); # operating system function

# function call
renameFiles();
