# Q) Install an external module and perform an operation using of your Interest .

# Sol:- pip install "Module"

# Process of Using - 
 # import as Module
    # respective command

#Ex. Step 1 ( Performed in Terminal ) pip install pyttsx3
    # Step 2 Code for Operation
import pyttsx3
engine = pyttsx3.init()
engine.say("My name is Joshep Paul")
engine.runAndWait()