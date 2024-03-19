from app.io.input import coninput, readfile, pd_readfile
from app.io.output import conoutput, writefile, pd_writefile

def main():
    print("a")
    coninput()
    a = readfile('text.txt')
    b = pd_readfile('text.txt')
    conoutput('test')
    writefile('text.txt', 'abcdefg')
    pd_writefile('test.txt', '{}')
main()