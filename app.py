import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# Initializes your app with your bot token and socket mode handler
app = App(token=os.environ.get("SLACK_BOT_TOKEN"),
          signing_secret=os.environ.get("SLACK_SIGNING_SECRET"))


@app.message("Hi dc-bot!")
def message_hello(message, say):
    say(f"Hi <@{message['user']}>! My name is DC-bot.")

@app.event("app_mention")
def respond_to_mention(body, say):
    if body["event"]["text"].lower() == "dev meetup":
        say("The dev meetup will be help on November 21")
    elif body["event"]["text"].lower() == "team activity":
        say("The team activity will be to give me a voice")
    elif body["event"]["text"].lower() == "code":
        say("My code is available at https://github.com/ScilifelabDataCentre/dc-bot")

# Start your app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))
