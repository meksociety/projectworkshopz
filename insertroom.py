from firebase import firebase


firebase = firebase.FirebaseApplication(
    "https://sleepyhotelzoo-default-rtdb.firebaseio.com/", None
)

print("Choose option for insert")
print("1.Private room")
print("2.Package room")
print("3.Group room")
x = input(":")


if x == "1":
    room_id = input(" Input you ID room :  ")
    name_room = input(" Input you Room name :  ")
    Price = input(" Input Price of Room :  ")
    htz = {"Type of room": "PrivateRoom", "name_room": name_room, "Price": Price}
    result = firebase.put("/Hotel_room/PrivateROOM", room_id, htz)
elif x == "2":
    room_id = input(" Input you ID room :  ")
    name_room = input(" Input you Room name :  ")
    Price = input(" Input Price of Room :  ")
    htz = {"Type of room": "PackageRoom", "name_room": name_room, "Price": Price}
    result = firebase.put("/Hotel_room/PackageROOM", room_id, htz)
elif x == "3":
    room_id = input(" Input you ID room :  ")
    name_room = input(" Input you Room name :  ")
    Price = input(" Input Price of Room :  ")
    htz = {"Type of room": "GroupRoom", "name_room": name_room, "Price": Price}
    result = firebase.put("/Hotel_room/GroupROOM", room_id, htz)
else:
    print("ERROR")