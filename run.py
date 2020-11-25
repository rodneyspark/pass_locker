from info import Info
from user import User
import string
import random

def created_account(fname,lname,email):
   new_user = User(fname,lname,email)
   return new_user

def create_credentials(facebookp,emailp,instagrampas,twitterpas,facebookusername,instagramusername,twitusername):
    new_cred = Info(facebookp,emailp,instagrampas,twitterpas,facebookusername,twitusername,instagramusername)
    return new_cred
def save_account(user):
    user.save_user()

def save_credentials(credentials):
    credentials.save_info()
    
def display_users():
    return User.display_users()

def display_creds():
    return Info.display_info()

def generatePassword(num):
    password = ''
    
    for n in range(num):
        x = random.randint(0,94)
        password += string.printable[x]
    return password

    
 

def main():
    
    while True:
        print('')
        print('')
        print('Welcome to password locker')
        print('\n')
        print('''
              Select a short code to navigate through:
              'cn' to create a new account: 
              "disp" to display credentials
              "gs" to generate passwords 
              "ex" to exit''')
        short_code = input().lower()
        print('\n')
        
        if short_code == 'cn':
            print('CREATE A NEW ACCOUNT')
            print('')
            
            print('Enter firstname?')
            fname = input()
            print('')
            
            print('Enter lastname?')
            lname = input()
            print('')
            
            print('Enter your email address')
            email = input()
            print('')
            print('Enter your email password?')
            emailp = input()
            print('')
            
            print('Enter facebook Username')
            facebookusername = input()
            print('')
            print('Enter facebook password ')
            facebookp = input()
            print('')
            
            
            
            print('Enter your twitter username?')
            twitusername = input()
            print('')
            print('Enter twitter password')
            twitterpas =input()
            print('')
             
            print('Enter Instagram username ')
            instagramusername = input()
            print('')
            print('Enter Instagram password ')
            instagrampas = input()
            print('')
            
            save_account(created_account(fname,lname,email))
            print('\n')
            save_credentials(create_credentials(facebookp,emailp,instagrampas,twitterpas,facebookusername,twitusername,instagramusername))
            print('-' * 50)
            
            print(f'New Account{fname}{lname} has been created')
            print('\n')
        
        
        elif short_code == 'disp':
            if display_users():
                print('')
                print('The user name')
                print('')
                
                for user in display_users():
                    print(f'{user.fname}{user.lname}')
                    
                for credentials in display_creds():
                    print(f'''
                          facebookusername {facebookusername}
                          facebook password:  {facebookp}
                          Twitter username :  {twitusername}
                          twitter password:  {twitterpas }
                          instagram username: {instagramusername}
                          instagram password: { instagrampas }
                          
                          ''')
                    print('')
            
            
            else:
                print('')
                
                print('Please Create an Account\n You have not created an account')
                
                
        elif short_code == 'gs':
            print('\n')
            print('')
            print('To generate a password enter the number of characters that you will want your password to have:')
            number = int(input())
            print(generatePassword(number))
            
        
        elif short_code == 'ex':
            break
        else:
            print('Enter valid code to continue')
if __name__ == '__main__':
    main()
            