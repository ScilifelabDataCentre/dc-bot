import os

from slack_bolt import App
#from slack_bolt.adapter.socket_mode import SocketModeHandler

import helpers

app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"), signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)


@app.message("Hi dc-bot!")
def message_hello(message, say, logger):
    say(f"Hi <@{message['user']}>! My name is DC-bot.")


@app.event("message")
def default_message_response():
    pass


@app.event("app_mention")
def respond_to_mention(body, say, logger):
    message = body["event"]["text"].lower()
    parts = message.split()
    if len(parts) == 1:
        say(f"Hi <@{body['event']['user']}>!")
    elif parts[1] == "github":
        if len(parts) > 2:
            if parts[2] == "help":
                say(
                    (
                        "Information about using Github is available on "
                        "<https://scilifelab.atlassian.net/wiki/spaces/DC/pages/2198339588/Using+Github|Confluence>"
                    )
                )
            elif parts[2] == "org":
                say(
                    "Data Centre has an organisation on <https://github.com/ScilifelabDataCentre|Github>"
                )
    elif parts[1] == "menu":
        if len(parts) > 2:
            restaurant_info = helpers.get_menu(parts[2])
            if restaurant_info:
                if restaurant_info["menu"]:
                    blocks = [
                        {
                            "type": "section",
                            "text": {
                                "type": "mrkdwn",
                                "text": f"Today at *{restaurant_info['name']}*",
                            },
                        }
                    ]
                    for entry in restaurant_info["menu"]:
                        blocks.append(
                            {
                                "type": "section",
                                "text": {
                                    "type": "mrkdwn",
                                    "text": entry,
                                },
                            }
                        )
                    say(blocks=blocks, text=f"Today at *{restaurant_info['name']}*")
                else:
                    say(f"Unable to retrieve the menu for *{restaurant_info['name']}*")
            else:
                say("Unable to retrieve the menu")
        else:
            pass  # should probably list the choices here as a silent message


@app.event("member_joined_channel")
def respond_to_channel_join(body, say, logger):
    """Greetings when people join channels."""
    say(f"Check if userid: <@{body['event']['user']}>")
    if body["event"]["channel"] == "GQY2NLTPA":
        say(f"Welcome <@{body['event']['user']}> to the Data Centre Development Team!")
    elif body["event"]["channel"] == "GADPJCJRW":
        say(f"Welcome <@{body['event']['user']}> to SciLifeLab Data Centre!")


# Start your app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))
#    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
