import hashlib as hl
def hash_pw(pw):
    hash=hl.sha256()
    hash.update(pw.encode("utf-8"))
    return hash.hexdigest()
def save_pw(username,pw):
    encrypt=hash_pw(pw)
    with open ("passwords.txt","a") as file:
        file.write(f"{username}:{encrypt}\n")
    print(f"password for {username} saved successfully!")
def find_pw(username):
    with open ("passwords.txt","r") as file:
        for line in file:
            su,sp=line.strip().split(":")
            if username== su:
                return sp
    return None


def main():
    while True:
        print("\n password manager menu")
        print("1. Save Password.")
        print("2. Find Password.")
        print("3. Quit.")
        choice=input("Enter your choice: ")
        if choice =="1":
            username=input("Enter username: ")
            pw=input("Enter password: ")
            save_pw(username,pw)
        elif choice== "2":
            username=input("Enter username to get your password.")
            stored_pw=find_pw(username)
            if stored_pw:
                print(f"Password for {username}:{stored_pw}")
            else:
                print(f"Password for {username} not found. ")
        elif choice=="3":
            print("Exiting password manager.")
            break
        else:
            print("Invalid choice.")

if __name__=="__main__": #to run the main function 
    main()
