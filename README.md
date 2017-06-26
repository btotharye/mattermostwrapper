# Python Mattermost v4 API Wrapper
This will be a api v4 wrapper for mattermost.  The plan is to use this for bots, etc.

# Usage
1. Change the m = MattermostAPI("") at the end of the script to be your url, eventually will have this setup so it is a variable but still testing.

2. Change the m.login("login", "password") to match your login and password

# Testing
This is still in testing phase and I recommend just using the code in ipython to test, you can then interactively after logging in via the

m = MattermostAPI you can call m.get_teams() etc to see live results.

More to come soon after I finish this project.
