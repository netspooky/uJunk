import urllib.request, json, sys, textwrap
# 2019-02-19
# Find public exploits based on CVE. Also works as a github search in general :P
# Run like
# python3 pubsploit.py CVE-2017-0143

def cveSearch(cve):
    with urllib.request.urlopen('http://cve.circl.lu/api/cve/'+cve) as url:
        data = json.loads(url.read().decode())
        try:
            if data['cvss']:
                print("{} | CVSS {}".format(cve,data['cvss']))
            if data['summary']:
                print('+-- Summary '+'-'*68+"\n")
                print('\n'.join(textwrap.wrap(data['summary'],80)))
                print()
            if data['exploit-db']:
                print('+-- ExploitDB '+'-'*66)
                for d in data['exploit-db']:
                    print("| Title | {}".format(d['title']))
                    print("|   URL | {}".format(d['source']))
                    print("+-------+"+"-"*71)
                print()
            if data['packetstorm']:
                print('+-- Packet Storm '+'-'*63)
                for p in data['packetstorm']:
                    print("| Title | {}".format(p['title']))
                    print("|   URL | {}".format(p['data source']))
                    print("+-------+"+"-"*71)
                print()
            if data['metasploit']:
                print('+-- Metasploit '+'-'*65)
                for m in data['metasploit']:
                    print("| Title | {}".format(m['title']))
                    print("|    ID | {}".format(m['id']))
                    print("|   URL | {}".format(m['source']))
                    print("+-------+"+"-"*71)
                print()
        except (TypeError, KeyError) as e:
            print('oof')
            print(e)

def gitSearch(cve):
    with urllib.request.urlopen('https://api.github.com/search/repositories?q='+cve) as url:
        data = json.loads(url.read().decode())
        try:
            print('+-- GitHub '+'-'*69)
            for i in data['items']:
                print("|  Repo | {}".format(i['full_name']))
                print("|  Desc | {}".format(i['description']))
                print("|   URL | {}".format(i['html_url']))
                print("+-------+"+"-"*71)
        except (TypeError, KeyError) as e:
            print('oof')
            print(e)
            
cve = sys.argv[1]
cveSearch(cve)
gitSearch(cve)
