# 2019-07-05
# This is a test of the dnslib library, used to display art in TXT records

from datetime import datetime
from time import sleep
import random 

from dnslib import DNSLabel, QTYPE, RD, RR
from dnslib import A, AAAA, CNAME, MX, NS, SOA, TXT
from dnslib.server import DNSServer

#EPOCH = datetime(1970, 1, 1)
#SERIAL = int((datetime.utcnow() - EPOCH).total_seconds())
SERIAL = 1111115150

TYPE_LOOKUP = {
    A:     QTYPE.A,
    AAAA:  QTYPE.AAAA,
    CNAME: QTYPE.CNAME,
    MX:    QTYPE.MX,
    NS:    QTYPE.NS,
    SOA:   QTYPE.SOA,
    TXT:   QTYPE.TXT,
}

class Record:
    def __init__(self, rdata_type, *args, rtype=None, rname=None, ttl=None, **kwargs):
        if isinstance(rdata_type, RD):
            # actually an instance, not a type
            self._rtype = TYPE_LOOKUP[rdata_type.__class__]
            rdata = rdata_type
        else:
            self._rtype = TYPE_LOOKUP[rdata_type]
            if rdata_type == SOA and len(args) == 2:
                # add sensible times to SOA
                # Or not lolol
                args += ((
                    SERIAL,  # serial number
                    60 * 60 * 1,  # refresh
                    60 * 60 * 3,  # retry
                    60 * 60 * 24, # expire
                    60 * 60 * 1,  # minimum
                ),)
            rdata = rdata_type(*args)

        if rtype:
            self._rtype = rtype
        self._rname = rname
        self.kwargs = dict(
            rdata=rdata,
            ttl=self.sensible_ttl() if ttl is None else ttl,
            **kwargs,
        )

    def try_rr(self, q):
        if q.qtype == QTYPE.ANY or q.qtype == self._rtype:
            return self.as_rr(q.qname)

    def as_rr(self, alt_rname):
        return RR(rname=self._rname or alt_rname, rtype=self._rtype, **self.kwargs)

    def sensible_ttl(self):
        if self._rtype in (QTYPE.NS, QTYPE.SOA):
            return 60 * 60 * 24
        else:
            return 300

    @property
    def is_soa(self):
        return self._rtype == QTYPE.SOA

    def __str__(self):
        return '{} {}'.format(QTYPE[self._rtype], self.kwargs)

def randomTXT():
    answers = ["lol","yup","yes"]
    answer = random.choice(answers)
    return answer

