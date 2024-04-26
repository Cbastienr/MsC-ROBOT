import os
import subprocess

# Chemin vers les modules
MODULES_PATH = "/Users/macbook/EPITECH/Msc/MsC-ROBOT/ROBOT/Modules_test"

def execute_module(module_name):
    module_path = os.path.join(MODULES_PATH, module_name)
    subprocess.run(["python", module_path])

def main():
    # Exécuter le module speechtotext
    execute_module("Speech/speechtotext.py")

    # Exécuter le module texttocommand
    execute_module("Command/texttocommand.py")
    
    # Exécuter le module segmentation
    execute_module("Segmentation/segmentation.py")

    # Exécuter le module resume
    execute_module("Resume/resume.py")

if __name__ == "__main__":
    main()