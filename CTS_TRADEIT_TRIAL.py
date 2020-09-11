import bs4 as bs
import urllib.request


def main():
    
    source = urllib.request.urlopen("https://www.cts-tradeit.cz/kariera/").read()
    soup_source = bs.BeautifulSoup(source,'lxml')
    print(soup_source.title)

    
if __name__ == "__main__":
    main()
