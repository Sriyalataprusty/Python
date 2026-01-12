#Hashing
import hashlib
number = "1234"
number_encoded = number.encode()
number_hashed = hashlib.sha256(number_encoded)
readable_number_hashed = number_hashed.hexdigest()
del number
print(number_hashed)
num = input("Enter a password: ")
num_encoded = num.encode()
num_hashed = hashlib.sha256(num_encoded)
readable_num_hashed = num_hashed.hexdigest()
if number_hashed == num_hashed:
    print("You enter the correct password.")
else:
    print("Invalid pin.Try again.")
