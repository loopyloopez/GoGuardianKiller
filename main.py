import os
import time
process_name = "TheGoGuardianApp.exe"  
while True:
    try:
        os.system(f"taskkill /F /IM {process_name}")
    except:
        print("the task does not exist")
    time.sleep(0.5)