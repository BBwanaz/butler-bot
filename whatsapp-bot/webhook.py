from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
import lyricsgenius as lg

genius = lg.Genius('btUspYNxfEDmb0NA_1Gsxvlste8GxwE52pOFk-7J2hVh_DzCXgLxLzqCZw0R3XIs',  # Client access token from Genius Client API page
                             skip_non_songs=True, excluded_terms=["(Remix)", "(Live)"],
                             remove_section_headers=True)

#    song = genius.search_song(song, artist)

app = Flask(__name__)

helpmsg = """\n © *LYRIC BUTLER* by *Bwanaz*\nTo Lookup a song, type its name and artists separated by a comma. \n\nFor example to look up *'ALRIGHT'* by *Kendrick Lamar* type "Alright , Kendrick Lamar"\n \nThe lyrics may be cut off due to capacity issues. \n\nIf your lyrics are cut off, simply type the [SONG NAME] , ARTIST, INDEX. Where index is any number between 2 and 4. \n2 gives you the second fraction of the lyrics and three gives you the third fraction of the lyrics.\n\n For Example the lyrics of *Rap God, Eminem* cut off on the line *"Off a plank and, tell me what.."*. To fetch the next fraction simply type *" Rap God, Eminem, 2"* and the lyrics will continue  """

@app.route('/', methods=['POST'])
def bot():
  
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    result = incoming_msg.split(",")
  
    song = result[0]
    try:
        artist = result[1]
    except IndexError:

        if "help" in result:
            lyric = helpmsg
        else:
            lyric = """\n © *LYRIC BUTLER* by *Bwanaz*\n Text [SONG NAME], [ARTIST], [INDEX] \n Type *HELP* for more info\n\n"""
        msg.body(lyric)
        responded = True
        return str(resp)

    song = genius.search_song(song, artist)
    lyric = song.lyrics
    
    if len(result) == 3:
        index = result[2]
        if int(index) == 1 and len(lyric) > 1450:
            lyric = lyric[:1450]
        elif int(index) == 2 and len(lyric) > 1450*2:
            lyric = lyric[1450: 1450*2]
        elif int(index) == 3 and len(lyric) > 1450*3:
            lyric = lyric[1450*2:1450*3]
        elif int(index) == 4  and len(1450) > 1450 *4:
            lyric = lyric[1450*3:1450*4]
        else:
            lyric = "Requested lyrics unavailable"
    else:
        if len(lyric) > 1450:
            lyric = lyric[:1450]
    lyric =  """\n © *LYRIC BUTLER* by *Bwanaz*\n IF LYRICS ARE CUT OFF TEXT\n [SONG NAME], [ARTIST], [INDEX] \n Type Help for more info\n\n""" + "*" + song.title + "*\n" + lyric
    msg.body(lyric)
    responded = True
    
    if not responded:
        msg.body('Please Enter Song name and artist name separated by a comma eg. Chandelier , Sia')
    return str(resp)


if __name__ == '__main__':
    app.run(host = '0.0.0.0')
