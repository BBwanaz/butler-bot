from PyDictionary import PyDictionary
import lyricsgenius as lg
import requests

credit = "\n © BUTLER* by *Bwanaz*\n\n"
covidmsg = """Help stop the spread of COVID 19. Always remember to:\n1. Wash or sanitize your hands frequently\n2  Wear a mask in public places and make sure it covers your mouth and nose\n3. Keep a physical distance of atleast 2m from other people\n\n*Disclaimer*: These tips were derived from the WHO website and we take NO responsibility should they fail to work.
                """



# Declare objects for our helper modules
mydict = PyDictionary()
genius = lg.Genius('btUspYNxfEDmb0NA_1Gsxvlste8GxwE52pOFk-7J2hVh_DzCXgLxLzqCZw0R3XIs',  # Client access token from Genius Client API page
                             skip_non_songs=True, excluded_terms=["(Remix)", "(Live)"],
                             remove_section_headers=True)
class apis:
    
  #  def __init__(self):

#=====================================================================================================================================================
#                COVID STATS
#=====================================================================================================================================================
    def getCovidStats(country):
        res = ""
        parameter = {'country' : country}
        print(country)
        #response = requests.get("https://coronavirus-tracker-api.herokuapp.com/v2/locations", params = parameter)
        response = requests.get("https://coronavirus-19-api.herokuapp.com/countries/"+country, params = parameter)
        
        print(response.status_code)

        if response.status_code != 200:
            return credit + "Something Went Wrong. Check country spelling"
        else:
            stats = response.json()#['latest']
            print(stats)
          #  blurb = "Covid Stats in" + country + "\n"
          #  for key,value in stats.items():
          #      res = res + key + " : " + str(value) + "\n"
            res = res + "*Country* : " + str(stats['country']) + "\n"
            res = res + "Total Cases : " + str(stats['cases']) + "\n"
            res = res + "Active : " + str(stats['active']) + "\n"
            res = res + "Deaths : " + str(stats['deaths']) + "\n"
            res = res + "Recovered : " + str(stats['recovered']) + "\n\n"
            res = res + "Today, " + str(stats['todayCases']) + " new cases were discovered  and " + str(stats['todayDeaths']) + " new deaths occured. " + str(stats['critical']) + "People are in critical condition.\n\n" 
            return credit + res + covidmsg
        
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
                return credit + """ Text [Lyrics:] [SONG NAME], [ARTIST], [INDEX] \n Type *HELP* for more info\n\n"""
            
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
        lyric =  credit + """ IF LYRICS ARE CUT OFF TEXT\n [SONG NAME], [ARTIST], [INDEX] \n Type Help for more info\n\n""" + "*" + song.title + "*\n" + lyric
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
        if decoded.lower().strip() == "covid":
            return "covid"

#==================================================================================================================================================================================================
#   Get Definition
#==================================================================================================================================================================================================
    def dictionary(decoded):
        result = ""
    # Do nothing
        mean = mydict.meaning(decoded)        # Remove the curly brackets
        print(mean)

        if mean == None:
            return credit + "Word not found"

        for key, value in mean.items():
            result = result + "*" + key + "*" + ": \n\n"
            for i in value:
                result = result + " - " +  i + "\n\n"
            

        return credit + result

#==================================================================================================================================================================================================
#   Get SYnonym
#==================================================================================================================================================================================================


    def getSynonym(decoded):
        result = ""
        syn = mydict.synonym(decoded)        # Remove the curly brackets
        if syn == None:
             return credit + "Word not found"

        result = "*Synonyms*: \n"
        for i in syn:
            result = result + " - " +  i + "\n"
            

        return credit + result
            
