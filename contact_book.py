contacts = {}
contacts = {
    "ruhan" : {
        "name" : "ruhan" ,
        "contact" : 987654321 
    },
    "nika" : {
        "name" : "nika" ,
        "contact" : 912345678 
    }
}
while True:
    feature = int(input("Enter 1 to store details\nEnter 2 to see contact list\nEnter 3 to delete a contact\nEnter 4 to exit :"))
    def add_contact():
        name = input("Enter name: ")
        number = int(input("Enter contact no."))

        contacts[name] = {
            "name" : name ,
            "contact" : number
        }
        print("contact added")
        print(contacts[name])

    if feature == 1 :
        add_contact()

    elif feature == 2 :
        person = input("Enter name: ")
        print(contacts[person])

    elif feature == 3 :
        person = input("Enter name you want to delete : ")
        del contacts[person]
        print("contact deleted")

    elif feature == 4 :
        print("EXIT")
        break