ZONES = {
    'example.com': [
        Record(A, '1.2.3.4'),
        Record(CNAME, 'whever.com'),
        Record(MX, 'whatever.com.', 5),
        Record(MX, 'mx2.whatever.com.', 10),
        Record(MX, 'mx3.whatever.com.', 20),
        Record(NS, 'mx2.whatever.com.'),
        Record(NS, 'mx3.whatever.com.'),
        #Record(TXT, 'hello this is some text'),
        Record(TXT, randomTXT()),
        Record(SOA, 'ns1.example.com', 'dns.example.com'),
    ],
    'n0.lol': [
        Record(A, '1.3.3.7'),
        Record(CNAME, 'whever.com'),
        Record(MX, 'whatever.com.', 5),
        Record(MX, 'mx2.whatever.com.', 10),
        Record(MX, 'mx3.whatever.com.', 20),
        Record(NS, 'mx2.whatever.com.'),
        Record(NS, 'mx3.whatever.com.'),
        Record(TXT, "What the fuck did you just fucking say about me, you little bitch?"),
        Record(TXT, "I'll have you know I graduated top of my class in the Navy Seals,"),
        Record(TXT, "and I've been involved in numerous secret raids on Al-Quaeda,"),
        Record(TXT, "and I have over 300 confirmed kills. I am trained in gorilla warfare"),
        Record(TXT, "and I'm the top sniper in the entire US armed forces."),
        Record(TXT, "You are nothing to me but just another target."),
        Record(TXT, "I will wipe you the fuck out with precision the likes of which has"),
        Record(TXT, "never been seen before on this Earth, mark my fucking words."),
        Record(TXT, "You think you can get away with saying that shit to me over the Internet?"),
        Record(TXT, "Think again, fucker. As we speak I am contacting my secret network of spies"),
        Record(TXT, "across the USA and your IP is being traced right now so you better prepare for the storm, maggot."),
        Record(TXT, "The storm that wipes out the pathetic little thing you call your life. You're fucking dead, kid."),
        Record(TXT, "I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that's just with my bare hands."),
        Record(TXT, "Not only am I extensively trained in unarmed combat,"),
        Record(TXT, "but I have access to the entire arsenal of the United States Marine Corps"),
        Record(TXT, "and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit."),
        Record(TXT, "If only you could have known what unholy retribution your little 'clever' comment was about to bring down upon you,"),
        Record(TXT, "maybe you would have held your fucking tongue."),
        Record(TXT, "But you couldn't, you didn't, and now you're paying the price, you goddamn idiot."),
        Record(TXT, "I will shit fury all over you and you will drown in it. You're fucking dead, kiddo."),
        Record(SOA, 'ns1.example.com', 'dns.example.com'),
    ],
    'nsa.gov': [
        Record(A, '1.3.3.7'),
        Record(CNAME, 'whever.com'),
        Record(MX, 'whatever.com.', 5),
        Record(MX, 'mx2.whatever.com.', 10),
        Record(MX, 'mx3.whatever.com.', 20),
        Record(NS, 'mx2.whatever.com.'),
        Record(NS, 'mx3.whatever.com.'),
        Record(TXT, "Hey what's up youtube this is nextgenhacker101 and today I'll be teaching you"),
        Record(TXT, "how to view other computer's ip addresses, and um, really uh view em, and just"),
        Record(TXT, "see how they work and um, today I'm going to be teaching you how to do that."),
        Record(TXT, "Alright you guys um a few things first the cool thing about this ip viewer is"),
        Record(TXT, "is you can see what um what their connection speed is and you can see uh what"),
        Record(TXT, "site they're on alright so i mean it's really cool and um I think you guys "),
        Record(TXT, "might like this. Ok this is my precise instructions I will also post this in"),
        Record(TXT, "my description and remember to also you guys subscribe to my videos, please"),
        Record(TXT, "subscribe. Alright to view their ips there's no downloads no installments and"),
        Record(TXT, "no websites, all you do is you open up oh and you must have internet connection"),
        Record(TXT, "to uh view other people's ips you can't do it without having an internet connection."),
        Record(TXT, "I have a solid, good connection."),
        Record(TXT, "Alright so what you wanna do is you wanna open run cmd of course and this thing"),
        Record(TXT, "will pop up, and if anyone's familiar with cmd they'll know this alright what"),
        Record(TXT, "you do is you type in tracert and then space alright now this is the cool thing,"),
        Record(TXT, "tracert and then space, so now what you wanna do is you wanna type the site you"),
        Record(TXT, "uh wanna view so you wanna go http semicolon slash slash, well not semicolon,"),
        Record(TXT, "the little dot dot and then the website so lets just say google so lets just say"),
        Record(TXT, "we wanna see how many ips are looking at google right now, and like at this exact"),
        Record(TXT, "moment we're going to find how many people are looking at google, what their ips"),
        Record(TXT, "are, and what their connection speed is."),
        Record(SOA, 'ns1.example.com', 'dns.example.com'),
    ],
    'gucci.gov': [
        Record(A, '6.6.6.6'),
        Record(CNAME, 'zone6.zone'),
        Record(MX, 'mx1.zone6.zone.', 5),
        Record(MX, 'mx2.zone6.zone.', 10),
        Record(MX, 'mx3.zone6.zone.', 20),
        Record(NS, 'ns1.zone6.zone.'),
        Record(NS, 'ns2.zone6.zone.'),
        Record(TXT, "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/*,*(#%%%%%%&&&&%%&/**(/,,,*&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"),
        Record(TXT, "@@@@@@@@@@@@@@@@@@@@@@@@@@@@#.,////(#%%%%&&*..,,,,,,*#%*,,/@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"),
        Record(TXT, "@@@@@@@@@@@@@@@@@@@@&&&@@@@@,,/**///(####(,....,,.....,,(#&&,/@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"),
        Record(TXT, "@@@@@@@@@@@@@@@@@@@%%%#@@@@@./**/(###((/*.  ....   .,***.,*/.##*%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"),
        Record(TXT, "@@@@@@@@@@@@@@/*/(#%#(@@@@,*,*//(//**.. . ........*//. /(((,,.,,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"),
        Record(TXT, "@@@@@@@@@@@@@/,,##((##%/@@@@#**,*..     *# ,,,,,,*/...,,*////((,//(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"),
        Record(TXT, "@@@@@@@@@@@@**(/*,,,(*//*@@@@*.      .,,,#&%/..,*/**/((/////*/(/###@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"),
        Record(TXT, "@@@@@@@@@@@*(/*,..,**/,.*(@@@. .   .    *#&@@%&%(**////////***///(/@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"),
        Record(TXT, "@@@@@@@@@@/*,.*(((///,,..,@@@ .    . .. */*/*,, ..#%#((//*****,*/@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"),
        Record(TXT, "@@@@@@@@@//(((#(**,,*/(.,/*@@#*..   .. .*,,,....,(#%###(/**,,,,,,/@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"),
        Record(TXT, "@@@@@@@@((///*,,,,.,,..,(((*@@/.,,,...,,..  ..,((/,,.,*****,,,,,.,%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"),
        Record(TXT, "@@@@@@@@/,,,***,, .  ...(((/@@@%..  .,,**...*,,,..,%%##**,,,,,...,*/@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"),
        Record(TXT, "&&@@@@@@@.,,,,*/*,,. ,..////%@@@@@....,,*,,... *##*,,,.....,,.....,*/@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"),
        Record(TXT, "&&@@@@@@@@..,,,,***/,##///**,@@@@@@.....,... /,,,,........,........,*/@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"),
        Record(TXT, "&&&&@@@@@@&.,,,,**/*.//**/*,.@@@@@@@,......,,...........,,,...    ..,,*@@@@@@@(,.**#@@@@@@@@@@@@@@@"),
        Record(TXT, "&&&&&&&&@&&/..,,*//(/#(/*,,./@@@@@@@@*......................      ....,/#####%%(,,,,,,,,******/////"),
        Record(TXT, "&&&&&&&&&&&&,..,,,,(%%%%##..@@@@@@@@@@%..................        ......,*/(((/.....,,.,,,,*,****,**"),
        Record(TXT, "&&&&&&&&&&&&&,....*,%%%%%%(@@@@@@@@@@@@@*.............            ......,*/* ....,,,,,,,,,,**,,,,,,"),
        Record(TXT, "&&&&&&&&&&&&&,,,...(,*@@/%@%@@@@@@@@@@@@@@@%.                     .......,  .. ..,,,,,.,,,,...,,,,,"),
        Record(TXT, "&&&&&&&&&&&&/*,,,,..,##/(&&/#@@@@@@@@@@@@@@%(...                 ...   .     .......,,,,...,,,,,,,,"),
        Record(TXT, "&&&&&&&&&&&(*,***,,/#(%(#%(%#&&&&&&@@@@@@@...                              . . ..,,,......,,,,,,,,."),
        Record(TXT, "&&&&&&&&&,(.******,. ..##%%%/&&&&&&&&&&,,,,..                                ,,,...   ...,..,.,.,.."),
        Record(TXT, "&&&&&&(..(,,*****,.   ,//**,*&&&&&&&%*,,... .                             ......     .............."),
        Record(TXT, "&&&&&&& .(#....         ,/*,#&&&/,,,,...                               .            ..............."),
        Record(TXT, "&&&&&&&.//%...         (%((/((((/,,....                                           .............. .."),
        Record(TXT, "&&&&&&&,((&.....     ,*(##(#(#(((#....                                              ....... ...   ."),
        Record(TXT, "&&&&&&,../%....      .##/(#((((#(*(.                                                               "),
        Record(TXT, "&&&&&&...*(..        *(#.(##((//(/,((                                                              "),
        Record(TXT, "&&&%.,.  (/(         *(#.#(((//*.** ,                                                              "),
        Record(TXT, "&&&..  .../(         ,#(,,,*,,,,***                                                                "),
        Record(TXT, "&&&...... /(*        ,*, ,/(*/. .(#/                                                               "),
        Record(TXT, "&&..      ,*/              ,((/  /(&                                                               "),
        Record(TXT, "&&....   . ***          .  /%#%, /##(*#*                                                           "),
        Record(TXT, "@,... ..   ,/(/           ./%#((..*,*                                                              "),
        Record(TXT, ".. . .   .. (#*. ..        .***.     .                                                             "),
        Record(SOA, 'ns1.zone6.zone', 'dns.zone6.zone'),
    ]
}

class Resolver:
    def __init__(self):
        self.zones = {DNSLabel(k): v for k, v in ZONES.items()}

    def resolve(self, request, handler):
        reply = request.reply()
        zone = self.zones.get(request.q.qname)
        if zone is not None:
            for zone_records in zone:
                rr = zone_records.try_rr(request.q)
                rr and reply.add_answer(rr)
        else:
            # no direct zone so look for an SOA record for a higher level zone
            for zone_label, zone_records in self.zones.items():
                if request.q.qname.matchSuffix(zone_label):
                    try:
                        soa_record = next(r for r in zone_records if r.is_soa)
                    except StopIteration:
                        continue
                    else:
                        reply.add_answer(soa_record.as_rr(zone_label))
                        break
        return reply
    # will want to put refresh somewhere into resolve, with random func

resolver = Resolver()
servers = [
    DNSServer(resolver, port=5053, address='localhost', tcp=True),
    DNSServer(resolver, port=5053, address='localhost', tcp=False),
]

if __name__ == '__main__':
    for s in servers:
        s.start_thread()

    try:
        while 1:
            sleep(0.1)
    except KeyboardInterrupt:
        pass
    finally:
        for s in servers:
            s.stop()
