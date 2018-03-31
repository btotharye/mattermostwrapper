[![Stories in Ready](https://badge.waffle.io/btotharye/mattermost_wrapper.png?label=ready&title=Ready)](https://waffle.io/btotharye/mattermost_wrapper?utm_source=badge)
# Python Mattermost v4 API Wrapper
This will be a api v4 wrapper for mattermost.  The plan is to use this for bots, etc.

# Installation
`pip install mattermostwrapper`

# Documentation
Will be updating the documentation but it can be found at http://mattermostwrapper.readthedocs.io/en/latest/

# Usage
1. Clone the project and import it into your new script and add the following code to your python file, replace the url, login, and pw to match your settings for your server as well as your team name you want to interact with:

```
m = MattermostAPI("your mattermost url", "team_name")
m.login("login", "password")

# Test showing the teams
print(m.get_teams())
```

Get channel listing example code:

```
from mattermostwrapper import MattermostAPI

m = MattermostAPI("https://yoururlhere/api/v4")
m.login("username", "password")

channel_list = m.get_channel_listing('team_name')

for channel in channel_list:
    print(channel['display_name'])
    
```

This will login and print out channel listings for your team.

You can also do the following to post a test message to the channel off-topic using the wrapper:
```
from mattermostwrapper import MattermostAPI

m = MattermostAPI("https://yoururlhere/api/v4")
m.login("username", "password")

channel_id = 'channel_id_goes_here'
message = 'This is a test message'
post_message = m.post_channel(channel_id, message)

print(post_message)
```


