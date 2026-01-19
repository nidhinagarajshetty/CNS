import os
import hashlib
def hash_password(password):
    salt=os.urandom(16)
    salted_password=password.encode()+salt
    hash_value=hashlib.sha256(salted_password).hexdigest()
    return salt,hash_value
def verify_password(input_password,stored_salt,stored_hash):
    salted_input=input_password.encode()+stored_salt
    new_hash=hashlib.sha256(salted_input).hexdigest()
    return new_hash==stored_hash
if __name__=="__main__":
    password=input("enter password:")
    salt,hashed=hash_password(password)
    print("\nStored salt:",salt)
    print("Stored hash:",hashed)
    print("\nLogin verification")
    login_password=input("Re-enter password:")
    if verify_password(login_password,salt,hashed):
        print("password verified")
    else:
        print("wrong password")