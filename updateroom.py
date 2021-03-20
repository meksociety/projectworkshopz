from firebase import firebase


firebase = firebase.FirebaseApplication(
    "https://sleepyhotelzoo-default-rtdb.firebaseio.com/
", None
)

print("1.Private room")
print("2.Package room")
print("3.Group room")
x = input("Input you TYPE of room you want to update:  ")

if x == "1":
    print("########### Private room ###########")
    room_id = input("Input you ID room you want to UPDATE:  ")
    types = input("input you type for update :")
    name = input("input you name of room for update :")
    price = input("input you price for update : ")
    firebase.put(f"Hotel_room/PrivateROOM/{room_id}", "Price", price)
    firebase.put(f"Hotel_room/PrivateROOM/{room_id}", "Type of room", types)
    firebase.put(f"Hotel_room/PrivateROOM/{room_id}", "name_room", name)
elif x == "2":
    print("########### Private room ###########")
    room_id = input("Input you ID room you want to UPDATE:  ")
    types = input("input you type for update :")
    name = input("input you name of room for update :")
    price = input("input you price for update : ")
    firebase.put(f"Hotel_room/PackageROOM/{room_id}", "Price", price)
    firebase.put(f"Hotel_room/PackageROOM/{room_id}", "Type of room", types)
    firebase.put(f"Hotel_room/PackageROOM/{room_id}", "name_room", name)
elif x == "3":
    print("########### Private room ###########")
    room_id = input("Input you ID room you want to UPDATE:  ")
    types = input("input you type for update :")
    name = input("input you name of room for update :")
    price = input("input you price for update : ")
    firebase.put(f"Hotel_room/GroupROOM/{room_id}", "Price", price)
    firebase.put(f"Hotel_room/GroupROOM/{room_id}", "Type of room", types)
    firebase.put(f"Hotel_room/GroupROOM/{room_id}", "name_room", name)
else:
    print("ERROR")