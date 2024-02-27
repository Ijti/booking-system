import sqlite3, datetime, re
# This imports the appjar library and datetime
 
connect = sqlite3.connect(         #Imports the SQLite3 library so i can use it alongside my python code
    "FootballBookingDatabase.db")  # This line will make a connection that should create a database
cursor = connect.cursor() # Makes the cursor into an object and will perform SQL commands
from appJar import gui  # will import the library
 
app = gui("FootballBookingSystem", "600x400") # Makes the GUI screen 600x400
 
 
#app.showSplash("Welcome to Southbury Leisure Centre", fill="orange", stripe = "red", fg="black", font=44)
 
 
#####################################Interface############################################
def CreateInterface():        # the function to create my user interface
    
    
    #Create login subwindow
    app.startSubwindow("Login")
    app.setTitle("Login") # the title of this subwindow will be labelled as Login
    app.addLabel("Welcome to Southbury leisure centre")#This will output on the GUI will welcome the user
    app.addLabelEntry("Emailaddress") # This will take user inputs specifically for the users emailaddress
    app.setBg("white", override=False) #This will set the background of the login screen to red
    app.setFg("black", override=False) # This will set the Foreground to white
    app.addLabelSecretEntry("Password")  #takes in user inputs for their password and the characters inputted will be showsn as an asterisk for security reasons
    app.image('Fusion.png', value='Fusion.png')
    app.setEntryBg("Password", 'orange')
    app.setEntryBg("Emailaddress", 'orange')
    app.setEntryFg("Password", "black")
    app.setEntryFg("Emailaddress", "black")
    app.addButton("Enter", login) #Adds the button called enter, if/when pressed it will run the login function
    app.addButton('Create New User',lambda: app.showSubWindow('Create an Account'))
    app.setLabelBg('Welcome to Southbury leisure centre', 'red')
    #Reference w3schools When the button is presed it will temporarily run the subwindow create an account
 
    #The code below is the subwindow for main menu that has buttons for booking a pitch, canelling a booking and logging out
 
    app.startSubWindow("Main Menu", "600x400")
    app.setTitle("Main menu")
    app.addButton("Book a pitch", lambda: app.showSubWindow('Book a pitch'))# When book a pitch is pressed a lambda it will run the subwindow book a pitch, using lambda is more efficient
    app.setfg("white", override=False)
    app.setButtonBg('Book a pitch','red')
    app.setButtonFg('Book a pitch','black')
    app.setFg("orange", override=False)
    app.addButton("Cancel a booking", lambda: app.showSubWindow('Cancel booking'))
    app.setButtonFg('Cancel a booking','black')
    app.setButtonBg('Cancel a booking','orange')
    app.addButton("Log out", log_out)
    app.setButtonFg('Log out','black')
    app.setButtonBg('Log out','green')    
    app.stopSubWindow()
 
    #the code below is the subwindow for creating an account this will allow users to an email address and password once for choice and the second time to confirm
 
    app.startSubWindow("Create an Account")
    app.setTitle("New Account")
    app.addLabel('Create A New Account')
    app.setLabelBg('Create A New Account','red')
    app.setBg("white", override=False)
    app.setFg("black", override=False)
    app.addLabelEntry("Enter Emailaddress")
    app.addLabelSecretEntry("    Enter Password")
    app.addLabelSecretEntry("Confirm Password")
    app.setEntryBg('Enter Emailaddress', 'orange')
    app.setEntryBg('    Enter Password','orange')
    app.setEntryBg('Confirm Password','orange')
    app.setEntryFg('Enter Emailaddress','black')
    app.setEntryFg('    Enter Password','black')
    app.setEntryFg('Confirm Password','black')
    app.addButton("Confirm", account_new)
    app.addButton
    app.addButton("Back ", lambda: app.showSubWindow('Login'))
    
    app.stopSubWindow()
    app.startSubWindow("Cancel booking")
 
    # The code below is the subwindow for cancelling a booking, it allows input for the user emailaddress
 
    app.startSubwindow("Cancel booking")
    app.setTitle("Cancel booking")
    app.addLabelEntry("Enter your email address")
    app.addLabelEntry("Enter Booking ID")
    app.addLabel("Would you like to cancel your booking")
    app.setBg("white", override=False)
    app.setLabelFg("Enter your email address", "black")
    app.setEntryBg('Enter your email address','orange')
    app.setLabelFg("Enter Booking ID", "black")
    app.setEntryBg('Enter Booking ID','orange')
    app.setLabelFg("Would you like to cancel your booking", "black")
    #Add email address and booking id entries
 
    app.addButton("Yes", cancel_booking)
    app.addButton("Back  ", lambda: app.showSubWindow('Main Menu'))
 
    app.stopSubWindow()
 
    app.startSubWindow('Book a pitch')
    app.addLabel('Book a pitch')
    app.setLabelBg('Book a pitch','red')
    app.addLabelEntry("Enter your Emailaddress")
    app.setLabelFg("Enter your Emailaddress", "black")
    app.setEntryBg('Enter your Emailaddress', 'orange')
    app.addLabelEntry("Enter date in form as dd/mm/yyyy")
    app.setLabelFg("Enter date in form as dd/mm/yyyy", "black")
    app.setEntryBg("Enter date in form as dd/mm/yyyy", "orange")
    app.addLabelEntry("Enter 5 for 5-a-side, 7 for 7-a-side, 11 or 11-a-side")
    app.setLabelFg("Enter 5 for 5-a-side, 7 for 7-a-side, 11 or 11-a-side", "black")
    app.setEntryBg("Enter 5 for 5-a-side, 7 for 7-a-side, 11 or 11-a-side", "orange")
    app.setBg("white")
    app.addButton("enter", book_pitch)
    app.addButton("Back", lambda: app.showSubWindow('Main Menu'))
    app.stopSubWindow()
    app.go()
 
 
    ########## login system   ###########################
 
