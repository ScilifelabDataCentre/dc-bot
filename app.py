import os
from slack_bolt import App
#from slack_bolt.adapter.socket_mode import SocketModeHandler

app = App(token=os.environ.get("SLACK_BOT_TOKEN"),
          signing_secret=os.environ.get("SLACK_SIGNING_SECRET"))


@app.message("Hi dc-bot!")
def message_hello(message, say, logger):
    say(f"Hi <@{message['user']}>! My name is DC-bot.")

@app.event("message")
def default_message_response():
    pass

@app.event("app_mention")
def respond_to_mention(body, say, logger):
    message = body["event"]["text"].lower()
    if message.endswith("github help"):
        say("Information about using Github is available on <https://scilifelab.atlassian.net/wiki/spaces/DC/pages/2198339588/Using+Github|Confluence>")
    elif message.endswith("github org"):
        say("We have an organisation on <https://github.com/ScilifelabDataCentre|Github>")
    elif message.endswith("hidden channels"):
        say()

@app.event("member_joined_channel")
def respond_to_channel_join(body, say, logger):
    """Greetings when people join channels."""
    say(f"Check if userid: <@{body['event']['user']}>")
    if body["event"]["channel"] == 'GQY2NLTPA':
        say(f"Welcome <@{body['event']['user']}> to the Data Centre Development Team!")
    elif body["event"]["channel"] == 'GADPJCJRW':
        say(f"Welcome <@{body['event']['user']}> to SciLifeLab Data Centre!")

# Start your app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))
#    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
