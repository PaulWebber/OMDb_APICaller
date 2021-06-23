import omdb
import json
import datetime

#set the API key
omdb.set_default('apikey', 'API_KEY_HERE')
#response = the search criteria results
response = omdb.get(title='The Lighthouse', year=2019, fullplot=True, tomatoes=True)
#convert json response to python object
resp = json.loads(json.dumps(response))

with open("ckad.md","a") as ckad:
    print("+++\nauthor = \"Paul Webber\"\ntitle = \"" + resp['title']+"\"\ndate = \""\
          +datetime.datetime.now().strftime("%Y-%m-%d")+"\"" \
          "\ndescription = \"Screening June 25, 2021\"\n+++\n", file=ckad)
    print("Title: ["+resp['title']+"]("+resp['tomato_url']+")\\", file=ckad)
    print("Year: "+resp['year']+"\\", file=ckad)
    print("Rating: "+resp['rated']+"\\", file=ckad)
    print("Runtime: "+resp['runtime']+"\\", file=ckad)
    print("Genre: "+resp['genre']+"\\", file=ckad)
    print("Plot: "+resp['plot']+"\\", file=ckad)
    print("![Movie]("+resp['poster']+")\\\n", file=ckad)
    print("* [Click to View](https://s.kast.live/g/9da8ll3kwkh)", file=ckad)
    print("* [Click to Chat](https://meet.jit.si/UAFSA)", file=ckad)
    print("* [Click to Add Movies](https://docs.google.com/spreadsheets/d/1ndfumzZ3xnx3cYl-mEmQvv08YH9JOq8IUEzZLYCUeAA/edit#gid=0)", file=ckad)

#for key, value in response.items():
#        print(key, ":", value)
