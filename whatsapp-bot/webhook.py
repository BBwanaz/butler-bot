from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse


from apiHelpers import apis

#Declare objects

helper = apis()




app = Flask(__name__)

helpmsg = """\n © *LYRIC BUTLER* by *Bwanaz*\nTo Lookup a song, type its name and artists separated by a comma. \n\nFor example to look up *'ALRIGHT'* by *Kendrick Lamar* type "Alright , Kendrick Lamar"\n \nThe lyrics may be cut off due to capacity issues. \n\nIf your lyrics are cut off, simply type the [SONG NAME] , ARTIST, INDEX. Where index is any number between 2 and 4. \n2 gives you the second fraction of the lyrics and three gives you the third fraction of the lyrics.\n\n For Example the lyrics of *Rap God, Eminem* cut off on the line *"Off a plank and, tell me what.."*. To fetch the next fraction simply type *" Rap God, Eminem, 2"* and the lyrics will continue  """

@app.route('/', methods=['POST'])
def bot():
  
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    try:
        decoded = incoming_msg.split(":", 1)     #Split the first word
    except:
        msg.body(helpmsg)
        return str(resp)
    
    state = apis.decode(decoded[0])

    if state == "dictionary":
        resp_message = apis.dictionary(decoded[1])
    elif state == "genius":
        resp_message = apis.getLyrics(decoded[1])
    elif state == "synonym":
        resp_message = apis.getSynonym(decoded[1])
    else:
        resp_message = helpmsg
  
    msg.body(resp_message)
    responded = True
    
    if not responded:
        msg.body('Please Enter Song name and artist name separated by a comma eg. Chandelier , Sia')
    return str(resp)


if __name__ == '__main__':
    app.run(host = '0.0.0.0')
