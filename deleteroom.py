import json
from firebase import firebase

print("1.Private room")
print("2.Package room")
print("3.Group room")
x = input("Input you TYPE of room you want to DELETE:  ")

firebase = firebase.FirebaseApplication(
    "https://sleepyhotelzoo-default-rtdb.firebaseio.com/", None
)


if x == "1":
    print("########### Private room ###########")
    room_id = input("Input you ID room you want to DELETE:  ")
    result = firebase.delete("/Hotel_room/PrivateROOM", room_id)
    print(result)
elif x == "2":
    print("########### Package room ###########")
    room_id = input("Input you ID room you want to DELETE:  ")
    result = firebase.delete("/Hotel_room/PackageROOM", room_id)
    print(result)
elif x == "3":
    print("########### Group room ###########")
    room_id = input("Input you ID room you want to DELETE:  ")
    result = firebase.delete("/Hotel_room/GroupROOM", room_id)
    print(result)
else:
    print("ERROR")