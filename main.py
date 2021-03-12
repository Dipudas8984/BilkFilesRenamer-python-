import os
import time
# os.rename("file.mp3","new_file.mp3")
list = [i for i in os.listdir() if '.py' not in i]
# for i in range(len(list)):
#     os.rename(list[i], f"{i}>{list[i]}")

method = input('''Press enter to go default
or press anyhting to enter a renge of number: ''')

if method == '':
    num = [i+1 for i in range(len(list))]
else:
    num_range = int(input("Enter The Num Range Of Your Files(*list will go from 0 upto the range) : "))
    num = [i for i in range(num_range)]

print('\n',num)
press = input("\nPress 1 to proceed-")
print()
if press == '1':
    pass
else:
    print("exiting...........\n")
    exit()




for i in num:
    char = f"- {i} "#EDIT 'char' here 
    for j in list:
        # print(j)
        if  char in j:
            print(f"{j} > {i}-{j.replace(char, '')}")
            os.rename(j, f"{i}-{j.replace(char, '')}")
            time.sleep(.3)
        else:
            pass
        
print('Done')