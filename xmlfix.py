import os
import time

print("#########################")
print("######################### Logan's Sid Meier's Railroad's Patcher")
print("######################### https://github.com/loganpiper9/smr_xml_patch")
print("######################### Explanation: Due to a glitch, you cannot play custom SMR maps unless you use this utility.") 
print("######################### This tool changes the file modified timestamp on all XML files to the current time.")
print("######################### This will allow you to launch custom maps without any runtime errors.")
print("#########################")

# Prompt the user for a directory, default to the current one
directory = input(f"Enter the directory path (default is current directory: {os.getcwd()}): ") or os.getcwd()

# Loop through all files in the directory
for filename in os.listdir(directory):
    # Check if the file is an XML file
    if filename.endswith('.xml'):
        # Get the full path to the file
        file_path = os.path.join(directory, filename)
        
        # Update the modified time to the current time
        current_time = time.time()
        os.utime(file_path, (current_time, current_time))

print("Modified dates of all XML files have been updated.")