# contact book by Aute @2022

print("Hello! This is your phone contact book.")

while True:
    d = str(input("To see your contacts press, {}, to add contact {}, to delete press {}, to exit press {}: ".format(
        "s", "a", "d", "e")))
    if d == 's':
        file = open("contacts.txt", "r")
        print(file.read())
    elif d == 'a':
        file = open("contacts.txt", "a")
        name = str(input("Enter name of contact: "))
        number = str(input("Enter number of contact: "))
        confirm = str(input("Confirm by pressing c: "))
        if confirm == 'c':
            file.write("\n {} - {}".format(name, number))
            file = open("contacts.txt", "r")
            print("We added your contact...")
            print(file.read())
    elif d == 'd':
        file = open("contacts.txt", "a")
        name = str(input("Enter name of contact: "))
        if file['name'] == name:
            print("Need to delete %s (yes/no)?: " % name)
            name_del = input('> ')
            if name_del == 'yes':
               file.remove(contact)
               print("We delete contact %s " % name)
                #print('Still adding feature')
    elif d == 'e':
        exit()
