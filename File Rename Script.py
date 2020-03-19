import os

def main():
    i = 0
    print("******* Welcome to File Renamer *******")
    print()
    print("\u2764 \u2764 \u2764 \u2764 \u2764 Created by hk \u2764 \u2764 \u2764 \u2764 \u2764")
    path = input("Enter the desired path or paste it. ")
    print()
    path = path.replace('\\','/')
    path = path + "/"
    name = input("Enter the name of the file that you want to be reflected ")
    print()
    for filename in os.listdir(path):
        
        dst = name + str(i) + ".jpg"
        src = path + filename
        dst = path + dst
        os.rename(src,dst)
        i+=1


if __name__== '__main__':
    main()
    print("Name Changed Succesfully")
    print()
    print("***** Thanks for using our Service \u00A9 hk *****")
    print()
    input("Press Enter to Quit")
                        
