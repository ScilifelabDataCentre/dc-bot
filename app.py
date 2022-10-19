import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# Initializes your app with your bot token and socket mode handler
app = App(token=os.environ.get("SLACK_BOT_TOKEN"),
          signing_secret=os.environ.get("SLACK_SIGNING_SECRET"))


@app.message("Hi dc-bot!")
def message_hello(message, say):
    say(f"Hi <@{message['user']}>!\nI am DC-bot. Hope you can teach me how to talk at the dev meetup on Nov 21!")


# Start your app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))
