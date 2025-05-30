from firebase import firebase

# Initialize Firebase
firebase = firebase.FirebaseApplication('https://esp32blockchaindata-default-rtdb.firebaseio.com', None)

def update_firebase(data_value):
    try:
        path = '/ESP322'  # Firebase path
        result = firebase.put(path, 'relay_state', int(data_value))
        print("Data successfully updated in Firebase!")
        return result
    except Exception as e:
        print("Error updating Firebase:", e)

# Example value to update (e.g., 1 for ON, 0 for OFF)
relay_value = 0

# Call function
update_firebase(relay_value)
