import os
parent_directory = '/Users/Eoin/OneDrive/Cambridge/IB/General/UROP/CrunchTope-InstallMac/Projects/EoinInput/Archives'
count = 0
new_directory = "ModelAttempt%s" % count
path = os.path.join(parent_directory, new_directory)
if os.path.exists(path):
    count =+ 1
    new_directory = "ModelAttempt%s" % count
    print(new_directory)
path = os.path.join(parent_directory, new_directory)
#os.mkdir(path)