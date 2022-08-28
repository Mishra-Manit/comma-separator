#Add a comma after each line of a text file automatically

'''
In order to use this piece of software, you will need to first paste all the emails into emails.txt. 

MAKE SURE EACH EMAIL IS ON A SEPARATE LINE!!

After that, run main.py. Then check formattedEmails.txt. All of the formatted emails will be there.
'''

txt_file = open("emails.txt", "r")
listOfNames = txt_file.read()

def main():
    with open("formattedEmails.txt",'r+') as file:
        file.truncate(0)
        file.close()

    with open("formattedEmails.txt", "w") as file:
        file.write(listOfNames)
        file.close()

    with open("formattedEmails.txt", "r") as f:
        lines = f.read().splitlines()
        f.close()

    with open("formattedEmails.txt", "w") as f:
        for line in lines:
            f.write(line + ",\n")
        f.close()

main()

print("Your emails are done formatting")
