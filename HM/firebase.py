import pyrebase

config = {
    "apiKey": "AIzaSyC4GpwN4YKcb8TMOLlwXF4xk7Ebpz9mS58",
    "authDomain": "connectiontopython-4d957.firebaseapp.com",
    "databaseURL": "https://connectiontopython-4d957.firebaseapp.com",
    "projectId": "connectiontopython-4d957",
    "storageBucket": "connectiontopython-4d957.appspot.com",
    "serviceAccount": "serviceAccountKey.json"
}

firebase_storage = pyrebase.initialize_app(config)

storage = firebase_storage.storage()

storage.child("obi.mp4").put("obi.mp4")
