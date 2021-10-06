import requests, json, time, os, sys
# Wrote this sometime in late 2018/early 2019, 
# idk if twitch still works this way but it probably does
# - Download the top X number of clips from categories in "gameList"
# - Generate a video containing all the clips using ffmpeg

ts    = time.gmtime()
today = time.strftime("%Y-%m-%d", ts)

CLIENTID = 'YOUR-CLIENT-ID'
def makeRequest(game):
    try:
        r = requests.get("https://api.twitch.tv/kraken/clips/top?limit=10&game="+game,
                          headers={"Client-ID": CLIENTID,"Accept": "application/vnd.twitchtv.v5+json"})
        return r.text
    except Exception as e:
        print("Error")
        print(e)

def getSlugs(results):
    try:
        clipList = []
        jResult = json.loads(results)
        for i in jResult["clips"]:
            slugName    = i["slug"]
            broadcaster = i["broadcaster"]["display_name"]
            chanUrl     = i["broadcaster"]["channel_url"]
            viewCount   = i["views"]
            videoObj    = {"slug":slugName,"broadcaster":broadcaster,"url":chanUrl,"views":viewCount}
            clipList.append(videoObj)
        return clipList
    except Exception as e:
        print("Error")
        print(e)

def getURLs(slugs,gameType):
    try:
        urlList = []
        #gameType = gameType.replace("%20","_")
        for s in slugs:
            slugName = s["slug"]
            r = requests.get("https://clips.twitch.tv/api/v2/clips/"+slugName+"/status")
            r2 = json.loads(r.text)
            clip720 = r2["quality_options"][0]["source"]
            bcasturl = s["broadcaster"].split("twitch.tv/")
            filename = gameType + "_" + bcasturl[0] +"_"+ slugName + ".mp4"
            print("Downloading " + filename)
            clipVideo = requests.get(clip720)
            fullpath = "./"+today+"-"+gameType+"/"+filename
            os.makedirs(os.path.dirname(fullpath),exist_ok=True)
            open(fullpath, 'wb').write(clipVideo.content)
            #open('filelist.txt','a').write(filename)
            urlList.append(clip720)
        return urlList
    except Exception as e:
        print("Error")
        print(e)

gameList = ["IRL","Just%20Chatting"]

for g in gameList:
    output  = makeRequest(g)
    print("[+] Enumerating Slugs for %s on %s..."%(g,today))
    slugz = getSlugs(output)
    #print(slugz) # This is the list of data from each
    print("[+] Resolving Clip URLs \n")
    g = g.replace("%20","_")
    urls = getURLs(slugz,g)
    path = "./"+today+"-"+g+"/"
    dirs = os.listdir(path)
    print("[+] Generating File List")
    for file in dirs:
        open(path+"filelist.txt","a").write("file "+file+"\n")
    print("[+] Concatenating Videos")
    os.system("ffmpeg -f concat -safe 0 -i "+path+"filelist.txt"+" -c copy "+path+"output.mp4")
    # print(urls) # The list of urls this was downloaded from
