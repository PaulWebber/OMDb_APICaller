#pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib omdb json datetime os subprocess git
from googleapiclient.discovery import build
from google.oauth2 import service_account
import omdb
import json
import datetime
import os
import subprocess
from git import Repo

format = "%Y-%m-%d"
Today = datetime.datetime.today()
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
SERVICE_ACCOUNT_FILE = 'keys.json'

creds = None
creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = 'REMOVED_ID'

service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="Movies!A2:D125").execute()
values = result.get('values', [])
#df = pd.DataFrame(values)
#print(df)

for n in values:
    if datetime.date.fromtimestamp(datetime.datetime.strptime(n[0],format).timestamp()) >= datetime.date.fromtimestamp(Today.timestamp()):
        print(n)
        break

#set the API key
omdb.set_default('apikey', 'REMOVED_KEY')
#response = the search criteria results
response = omdb.get(title=n[1], year=n[2], fullplot=True, tomatoes=True)
#convert json response to python object
resp = json.loads(json.dumps(response))
#folder to put ckad.md in
ckadPath = os.path.join("E:\\Gits\\tehnerdz\content\\","ckad.md")


with open(ckadPath,"w") as ckad:
    print("+++", file=ckad)
    print("author = \"Paul Webber\"", file=ckad)
    print("title = \"" + resp['title']+"\"", file=ckad)
    print("date = \"" + datetime.datetime.now().strftime("%Y-%m-%d") +"\"", file=ckad)
    print("description = \"Screening 8pm on "+n[0]+"\"", file=ckad)
    print("+++\n", file=ckad)
    print("Title: ["+resp['title']+"]("+resp['tomato_url']+")\\", file=ckad)
    print("Trailer: [" + resp['title'] + "](" + n[3] + ")\\", file=ckad)
    print("Year: "+resp['year']+"\\", file=ckad)
    print("Rating: "+resp['rated']+"\\", file=ckad)
    print("Runtime: "+resp['runtime']+"\\", file=ckad)
    print("Genre: "+resp['genre']+"\\", file=ckad)
    print("Plot: "+resp['plot']+"\\", file=ckad)
    print("![Movie]("+resp['poster']+")\\\n", file=ckad)
    print("* [Click to View](https://s.kast.live/g/9da8ll3kwkh)", file=ckad)
    print("* [Click to Chat](https://meet.jit.si/UAFSA)", file=ckad)
    print("* [Click to Add Movies](https://docs.google.com/spreadsheets/d/1ndfumzZ3xnx3cYl-mEmQvv08YH9JOq8IUEzZLYCUeAA/edit#gid=0)", file=ckad)

os.chdir("E:\\Gits\\tehnerdz\\")
print(os.getcwd())
subprocess.run('hugo')

try:
    repo = Repo('E:\\Gits\\tehnerdz\\.git')
    repo.git.add(update=True)
    repo.index.commit("new ckad")
    origin = repo.remote(name='origin')
    origin.push()
    print("Pushed to github")
except:
    print('Some error occured while pushing the code')


#for key, value in response.items():
#        print(key, ":", value)