def login(): #The subroutine/function for login
    # Emailaddress Password
    emailaddress = app.getEntry('Emailaddress')#fetches the email address
    password = app.getEntry('Password')#fetches the password
    connect = sqlite3.connect(         #Imports the SQLite3 library so i can use it alongside my python code
    "FootballBookingDatabase.db")  # This line will make a connection that should create a database
    cursor = connect.cursor() # Makes the cursor into an object and will perform SQL commands
    if len(emailaddress) == 0 or len(password) == 0: # boolean, checking if the length of the inputs equals to 0
        print('empty values')
        app.errorBox('error', "Empty Values")# an error box will show saying that the input boxes are empty
        return #Create length error.
    elif emailaddress.find('@') == -1 or emailaddress.find('.com') == -1: #checks if the inputs entered are in the database
        print('email address wrong')
        app.errorBox('error', "Wrong Email address")
        return #Create email address error
    users = cursor.execute('SELECT * FROM Members WHERE Emailaddress=? AND Password=?', [emailaddress, password]).fetchall()
    connect.commit()
    #^ Selects from the database in the table members to fetch the emailaddress and password
    if len(users) == 0:
        print('no user')
        app.errorBox('error', "No user found")
        return #No user found
    app.showSubWindow('Main Menu')
    return
    
    
###################################Create an account######################################
 
 
 
def account_new():  #Subroutine for making a new account
    emailaddress = app.getEntry('Enter Emailaddress') # Gets the input entered
    password = app.getEntry('Enter Password')
    confirm_password = app.getEntry('Confirm Password')
    if len(emailaddress) == 0 or len(password) == 0 or len(confirm_password) == 0:#checks length of inputs
        print('empty values')
        app.errorBox('error', "Length error")
        return #Create length error.
    elif emailaddress.find('@') == -1 or emailaddress.find('.com') == -1:#checks to see if they aren't in database
        print('email address wrong')
        app.errorBox('error', "Wrong email address")
        return #Create email address error
    elif password != confirm_password:
        print('password != confirm_password')
        app.errorBox('error', "The passwords typed do not match")
        return #create password mismatch error.
    cursor.execute('INSERT INTO Members VALUES (?,?)', [emailaddress, password])#updates database
    connect.commit()
    app.infoBox("Information", "Your details have been saved")
    print('Data saved') #Create information message informing user.
    app.hideSubWindow('Create an Account')#Hides subwindow
    return
    
##################### cancel booking ####################
 
 
def cancel_booking():
    Booking_id = app.getEntry('Enter Booking ID')
    Emailaddress = app.getEntry("Enter your email address")
    
    if len(Emailaddress) == 0 or len(Booking_id) == 0:
        print('empty values')
        app.errorBox('error', "Empty Values")
        return #Create length error.
    elif Emailaddress.find('@') == -1 or Emailaddress.find('.com') == -1:
        print('email address wrong')
        app.errorBox('error', "Wrong Email address")
        app.startSubWindow("Cancel Booking")
        return #Create email address error
    users = cursor.execute('SELECT * FROM Members WHERE Emailaddress=?', [Emailaddress]).fetchall() 
    if len(users) == 0:
        app.errorBox('error', "No booking")
        app.startSubWindow("Cancel Booking")
        return
    if Booking_id != "PID5" or  Booking_id != "PID7" or  Booking_id != "PID11":
        app.errorBox('Error','Not a correct Booking ID')
        return
    else:
        app.infoBox('Information','Your booking has been cancelled')
    #SQL statement would delete if it finds it in database otherwise nothing happens.
    cursor.execute("""
        DELETE FROM BookingsList WHERE Emailaddress=? AND BookingID=?
    """, [Emailaddress, Booking_id])
    connect.commit()
    app.infoBox('Information','Your booking has been cancelled')
    
    #Add information message stating that booking has been cancelled.
 
    #app.hideSubWindow('Cancel booking')
    return
 
 
