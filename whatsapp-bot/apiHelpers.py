from PyDictionary import PyDictionary
import lyricsgenius as lg


# Declare objects for our helper modules
mydict = PyDictionary()
genius = lg.Genius('btUspYNxfEDmb0NA_1Gsxvlste8GxwE52pOFk-7J2hVh_DzCXgLxLzqCZw0R3XIs',  # Client access token from Genius Client API page
                             skip_non_songs=True, excluded_terms=["(Remix)", "(Live)"],
                             remove_section_headers=True)
class apis:
    
  #  def __init__(self):
        
#=====================================================================================================================================================
#                GENIUS API
#=====================================================================================================================================================
    def getLyrics(req):
        result = req.split(",") # split the request to get artist and name
        song = result[0]
        try:
            artist = result[1]
        except IndexError:

            if "help" in result:
                return helpmsg
            else:
                return """\n © *LYRIC BUTLER* by *Bwanaz*\n Text [Lyrics:] [SONG NAME], [ARTIST], [INDEX] \n Type *HELP* for more info\n\n"""
            
        song = genius.search_song(song, artist)
        if song == None:
            return "Song not found. Verify spelling and syntax"
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
        return lyric
#==========================================================================================================================================================================================
#               DECODING STAGE
#==========================================================================================================================================================================================
    def decode(decoded):
    # State Machine for decoded message
        if decoded.lower().strip() == "define":
            return "dictionary"
        if decoded.lower().strip() == "lyrics":
            return "genius"
        if decoded.lower().strip() == "synonym":
            return "synonym"

#==================================================================================================================================================================================================
#   Get Definition
#==================================================================================================================================================================================================
    def dictionary(decoded):
    # Do nothing
        mean = mydict.meaning(decoded)        # Remove the curly brackets
        if mean == None:
            mean = "Word not found"
        return mean

#==================================================================================================================================================================================================
#   Get SYnonym
#==================================================================================================================================================================================================


    def getSynonym(decoded):
        syn = mydict.synonym(decoded)        # Remove the curly brackets
        if syn == None:
            syn = "Word not found"
        return syn
