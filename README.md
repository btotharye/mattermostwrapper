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

Get channel listing example code:

```
from mattermost_wrapper import wrapper

m = wrapper.MattermostAPI("https://yoururlhere/api/v4")
m.login("username", "password")

channel_list = m.get_channel_listing('team_name')

for channel in channel_list:
    print(channel['display_name'])
    
```

This will login and print out channel listings for your team.

