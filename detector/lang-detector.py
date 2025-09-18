################### MODULES #############################################
from langdetect import detect, DetectorFactory,detect_langs             #
from langdetect.lang_detect_exception import LangDetectException        #
import pyfiglet as pf                                                   #
import warnings                                                         #
import sys                                                              #
from datetime import datetime                                           #
#########################################################################

############################# BANNER #######
pf = pf.figlet_format("LANG-Detector")     #
print(pf,"\n version 1.0")                 #
print()                                    #
warnings.filterwarnings('ignore')          #
############################################

###################### MAIN CODE ######################################################
print('''
**********************************
* ------------------------------ *
* |Created by Mr. Susanta Banik| *
* ------------------------------ *
**********************************
''')
print("--------------------------- :INPUT: -----------------------------------")
print()
text =str(input("Enter Your Text: "))
print()
print("-----------------------------------------------------------------------")
# Ensure consistent results
DetectorFactory.seed = 0

# Dictionary to map language codes to full language names
language_names = {
    'en': 'English',
    'es': 'Spanish',
    'fr': 'French',
    'de': 'German',
    'it': 'Italian',
    'pt': 'Portuguese',
    'ru': 'Russian',
    'zh-cn': 'Chinese (Simplified)',
    'zh-tw': 'Chinese (Traditional)',
    'ja': 'Japanese',
    'ko': 'Korean',
    'ar': 'Arabic',
    'hi': 'Hindi',
    'bn': 'Bengali',
    'pa': 'Punjabi',
    'ur': 'Urdu',
    'tr': 'Turkish',
    'pl': 'Polish',
    'ro': 'Romanian',
    'nl': 'Dutch',
    'sv': 'Swedish',
    'no': 'Norwegian',
    'da': 'Danish',
    'fi': 'Finnish',
    'cs': 'Czech',
    'el': 'Greek',
    'th': 'Thai',
    'he': 'Hebrew',
    'id': 'Indonesian',
    'ms': 'Malay'
    # Add more languages as needed
}
# Function to detect the language of a given text
try:
    # Detect the language
    lang = detect(text)
    language = language_names.get(lang, "Unknown Language")
    print("The detected language is: "+str(language))
    print()
except Exception as e:
    print("Error detecting language: "+str(e))

# Function to detect the probability of different languages
try:
    # Detect languages with probabilities
    langs = str(detect_langs(text))
    print("Languages with probabilities: "+str(langs))
    print()    
    print("[-]Exited at:",str(datetime.now().strftime("%I:%M %p")),"On",str(datetime.now().strftime("%d %B %Y, %A")))
    print("***********************************************************************")
    sys.exit()
except Exception as e:
    print("Error detecting languages: "+str(e))
    print("[-]Exited at:",str(datetime.now().strftime("%I:%M %p")),"On",str(datetime.now().strftime("%d %B %Y, %A")))
    print("***********************************************************************")    
    sys.exit()
####################################### END OF THE CODE ##################################
