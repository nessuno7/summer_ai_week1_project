#Various import Statements can go here
import json
import social_network_ui
from  social_network_classes import SocialNetwork, Person, Message
from collections import namedtuple

def as_person(dct):
    return Person(dct['name'], dct['year'], dct['password'])
    

def as_message(dct):
    if '__Message__' in dct:
        return Message(dct['text'], dct['receiver'], dct['texter'])
    return dct

current_user = Person("Nicola", 16, "Mamma_Mia")

list_of_people = []
with open("users.json", "r") as json_users_file:
    dict_list_of_people = json.load(json_users_file, object_hook=as_person)
    print(type(dict_list_of_people))
    Person_1 = dict_list_of_people.get()
    print(Person_1)

print(type(list_of_people))

with open("current_user.json", "r") as json_current_user_file:
    my_list = json.load(json_current_user_file)
    print(type(my_list))
    print(my_list)
    name = my_list[0]
    print(name)
    age = my_dict.
    password = my_dict.get["password"]

    current_user = Person(name, age, password)

with open("current_user.json", "r") as json_current_user_file:
    current_user = json.load(json_current_user_file, object_hook= as_person)


print(type(current_user))
#lambda d : namedtuple('X', d.keys())(*d.values())



list_of_people = [Person("0", 0, "0")]
with open("users.json", "r") as json_users_file:
    list_of_people = json.load(json_users_file, object_hook=as_person)
index_list_of_people = len(list_of_people)
print(type(list_of_people))


list_of_messages = []
with open("messages.json", "r") as json_messages_file:
    list_of_messages = json.load(json_messages_file, object_hook=as_message)
index_list_of_messages = len(list_of_messages)

ai_social_network = SocialNetwork()

social_network_ui.save_social_media(list_of_people, list_of_messages, current_user)


#ai_social_network.reload_social_media()


#The line below is a python keyword to specify which 
if __name__ == "__main__":
    print("########################################################")
    print("          Welcome to Summer AI Social Network")
    print("########################################################")
    
    #last_menu = None
    
    keep_social_open = True
    logged_in = False

    while keep_social_open == True: 
        
        if logged_in == False:
            choice = social_network_ui.mainMenuLoggedOff()
            continue_mainMenuLoggedOff_loop = True
            
            while continue_mainMenuLoggedOff_loop == True:
                continue_mainMenu_loop = False

                if choice == "1":
                    print("\nYou are now in the create account menu")
                    social_network_ui.create_account(list_of_people, index_list_of_people)
                    logged_in = False
                    social_network_ui.save_social_media(list_of_people, list_of_messages, current_user)
                    break
                
                elif choice == "2":
                    print("\nYou are now in the Login menu")
                    continue_loop = True

                    while continue_loop == True:
                        current_user = social_network_ui.loginMenu(list_of_people, index_list_of_people)

                        if(current_user == None):
                            print("\nLogin Failed")
                            x = None
                            while x == None:
                                x = input("Try again [1]yes, [2]no: ") #asks whether he wants to try to login again
                                if x == "1":
                                    continue_loop = True
                                elif x == "2":
                                    continue_loop = False
                                else:
                                    print("invalid input, please try again")
                                    x = None
                        else:
                            continue_loop = False
                            logged_in = True

                        social_network_ui.save_social_media(list_of_people, list_of_messages, current_user)
                    break

                elif choice == "3":
                    print("Thank you for visiting. Goodbye")
                    keep_social_open = False
                    break

                else:
                    print("invalid input, please try again")
                    continue_mainMenuLoggedOff_loop = True
                    break

        else:
            continue_mainMenuLoggedIn_loop = True
            
            while continue_mainMenuLoggedIn_loop == True:
                choice = social_network_ui.mainMenuLoggedIn()

                if choice == "1":
                    continue_manageAccountMenu_loop = True  #Handle inner menu here

                    while continue_manageAccountMenu_loop == True:
                        choice_2 = social_network_ui.manageAccountMenu()

                        if choice_2 == "1":
                            print("Edit my details")
                            social_network_ui.change_credentials(current_user)
                            social_network_ui.save_social_media(list_of_people, list_of_messages, current_user)
                            print("-----------------------------------")
                            break
                        
                        elif choice_2 == "2":
                            print("Add a Friend")
                            name_search = input("search friend by name in the database: ")
                            friend_found = False

                            for i in range(0, index_list_of_people):
                                if(list_of_people[i].name == name_search):
                                    current_user.add_friend(list_of_people[i].name)
                                    friend_found = True
                                    break
                            
                            if(friend_found == True):
                                print(name_search, "added succesfully to your friendlist")
                            else:
                                print(name_search, "not found")
                            
                            social_network_ui.save_social_media(list_of_people, list_of_messages, current_user)
                            print("-----------------------------------")
                            break

                        elif choice_2 == "3":
                            print("These are all your friends: ")
                            friend_count = 0
                            for i in range(0, current_user.friendlist_index):
                                friend_count += 1
                                print(current_user.friendlist[i])
                            
                            if friend_count == 0:
                                print("you have no friends :(")
                            
                            print("-----------------------------------")
                            break

                        elif choice_2 == "4":
                            social_network_ui.receive_messages(list_of_messages, index_list_of_messages, current_user)
                            print("-----------------------------------")
                            break

                        elif choice_2 == "5":
                            print("Send Message") #chmage with function
                            social_network_ui.send_message(current_user)
                            social_network_ui.save_social_media(list_of_people, list_of_messages, current_user)
                            print("-----------------------------------")
                            break

                        elif choice_2 == "7":
                            print("going back to main menu")
                            print("...")
                            continue_manageAccountMenu_loop = False
                            continue_mainMenuLoggedIn_loop = True
                            break

                        elif choice_2 == "6":
                            print("Your information: ")
                            print("name: ", current_user.name)
                            print("age: ", current_user.age)
                            print("password: ", current_user.password)
                            print("-----------------------------------")
                            break

                        else:
                            print("invalid input, please try again")
                            break

                        ai_social_network.save_social_media()

                elif choice == "2":
                    print("Logging off")
                    print("...")

                    social_network_ui.log_off(current_user)
                    social_network_ui.save_social_media(list_of_people, list_of_messages, current_user)

                    logged_in = False
                    continue_mainMenuLoggedIn_loop = False
                    break

                elif choice == "3":
                    print("Quitting social media")
                    print("...")
                    keep_social_open = False
                    continue_mainMenuLoggedIn_loop = False
                    break

                else:
                    print("invalid input, please try again")
                    break
                    
                social_network_ui.save_social_media(list_of_people, list_of_messages, current_user)

social_network_ui.save_social_media(list_of_people, list_of_messages, current_user)