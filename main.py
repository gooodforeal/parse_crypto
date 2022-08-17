from funcs import *


# Const
url = "https://coinmarketcap.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
}

'''  MAIN   '''
def main():
    get_html(url=url)
    parse()


if __name__ == '__main__':
    main()