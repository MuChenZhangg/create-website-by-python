
def createHomePage(emailuser):
    firstname,lastname=emailuser.split(".")
    file = open(f'{emailuser}.html','w')
    file.write(createDocType())
    file.write(startHTML())
    file.write(createHead(firstname + "'s website"))
    file.write(startBody())
    file.write(createHeading("Welcome to " + firstname + '.' + lastname + "'s webpage"))
    file.write(createParagraph("Hello everyone I am Philemon below is my selfie"))

    file.write(createPic('"'+firstname+'.'+lastname+'.jpeg'+'"'+' alt="my image"+ "width="400"height="500"'))
    file.write(createHeading(sentence()))
    file.write(createHeading(findTemperatureLive()))
    file.write(endBody())
    file.write(endHTML())
    file.close()

def createDocType():
    """Return standard html5 DOCTYPE string."""
    return '<!DOCTYPE html>\n'

def startHTML():
    """Return html start tag."""
    return '<html>\n\n'

def endHTML():
    """Return html end tag."""
    return '</html>\n'
def startBody():
    """Return body start tag."""
    return '<body>\n\n'
def endBody():
    return '</body\n>'
def createHead(text):
    return'<head>\n''<title>' + text + '</title>\n''</head>\n'
def createPic(src):
    return '<img src=' +src+ '/>\n'


def createHeading(text):
    return '<h1>' + text + '</h1>\n'
def createParagraph(text):
    return'<p>\n' + text + '\n</p>\n'
import requests
def findTemperatureLive():  
    """Print the current temperature in Wenham using data from localconditions.com.
  
    This function depends on knowledge of the page structure - if they change
    the page structure, the program will not work!
    """

    # Get the weather page
    weather = requests.get("https://www.localconditions.com/weather-boston-massachusetts/01984/").text

    # The temperature can be found near the top of the page after the word "Wenham" and
    # immediately before the HTML code &deg; (the degree symbol)
    curLoc = weather.find("Wenham")
    if curLoc != -1:
        # Now, find the degree symbol ("&deg;") following the temperature
        degLoc = weather.find("&deg;", curLoc)
        # The temperature number is preceded by a pipe
        tempLoc = weather.rfind("|", 0, degLoc)
        # Temperature value is everything between the pipe (and space) and the degree symbol
        return "Current temperature in Wenham is "+weather[tempLoc+2:degLoc]+" degrees"
    else:
        return "Page format has changed; cannot find the temperature"

from random import choice

def sentence():
    """Generate a random sentence from a select set."""
    nouns = [
        "Mark",
        "Adam",
        "Angela",
        "Larry",
        "Jose",
        "Matt",
        "Jim"
        ]
    verbs = [
        "runs",
        "skips",
        "sings",
        "leaps",
        "jumps",
        "climbs",
        "fires a Civil War cannon",
        "swims",
        "argues",
        "giggles"
        ]
    phrases = [
        "in a tree",
        "through every room in the house",
        "very loudly",
        "around the bush",
        "while reading the newspaper",
        "very badly",
        "while skipping",
        "instead of grading",
        "while programming Python"
        ]
    return f"{choice(nouns)} {choice(verbs)} {choice(phrases)}."

    



if __name__=="__main__":
    createHomePage('Philemon.Zhang')
    