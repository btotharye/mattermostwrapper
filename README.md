# Python Mattermost v4 API Wrapper
This will be a api v4 wrapper for mattermost.  The plan is to use this for bots, etc.

# Usage
1. Clone the project and import it into your new script and add the following code to your python file, replace the url, login, and pw to match your settings for your server:

```
m = MattermostAPI("your mattermost url")
m.login("login", "password")

# Test showing the teams
print(m.get_teams())
```

This will login and print out the teams you have to show you how the api works.  More calls will be available soon for the wrapper.


# Testing
This is still in testing phase and I recommend just using the code in ipython to test, you can then interactively after logging in via the

m = MattermostAPI you can call m.get_teams() etc to see live results.

More to come soon after I finish this project.
