#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: python mcb.pyw save <keyword> - Saves clipboard to keyword.
#        python mcb.pyw <keyword> - loads keyword to clipboard.
#        python mcb.pyw list - loads all keys to clipboard.
#        python mcb.pyw delete <keyword> - Delete value and the key is <keyword>.
#        python mcb.pyw delete - Delete all data.

import sys,pyperclip,shelve

parameterList = ('save','delete','list')

def changeData(Values):

    if Values.lower() == 'save':
        clipboard = pyperclip.paste()
        if len(parameter) == 3:
            shelfFile[parameter[2]] = clipboard 
        else:
            print('Usage:  python mcb.pyw save <keyword> - Saves clipboard to keyword.')
            sys.exit()

    elif Values.lower() == 'list':
        pyperclip.copy(str(list(shelfFile.keys())))
        print('keys already be copied!')

    elif Values.lower() == 'delete':
        if len(parameter) == 2:
            print('Do you want delete all data? type "y" validation.')
            try:
                judge = input().lower()
            except ValueError:
                print('print "y" or others!')
                judge = input().lower()
            if judge == 'y':
                for i in list(shelfFile.keys()):
                    del shelfFile[i]
        elif len(parameter) == 3:
            if parameter[2] in list(shelfFile.keys()):
                del shelfFile[parameter[2]]
            else:
                print('type error, There is no input keys!')
                sys.exit()
        else:
            print('''
            Usage:  python mcb.pyw delete <keyword> - Delete value and the key is <keyword>.
                    python mcb.pyw delete - Delete all data.
            ''')

def copyValues(key):

    pyperclip.copy(shelfFile[key])

parameter = sys.argv
if len(parameter) == 1:
    print('''
    Usage:  python mcb.pyw save <keyword> - Saves clipboard to keyword.
            python mcb.pyw <keyword> - loads keyword to clipboard.
            python mcb.pyw list - loads all keys to clipboard.
            python mcb.pyw delete <keyword> - Delete value and the key is <keyword>.
            python mcb.pyw delete - Delete all data.
    ''')
    sys.exit()

shelfFile = shelve.open('mydata')

if parameter[1] in parameterList:
    changeData(parameter[1])
elif parameter[1] in list(shelfFile.keys()):
    copyValues(parameter[1])
else:
    print('type error, please try again.')    

shelfFile.close()

