import pickle as pkl

with open('secrets.dat', 'wb') as f:
    data = {'apiKey': "AIzaSyDR8tFTYqMqSYI6K1HAjJBfeS774o3aU5o",
    'authDomain': "spaceblogs.firebaseapp.com",
    'projectId': "spaceblogs",
    'storageBucket': "spaceblogs.appspot.com",
    'messagingSenderId': "113377744070",
    'appId': "1:113377744070:web:60c5f3e34e25b60987b3c7",
    'measurementId': "G-PG3VEDCTC8",
    'databaseURL' : "https://spaceblogs-default-rtdb.asia-southeast1.firebasedatabase.app/"}
    pkl.dump(data,f)
