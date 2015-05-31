'''
Opens the file with nouns, 
finds every noun on the web-page,
parses the webpage
extracts needed data with the help of XPath
and writes it into a new txt file
'''

import lxml.html, urllib

my_file=open('English_nouns.txt')
raw=my_file.read()
f=open("CountOrUncount.txt",'a')
for concept in raw.split()[76930:]:
    url = 'https://en.wiktionary.org/wiki/'+concept
    try:
        page = urllib.request.urlopen(url)
        pageWritten = page.read()
        xmldata = lxml.html.document_fromstring(pageWritten)
        text = xmldata.xpath('//a[@href="/wiki/Appendix:Glossary#uncountable"]')
        f.write(concept+ "-")
        try:
            f.write(text[0].text_content()+ "\n")
        except IndexError:
            f.write('countable'+ "\n")
    except OSError:
        pass

f.close()
