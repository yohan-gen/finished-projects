# password_generator

import random, math, os, string
import time, json

letters = list(string.ascii_lowercase)
Capletters = list(string.ascii_uppercase)
numbLIST = [str(i) for i in range(10)]
symbLIST = ["!","@","#","$","&","*",".",",","/",";"]


class passmanager() :
    
    def __init__(self, filename="PWdata.json"):
        self.filename = filename
        
    def loadpasswords(self) :
        if os.path.exists(self.filename) :
            try :
                with open(self.filename, "r") as lpws :
                    return json.load(lpws)
            except  json.JSONDecodeError:
                return {}
        return {}
    
    def savePWS(self, passwords) :
        
        with open(self.filename, "w") as saverPWS :
            json.dump(passwords, saverPWS, indent=4)
            
    def addPWS(self, description, password) :
        passwords = self.loadpasswords()
        passwords[description] = password
        self.savePWS(passwords)
        print(f"\n Passwords saved succesfully: '{description}'")
        
        
    def displayPWS(self) :
        passwords = self.loadpasswords()
        if not passwords:
            print("\n No passwords saved")
            return False
        
        print("\n" + "="*50)
        print("Saved passwords : ")
        print("="*50)
        for idx, (desc, pwd) in enumerate(passwords.items(), 1):
            print(f"[{idx}] {pwd} -- {desc}")
        print("="*50 + "\n")
        return True

    def editPWS(self) :
        if not self.displayPWS():
            return 
        
        passwords = self.loadpasswords()
        descriptions = list(passwords.keys())
        
        print("Digite o número da senha que deseja editar/remover:")
        
        try :
            choice = int(input("> "))
            if 1 <= choice <= len(descriptions) :
                selected_desc = descriptions[choice - 1]
                
                print(f"\n Selected password: {passwords[selected_desc]} -- {selected_desc}")
                print("[1] Editar descrição")
                print("[2] Editar senha")
                print("[3] Remover senha")
                print("[4] Cancelar")
                
                action = int(input("\n Choose an option: "))
                
                if action == 1 :
                    newdesc = input("\nNew description : ")
                    passwords[newdesc] = passwords.pop(selected_desc)
                    self.savePWS(passwords)
                    print(f"✓ Descrição alterada para '{newdesc}'")
                    
                elif action == 2 :
                    newpwd = input("\n New password : ")
                    passwords[selected_desc] = newpwd
                    self.savePWS(passwords)
                    print("\nPasswords updated ✓")
                    
                elif action == 3 :
                    confirm = str(input(f"Are you sure you want to delete the password : '{selected_desc}'? yes or no"))
                    if confirm.lower() == "yes" :
                        del passwords[selected_desc]
                        self.savePWS(passwords)
                        print("\n Password removed ✓")
                
                elif action == 4 :
                    print("\nOperation canceled ")
            else :
                print("Invalid number!")
        except (ValueError, IndexError) :
            print("Wrong Value")
        
    def clearALL(self, ) :
        confirm = str(input("Are you sure you want to delete all your saved passwords? yes or no : "))
        if confirm.lower() == "yes" :
            self.savePWS({})
            print("All passwords deleted ✓")
        else :
            print("Operation canceled")



class parameters() :
        
    def length(self) :

        while True :                                                    # while choosing the passwords length, it will keep the user on this loop
            options = {1: 6, 2: 8, 3: 10, 4: 12, 5: 14, 6: 16, 7: 20}
            print("\n" + "="*40)
            print("Select the password length\n")
            print("\n" + "="*40)
            for v, k in options.items() :
                print(f"[{v}]---{k} Digits\n")
                
            try :
                choice = int(input())
                if choice not in options :
                    print("Invalid option!\n")
                    continue
                
                confirm = str(input(f"Confirm {options[choice]} digits? yes or no : "))
                if confirm == "yes":
                    return options[choice]
                elif confirm == "no":
                    print("Try again\n")
                else:
                    print("Type yes or no\n")
            except ValueError:          # catches non-integer input
                print(" yes or no only\n")

    def yes_no(self, question) :
        
        while True:
            try :
                ask = str(input(f"{question} yes or no : "))
                if ask == "yes" :
                    return True
                elif ask == "no" :
                    return False
                else : print("Only Yes or No ")
            except ValueError :
                print("Only Yes or No")
                
    def lowercase(self) :
        return self.yes_no("Include lowercase letters ")
    
    def uppercase(self) :
        return self.yes_no("Include UPPERCASE letters ")
    
    def numbers(self) :
        return self.yes_no("Include numbers? (0-9) ")
    
    def symbols(self) :
        return self.yes_no(f"Include $ymb0ls : (! @ # $ & * . , / ;)")
            
            
