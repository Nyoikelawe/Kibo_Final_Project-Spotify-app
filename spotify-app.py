# Kibo FPWP Final Project
# Put your final project code in this file for submission
# Add the names of the authors, a brief description, and link to your video in the file called 'readme.md'
# Then, you can remove these instruction comments
#This program should open up playlists for you to listen to using your browser.
#The following code does not work on Replit because Replit is unable to open a browser page and play the music. I recommend that you use VS Code as your text-editor. 
#ensure that you use the terminal in VS Code to install the spotipy module before running the code. You can use 'pip install spotipy'. If the webbrowser module is also not available, install it in the same you have done for spotipy.
#The playlists will open in 'Ciano's' spotify account. Since, you have access, please do not tamper with anything. Just hit play or pause to interact with the music
#When your browser opens asking for permission to use python with 'Ciano's' account, hit agree. Copy the url in the address bar for the google page you will be directed to, and copy-paste it into the terminal or console where you are having the output for the code asking you to enter the url you have been redirected to.

#Imports spotipy and webbrowser modules 
import spotipy
import webbrowser

#Credentials that give you access to Ciano's Spotify account
username = '3162onfyedeyw2ineh26nr3ypmoe'
clientID = ''
clientSecret = ''
redirectURI = 'https://google.com/' 

#Using the spotipy module 
oauth_object = spotipy.SpotifyOAuth(clientID,clientSecret,redirectURI)
token_dict = oauth_object.get_access_token()
token = token_dict['access_token']
spotifyObject = spotipy.Spotify(auth=token)
user = spotifyObject.current_user()
print()
#Program output starts here
#Introductory statements for the program
print("Welcome to Spotify for the soul. I know you're going through a hard time in life; therefore, I would like to prescribe some music as medicine. This is my way of expressing so much love for you.")
print()
print("Press Enter to continue......")
input()
print("Would you like a bit of music pick-me-up?")
print()

#user choice if they want to continue
user_input =input("if Yes Enter(Y),if No Enter(N): ".capitalize())

print()
#This loop depends on the user's input on whether or not to continue and follows through with the conditional statements
while True:
    if user_input == 'n' :
        print("We are sorry to see you go but you know where to always find us. Still, here's a encouraging quote: ")
        print('''Just hold on
Let time be patient
You are still strong
Let pain be gracious
Just hold on
              
Sometimes loneliness is the only rest we get 
And the emptiness actually let's us forget
Sometimes forgiveness is easiest in secret
''')
        break
    elif user_input == 'y': # if yes print the categories
        user_name = input("Please enter your favourite nickname: ")
        print()
        while True:
            print("Here's the Categories to choose according to your mood\n")
            menu = '''
    1. Smile
    2. Drown in your Tears
    3. Wave your hands in the air like you don't care
    4. Fight
    5. Recomendations
    6. Exit the program
    '''
            print(menu)
            choices = input (user_name.capitalize()+", Please Enter a number corresponding to your choice: ")
            print()

#Depending on the user's choice playlists will be opened in your browser
            searchQuery = 0
            if choices == '1':
                searchQuery = 'smileciano'
            elif choices == '2':
                searchQuery = 'cryciano'
            elif choices == '3':
                searchQuery = 'nocaresciano'
            elif choices == '4':
                searchQuery = 'fightciano'
            searchResults = spotifyObject.search(searchQuery,1,0,"playlist")
                # Get required data from JSON response.
            tracks_dict = searchResults['playlists']

#Instead of playlists, this choice will open recommended artists. The artist may not show up with their music due to an error within spotify, which is something only Spotify can solve. There's nothing I can do if the error shows up. If there is no error, enjoy the music.
            if choices == '5':
                print("Whenever I feel down, apart from drowning myself with Adele's music (this is where you smirk), I also listen to Njoki Karu, Barbara Wangui, Ciano Maimba, and Matt Ngesa.")
                recommendations = '''
1. Njoki Karu
2. Barbara Wangui
3. Ciano Maimba
4. Matt Ngesa'''
                print(recommendations)
                print()
                choice = input (user_name.capitalize()+", Please Enter a number corresponding to your choice: ")
                print()
                if choice == '1':
                    searchQuery = 'Njoki Karu'
                elif choice == '2':
                    searchQuery = 'Barbara Wangui'
                elif choice == '3':
                    searchQuery = 'Ciano Maimba'
                elif choice == '4':
                    searchQuery = 'Matt Ngesa'
                else:
                    print("Please, enter a number from 1 to 4")
                    print()
                    continue
                searchResults = spotifyObject.search(searchQuery,1,0,"artist")
                # Get required data from JSON response.
                tracks_dict = searchResults['artists']

#This part kills the program
            elif choices == '6':
                break
            tracks_items = tracks_dict['items']
            song = tracks_items[0]['external_urls']['spotify']
                # Open the Song in Web Browser (This is where I am stuck Josiane)

#Accounts for errors concering user's input
            if choices != '1' and choices != '2' and choices != '3' and choices != '4' and choices != '5' and choices != '6':
                print("Enter a number between 1 and 6")
                continue

#Opens the Browser
            print('Songs have opened in your browser.')
            print()
            webbrowser.open(song)
        break

#Accounts for errors involving user input
    else:
        print("Please enter the correct value i.e. y or n.")
        user_input =input("if Yes Enter(Y),if No Enter(N): ".capitalize())
