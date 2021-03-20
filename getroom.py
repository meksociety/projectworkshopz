import json
from firebase import firebase

print("1.Private room")
print("2.Package room")
print("3.Group room")
print("#Press enter for see all room")
x = input("Input you TYPE of room you want to see:  ")

firebase = firebase.FirebaseApplication(
    "https://sleepyhotelzoo-default-rtdb.firebaseio.com/", None
)


if x == "1":
    print("########### Private room ###########")
    room_id = input("Input you ID room you want to see:  ")
    result = firebase.get("/Hotel_room/PrivateROOM", room_id)
    print(result)
elif x == "2":
    print("########### Package room ###########")
    room_id = input("Input you ID room you want to see:  ")
    result = firebase.get("/Hotel_room/PackageROOM", room_id)
    print(result)
elif x == "3":
    print("########### Group room ###########")
    room_id = input("Input you ID room you want to see:  ")
    result = firebase.get("/Hotel_room/GroupROOM", room_id)
    print(result)
else:
    result = firebase.get("/Hotel_room", "")
    print(result)