class generator() :
    
    def __init__(self, length, lowercase=True, uppercase=True, numbers=True, symbols=True):
        
        self.length = length
        self.lowercase = lowercase
        self.uppercase = uppercase
        self.numbers = numbers
        self.symbolcho = symbols
        
        self.letters = list("abcdefghijklmnopqrstuvwxyz")
        self.capletters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        self.numbers_list = list("0123456789")
        self.symbols_list = list("!@#$&*.,/;")
    
    def pass1gen(self) :
        pool = []
        
        if self.lowercase :
            pool += self.letters
        if self.uppercase :
            pool += self.capletters
        if self.numbers :
            pool += self.numbers_list
        if self.symbolcho :
            pool += self.symbols_list
            
        if not pool:
            return "what the fuck?"
        password = list(random.choice(pool) for _ in range(self.length))
        for _ in password :
            random.shuffle(password)
        password = "".join(password)
        return password


def main() :
    
    pm = passmanager()
    
    print("\n" + "="*50)
    print("\n Welcome to the password manager!")
    print("="*50)
    
    while True :
        
        print("\n Options : ")
        print("[1] Manage your saved passwords")
        print("[2] Generate new password")
        print("[3] Exit the program")
        
        try :
            choice = int(input("\n Choose an option : "))
            
            if choice == 1:
                if not pm.displayPWS() :
                    continue
            
                print("[1] Edit/remove specific password")
                print("[2] Clear all passwords")
                print("[3] Return to the menu")
            
                subchoice = int(input("\nChoice : "))
                
                if subchoice == 1 :
                    pm.editPWS()
                if subchoice == 2 :
                    pm.clearALL()
                if subchoice == 3 :
                    continue
            
            elif choice == 2 :
                p = parameters()

                length = p.length()
                lowercase = p.lowercase()
                uppercase = p.uppercase() 
                nums = p.numbers()
                syms = p.symbols()
                
                if not any([lowercase, uppercase, nums, syms]) :
                    print("\n ❌ Error you need to select at least one element to compose your password")
                    continue
                
                g = generator(length,lowercase, uppercase, nums, syms)
                
                print("\n" + "="*40)
                print("Parameters chosen : ")
                print(f"Length :  {'✓' if length else '❌'}")
                print(f"Lowercase :  {'✓' if lowercase else '❌'}")
                print(f"Uppercase :  {'✓' if uppercase else '❌'}")
                print(f"Numbers :  {'✓' if nums else '❌'}")
                print(f"Symbols :  {'✓' if syms else '❌'}")
                print("\n" + "="*40)
                
                print("\n Generating password", end="", flush=True)
                for _ in range(5) :
                    time.sleep(0.5)
                    print(".", end="", flush=True)
                    
                password = g.pass1gen()
                
                print(f"\n Password generated -- {password}\n")
                
                save = input("Do you wish to save your password? yes or no : ").lower()
                
                if save == "yes" :
                    description = input("Give your password a description")
                    pm.addPWS(description, password)
            
            elif choice == 3 :
                print("\nProgram terminated...")
                break
            else : 
                print("❌ invalid option! choose only between options 1 to 3")
                
        except ValueError:
            print("\n❌ You can only type numbers!")
        except KeyboardInterrupt:
            print("\n❌ Sorry the program was interrupted")
            
if __name__ == "__main__":
    main()