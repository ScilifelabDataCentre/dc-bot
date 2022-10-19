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
    if "dev meetup" in message:
        say("The dev meetup will be help on November 21")
    elif "team activity" in message:
        say("The team activity will be to give me a voice")
    elif "where is your code" in message:
        say("My code is available at https://github.com/ScilifelabDataCentre/dc-bot")

# Start your app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))
#    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
