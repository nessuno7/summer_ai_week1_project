# You can implement user interface functions here.
from json import JSONEncoder
class ClassEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
    pass

import json
from  social_network_classes import Person, Message

def mainMenuLoggedOff():
    print("")
    print("1. Create a new account")
    print("2. Login into your account")
    print("3. Quit")
    print("********************************************************")
    x = input()
    return x

def manageAccountMenu():
    print("")
    print("1. Edit my details")
    print("2. Add a friend")
    print("3. View all my friends")
    print("4. View all messages")
    print("5. Send message")
    print("6. Show my info")
    print("7. <- Go back ")
    return input("Please Choose a number: ")

def mainMenuLoggedIn():
    print("")
    print("1. Manage account Menu")
    print("2. Logoff your account")
    print("3. Quit")
    return input("Please Choose a number: ")

def loginMenu(list_of_people, index_list_of_people):
    print("")
    name = input("input name: ")
    password = input("input password: ")

    for i in range(0, index_list_of_people):
        if list_of_people[i].name == name:
            if list_of_people[i].name == password:
                return list_of_people[i]
        
    return None

def save_social_media(list_of_people, list_of_messages, current_user):
    users_Json = json.dumps(list_of_people, cls = ClassEncoder, indent = 4)
    with open("users.json", "w") as json_file: #saves new information about the users
        json_file.write(users_Json)

    messages_Json = json.dumps(list_of_messages, cls = ClassEncoder, indent = 4)
    with open("messages.json", "w") as json_file: #saves new information
        json_file.write(messages_Json)

    current_user_Json = json.dumps(current_user, cls = ClassEncoder, indent = 4)
    with open("current_user.json", "w") as json_file: #saves new information
        json_file.write(current_user_Json)
    
    pass

def create_account(list_of_people, index_list_of_people):
    name = input("insert name for new user: ")
    age = input("insert age for new user: ")
    password = input("insert password for the new user: ")
    list_of_people.insert(index_list_of_people, Person(name, age, password))
    index_list_of_people += 1
    pass

def send_message(list_of_messages, index_list_of_messages, current_user):
    texter = current_user.name
    for i in range(0, current_user.friendlist_index):
        print(i, ". ", current_user.friendlist[i])
    
    x = input("Input the number of the frind you want to text: ")
    while int(x) not in range(0, current_user.friendlist_index):
        x = input("Input the number of the frind you want to text: ")

    text =  input("Write the text of the  message: ")

    message = Message(text, current_user.friendlist[x], texter)

    list_of_messages.insert(index_list_of_messages, message)

    index_list_of_messages += 1

def receive_messages(self, ai_social_network):
    print("Checking for new messages ...")
    for i in range(0, self.index_list_of_messages):
        if(ai_social_network.list_of_messages[i].receiver == self.name):
            print(i, ". ", "Message from ", ai_social_network.list_of_messages[i].texter)
            self.inbox_messages.insert(self.inbox_messages_index, ai_social_network.list_of_messages[i].texter)  #add the message texter to the list of messages 
            self.inbox_messages_index += 1
    
    if self.inbox_messages_index == 0:
        print("You have no messages")
    else:
        print("You have messages from: ")
        for i in range(0, self.inbox_messages_index):
            print(i, ". ", self.inbox_messages[i])

        x = input("Input the number of the message you want to read: ")
        x = int(x)

        while int(x) not in range(0, self.friendlist_index):
            x = input("Input the number of the frind you want to text: ")
            x = int(x)

        for i in range(0, self.index_list_of_messages):
            if(ai_social_network.list_of_messages[i].receiver == self.name):
                if(ai_social_network.list_of_messages[i].texter == self.inbox_messages[x]):
                    print(ai_social_network.list_of_messages[i].text)
        
        x = input("")
    
    pass


def add_friend(current_user, name_friend_to_add):
    current_user.friendlist.insert(current_user.friendlist_index, name_friend_to_add) 
    current_user.friendlist_index += 1  
    #implement adding friend. Hint add to self.friendlist
    pass

def change_credentials(current_user):
    current_user.name = input("Change name: ")
    current_user.age = input("Chnage age: ")
    current_user.password = input("Chnage password: ")
    pass

def log_off(current_user):
    current_user.name = "0"
    current_user.age = 0
    current_user.password = "0"
    pass



    
