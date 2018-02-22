#class User 
class User:
    
    count = 1
    #increments id each time when posted
    def __init__(self,username,email,password):
        self.username =username
        self.email = email
        self.password =password
        self.id = User.count
        User.count +=1


#classs bucket list items
class Bucketlist():
    count = 1
     #increments id each time when posted
    def __init__(self,title,description,date_posted):
        self.title = title
        self.description = description
        self.date_posted = date_posted
        self.id = Bucketlist.count
        Bucketlist.count +=1

        


