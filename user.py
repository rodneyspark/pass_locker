class User:
    '''
    Class that generates instances of the user
    '''
    save_userlist = []
    def __init__(self,fname,lname,email,):
        
        self.fname = fname
        self.lname = lname
        self.email = email
        
    def save_user (self):
        '''
        save_user method saves a new user objectto the user list
        '''
        User.save_userlist.append(self) 
        
        
    def delete_user(self):
        User.save_userlist.remove(self)
        
    @classmethod 
    
    def display_users(cls):
        return cls.save_userlist
    
