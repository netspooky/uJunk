z = "█";      A = z*2;       c = "\x1b[38;5;"; b = c+"19m";
D = A+A;      e = "\x1b[0m"; f = c+"120m";     g = c+"77m";
h = c+"240m"; i = c+"34m";   j = c+"58m";      k = c+"208m";
l = c+"220m"; m = c+"237m";  q = c+"124m";     r = c+"161m";
S = "  ";     t = c+"88m";   U = S + S;        y = c+"214m";
N = [       66,19,17,  15,15,13,  11,11,    11,13,13,  13,15,17,
               17,     19,17,     15,  15,     15,     15,   17,
               11,     7,5,3,3,   3,   31,     31,      31,66]
O = ["",U+b,S+k+A+e+U+b+z*10+e+U+b,S+k+A+e+S+b+z*12+e+S+l+A+e+U+b,S+k+A
     +S+b+z*12+U+b,S+k+A      +S+b+z*12+e+S+l+A+S+b,S+k+D+e+S+b+z*12+S+
     l+A+S+b,S+k+A+e+S         +b+A*7+U+b     ,S+k+A+S+b+A*5+U+l+A+e+S+
     b,U+b+A*4+S+l+D       +e+S+b,S+k+A         +S+b+A*3+e+S+l+A+e+S+b+
     A*6+U+b,S+k+A+S       +b+D+e+S+l+A     +e+S+b+A+e+S*6+h+A+m+A+S+b,
     U+b+D+S+l+A+U       +r+A+U+r+D+q       +A+S*3+b,S+b+A*3+S+r+A+q+A+
     S+r+z*12+q+         A+S+b,S+b+D+       S*4+r+z*16+q+A+S+b,U+q+A+S+
     D+U+r+A*5+U       +q+A+S+b,S+r+A     *5+S+e+A+f+A+S+q+A+r+D+S+h+A+
     m+A+U+b,S+e       +A+h+A+r+D         +h+A+S+e+A+f+A+g+D+S+q+A+r+A+
     S+m+D+S+q+A+S     +b,S+g+A         +r+A*4+S+f+A+g+D+i+A+e+S+q+A+r+
     D+U+q+D+U+b,S       +g+A+h      +A+r+D+h+A+S     +g+D+i+D+U+S+r+A*
     3+q+D+U+b,S+i       +A+S                           *4+q+A+S+i+D+U+
     r+D+S+r+D+q+D+U     +b,S                           +y+A+S+y+D+S+A+
     S*4+j+A+r+A+S*3+q   +D+S+b                         ,U+S+t+A+S+y+A+
     S+y+D+S+A+U+j+A+S   *6+q                             +A+S+b,U+r+A*
     3+t+D+S*7+j+A+U+r+A                                    +q+A+S*4+b,
     h+S+D+S+q+D+t+D+S                                      +b+A+e+S*4+
     m+A+S+r+A*3+q+A                                          +S+r+A+q+
     A+S+b,h+S+A+m+D                                            +S+q+A*
     3+S+b+A+e+U+t+A                                            +S+m+A+
     S+h+A+S+r+A+q+A                                            +S+r+D+
     q+D+S+b,S+m+A+S*6                                        +b+A+m+S+
     D+S+t+A+S+h                                              +D+S+q+A+
     r+A+S+q                                                +A*4+S+b,U+
     b+z*14                   +S                            *6+h+A+m+A+
     S+r+                    A+                                 S+q+A+U
     +A+S                  +h                                   +A+e+S+
     b,h+     S+A+m+A+U+b+A+h                                     +S+D+
     S*4+b,e+S+h+A+S+b+A*3+e+S*3+b,e           +U                 +b,""]
P = [0,41,25,23,27,27,27,29,29,31,17       ,15,15       ,15,13,11,11,9,7
     ,7,7,9,9,11,11,9,9,7,7,15,29,0]
def p(n,o,p):
     print(b,z*n,o,z*p,e)
for v in range(0,len(N)):
     p(N[v],O[v],P[v])
