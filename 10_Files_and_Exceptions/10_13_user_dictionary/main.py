# 10-13. User Dictionary: The remember_me.py example only stores one piece of information, the username. 
# Expand this example by asking for two more pieces of information about the user, 
# then store all the information you collect in a dictionary. 
# Write this dictionary to a file using json.dumps(), and read it back in using json.loads(). 
# Print a summary showing exactly what your program remembers about the user.


from pathlib import Path
import json

def get_stored_userinfo (path):
    """Get stored user info if available."""
    if path.exists():
        contents = path.read_text()
        userinfo = json.loads(contents)
        return userinfo
    else:
        return None    


def get_new_userinfo (path):
    """Get new user info."""
    name = input("What is your name? ")
    location = input("Where are you from? ")
    color = input("What's your favorite color? ")
    
    userinfo = {
        'name': name,
        'city': location,
        'color': color,
    }
    
    contents = json.dumps(userinfo)
    path.write_text(contents)

    return userinfo


def summary_userinfo ():
    """Print summary about the user."""
    path = Path('userinfo.json')
    userinfo = get_stored_userinfo(path)
    if userinfo:
        print(f"Welcome back, {userinfo['name']}!")
        print(f"You are from {userinfo['city']} and your favorite color is {userinfo['color']}.")
    else:
        userinfo = get_new_userinfo(path)
        print(f"We'll remember your info when you come back, {userinfo['name']}!")
    
summary_userinfo()