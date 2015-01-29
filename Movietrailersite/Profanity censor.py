import urllib.request
import re




def censor(text):
    url = 'http://www.wdyl.com/profanity?q=' + '+'.join(set(re.findall(r'[a-zA-Z]+', text)))
    connection = urllib.request.urlopen(url)
    return re.search('true', str(connection.read())) and "There's Profanity!" or "No profanity"
some_file = open('/Users/oscarestrada/Dropbox/School/Udacity/GIT/recipes/chili-recipe.txt')
contents = some_file.read()
some_file.close()

print(censor(contents))
# print(dir(censor(contents)))