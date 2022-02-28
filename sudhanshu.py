import sys

def logo():
    print('''   _____           _ _                     _           
  / ____|         | | |                   | |          
 | (___  _   _  __| | |__   __ _ _ __  ___| |__  _   _ 
  \___ \| | | |/ _` | '_ \ / _` | '_ \/ __| '_ \| | | |
  ____) | |_| | (_| | | | | (_| | | | \__ \ | | | |_| |
 |_____/ \__,_|\__,_|_| |_|\__,_|_| |_|___/_| |_|\__,_|

============= My Name is Sudhanshuuuuu ===============\n
Beta: Only works for objects having single value,\n      multiple value support will come in BASH Script!
''')

def usage():
    print('''Usage Guide:
                python3 sudhanshu.py filename.json object_name''')


def core_action(value_choice,action_choice):
    with open(sys.argv[1]) as f:
        content=f.read()
        data=content.splitlines()
        # print(data)
        

    with open(f'{sys.argv[1]}-new.json', 'w') as fout:
        # print(value_choice)
        if(value_choice==1):
            if (action_choice==1):
                # print(sys.argv[2])
                content=content.replace(sys.argv[2].upper(),sys.argv[2].lower())
                fout.write(content)
            elif(action_choice==2):
                # print(sys.argv[2])
                content=content.replace(sys.argv[2],sys.argv[2].upper())
                # print(content)
                fout.write(content)
            else:
                print("\nWrong Choice!!")
                exit()  
        elif(value_choice==2):
            if(action_choice==1):
               for i in data:
                    if sys.argv[2] in i:
                        temp=i.rsplit(':',1)
                        i=f'"{sys.argv[2]}":'+temp[1].lower()
                    fout.write(i) 
            elif(action_choice==2):
                for i in data:
                    if sys.argv[2] in i:
                        temp=i.rsplit(':',1)
                        i=f'"{sys.argv[2]}":'+temp[1].upper()
                    fout.write(i)
            else:
                print("\nWrong Choice!!")
                exit() 
        else:
            print("\nWrong Choice!!")
            exit() 
            
  
########################## Start script ##############################
logo()
if len(sys.argv)>2:
    value_choice=int(input("\nSelect the type on which action needs to be performed:\n1. Object\n2. Value\n"))
    if(value_choice==1 or value_choice==2):
        action_choice=int(input("\nSelect the action to be performed:\n1. lowercase\n2. uppercase\n"))
        if(action_choice==1 or action_choice==2):
            core_action(value_choice,action_choice)
        else:
            print("\nWrong Choice!!")
            exit()
    else:
        print("\nWrong Choice!!")
        exit()  
else:
   usage()


