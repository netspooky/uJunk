# 2020-09-20
# Used to generate this https://twitter.com/netspooky/status/1307038708907081728
import time 
import urllib.request

l0 = '8b........d8...............................................................................................................88..88....................................................................................................88.....................................................................................88..88.................................................................................................................................88..88..................................................................................................................................88......................................................................................'
l1 = '.Y8,....,8P................................................................................................................88..""....................................................................................................88.....................................................................................88.."".................................................................................................................................""..88...............................................................................................................,d..........,d.....88......................................................................................'
l2 = '..Y8,..,8P.................................................................................................................88........................................................................................................88.....................................................................................88.........................................................................................................................................88...............................................................................................................88..........88.....88......................................................................................'
l3 = '..."8aa8"..,adPPYba,...88.......88.....,adPPYYba,..8b,dPPYba,...,adPPYba,.....8b,dPPYba,...,adPPYba,..,adPPYYba,...,adPPYb,88..88..8b,dPPYba,....,adPPYb,d8.....8b,dPPYba,....,adPPYba,..,adPPYYba,..8b,dPPYba,...,adPPYba,..........88.....,adPPYYba,..88,dPYba,,adPYba,......8b,dPPYba,...,adPPYba,..,adPPYYba,...,adPPYb,88..88..8b,dPPYba,....,adPPYb,d8.....8b.......d8...,adPPYba,...88.......88..8b,dPPYba,......,adPPYba,..88,dPYba,,adPYba,...,adPPYYba,..88..88..........8b......db......d8...,adPPYba,.....,adPPYYba,..8b,dPPYba,...,adPPYba,.....8b,dPPYba,....,adPPYba,..MM88MMM.....MM88MMM..88,dPPYba,....,adPPYba,.....,adPPYba,..,adPPYYba,..88,dPYba,,adPYba,....,adPPYba,.......'
l4 = '....`88"..a8"....."8a..88.......88....."".....`Y8..88P"..."Y8..a8P,,,,,88.....88P"..."Y8..a8P,,,,,88.."".....`Y8..a8"....`Y88..88..88P"...`"8a..a8"....`Y88.....88P"...."8a..a8"....."".."".....`Y8..88P"...."8a..I8[....""..........88....."".....`Y8..88P"..."88"...."8a.....88P"..."Y8..a8P,,,,,88.."".....`Y8..a8"....`Y88..88..88P"...`"8a..a8"....`Y88.....`8b.....d8"..a8"....."8a..88.......88..88P"..."Y8.....a8P,,,,,88..88P"..."88"...."8a.."".....`Y8..88..88..........`8b....d88b....d8"..a8P,,,,,88....."".....`Y8..88P"..."Y8..a8P,,,,,88.....88P"...`"8a..a8"....."8a...88..........88.....88P"...."8a..a8P,,,,,88.....I8[...."".."".....`Y8..88P"..."88"...."8a..a8P,,,,,88.......'
l5 = '.....88...8b.......d8..88.......88.....,adPPPPP88..88..........8PP""""""".....88..........8PP"""""""..,adPPPPP88..8b.......88..88..88.......88..8b.......88.....88.......d8..8b..........,adPPPPP88..88.......d8...`"Y8ba,...aaa.....88.....,adPPPPP88..88......88......88.....88..........8PP"""""""..,adPPPPP88..8b.......88..88..88.......88..8b.......88......`8b...d8"...8b.......d8..88.......88..88.............8PP"""""""..88......88......88..,adPPPPP88..88..88..aaa......`8b..d8"`8b..d8"...8PP""""""".....,adPPPPP88..88..........8PP""""""".....88.......88..8b.......d8...88..........88.....88.......88..8PP"""""""......`"Y8ba,...,adPPPPP88..88......88......88..8PP""""""".......'
l6 = '.....88..."8a,...,a8".."8a,...,a88.....88,....,88..88.........."8b,...,aa.....88.........."8b,...,aa..88,....,88.."8a,...,d88..88..88.......88.."8a,...,d88.....88b,...,a8".."8a,...,aa..88,....,88..88b,...,a8"..aa....]8I.."88.....88.....88,....,88..88......88......88.....88.........."8b,...,aa..88,....,88.."8a,...,d88..88..88.......88.."8a,...,d88.......`8b,d8"...."8a,...,a8".."8a,...,a88..88............."8b,...,aa..88......88......88..88,....,88..88..88.."88.......`8bd8"..`8bd8"...."8b,...,aa.....88,....,88..88.........."8b,...,aa.....88.......88.."8a,...,a8"...88,.........88,....88.......88.."8b,...,aa.....aa....]8I..88,....,88..88......88......88.."8b,...,aa..888..'
l7 = '.....88....`"YbbdP""....`"YbbdP"Y8.....`"8bbdP"Y8..88...........`"Ybbd8"".....88...........`"Ybbd8""..`"8bbdP"Y8...`"8bbdP"Y8..88..88.......88...`"YbbdP"Y8.....88`YbbdP""....`"Ybbd8""..`"8bbdP"Y8..88`YbbdP""...`"YbbdP""..d8".....88.....`"8bbdP"Y8..88......88......88.....88...........`"Ybbd8""..`"8bbdP"Y8...`"8bbdP"Y8..88..88.......88...`"YbbdP"Y8.........Y88"......`"YbbdP""....`"YbbdP"Y8..88..............`"Ybbd8""..88......88......88..`"8bbdP"Y8..88..88..d8".........YP......YP.......`"Ybbd8"".....`"8bbdP"Y8..88...........`"Ybbd8"".....88.......88...`"YbbdP""...."Y888......."Y888..88.......88...`"Ybbd8"".....`"YbbdP""..`"8bbdP"Y8..88......88......88...`"Ybbd8""..888..'
l8 = '.................................................................................................................................................aa,....,88.....88...................................88.....................8"....................................................................................................................aa,....,88.........d8"..................................................................................................8".......................................................................................................................................................................................................................'
l9 = '.................................................................................................................................................."Y8bbdP"......88...................................88............................................................................................................................................"Y8bbdP".........d8"............................................................................................................................................................................................................................................................................................................................'

x = 0  # The starting point in the scroll
y = 16 # End of screen

url = 'http://127.0.0.1:8080/index.php?page='
print("\033[2J")
for i in range(len(l0)):
  o0 = l0[x:y]
  o1 = l1[x:y]
  o2 = l2[x:y]
  o3 = l3[x:y]
  o4 = l4[x:y]
  o5 = l5[x:y]
  o6 = l6[x:y]
  o7 = l7[x:y]
  o8 = l8[x:y]
  o9 = l9[x:y]
  out = o0 + o1 + o2 + o3 + o4 + o5 + o6 + o7 + o8 + o9
  print(out)
  f = urllib.request.urlopen(url+out)
  x = x+1 # Increment start
  y = y+1 # Increment end
  if y == len(l0):
    break