def book_pitch():
    #Get the date and select all the dates and times not available from the database.
    #This allows me to display all the dates and times available.
    date = app.getEntry('Enter date in form as dd/mm/yyyy')
    # https://www.w3schools.com/python/python_regex.asp
    if not re.match('[0-9]{2}/[0-9]{2}/[0-9]{4}', date): 
        # this will make sure the user enters the date in the specififed format
        app.errorBox('Error', "Not in the specified format dd/mm/yyyy")
        return
    day_entered, month_entered, year_entered = date.split('/')
    try:                                     # https://www.w3schools.com/python/python_try_except.asp
        # Checks to see if the data entered is a valid date.
        correct_date = datetime.datetime(int(year_entered), int(month_entered), int(day_entered))
    except ValueError:
        return app.errorBox('Error', "Not a correct date")
    if correct_date <= datetime.datetime.today():
        #This line above checks to see if the date entered hasn't passed
        app.errorBox("Error", "This date has passed, enter another date")
        return
    emailaddress = app.getEntry('Enter your Emailaddress')#fetches the email address
    if emailaddress.find('@') == -1 or emailaddress.find('.com') == -1: #checks if the inputs entered are in the database
        app.errorBox("Error", "Email address not in specified format")
        return
    pitch_size = 'PID' + app.getEntry('Enter 5 for 5-a-side, 7 for 7-a-side, 11 or 11-a-side')
    #my code below
    if pitch_size != "PID5" and pitch_size !="PID7" and  pitch_size != "PID11":
        app.errorBox("Error", "Wrong pitch size entered")
        return
    #my code above
    Emailaddress = app.getEntry('Enter your Emailaddress')
    unavailable_slots = cursor.execute('''
        SELECT PitchID, Booking_date FROM BookingsList WHERE Booking_date=? AND PitchID=?
    ''', [date, pitch_size]).fetchall()
    if len(unavailable_slots) > 0:
        app.errorBox("Error", "Booking unavailable")
        return
    cursor.execute('''
        INSERT INTO BookingsList(PitchID, Booking_date, Emailaddress)
        VALUES (?,?,?)
    ''', (pitch_size, date, Emailaddress))
    connect.commit()
    app.infoBox("Info","Booking saved, the price to be paid is £10")
    app.hideSubWindow('Book a pitch')
    return app.showSubWindow('Main Menu')
    
 
def log_out():
    #Removes all subwindows displays and then displays the login subwindow.
    app.hideAllSubWindows()
    return
 
 
def build_database():   #Subroutine/function that will run to make a database
     #"cursor.execute" performs SQL command to make the table known as "Bookinglist" if it doesn't exist. Hence why it says in down below "IF NOT EXISTS"
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS BookingsList (
        BookingID INTEGER PRIMARY KEY,
        PitchID TEXT NOT NULL,
        Booking_date DATE NOT NULL,
        Emailaddress TEXT NOT NULL,
        FOREIGN KEY (PitchID) REFERENCES Pitch(PitchID)
        FOREIGN KEY (Emailaddress) REFERENCES Members(Emailaddress)
    )
    """) #Foreign Key Information from https://www.w3schools.com/sql/sql_foreignkey.asp    
    #"cursor.execute" performs SQL command to make the table known as "Members" if it doesn't exist. Hence why it says in down below "IF NOT EXISTS"
    cursor.execute('''CREATE TABLE IF NOT EXISTS `Members` (
    	`Emailaddress`	TEXT NOT NULL UNIQUE,
    	`Password`	TEXT NOT NULL,
    	PRIMARY KEY(Emailaddress)
     )''')
    #"cursor.execute" performs SQL command to make the table known as "Pitches" if it doesn't exist. Hence why it says in down below "IF NOT EXISTS" 
    cursor.execute('''CREATE TABLE IF NOT EXISTS `Pitches` (
    	`5-a-side`	TEXT,
    	`7-a-side`	TEXT,
    	`11-a-side`	TEXT
     )''')
    connect.commit()
 
#build_database()
 
 
 
CreateInterface()
 
