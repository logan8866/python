from slave import HTMLDownloader,Parse

def test_downloader():
    downloader = HTMLDownloader()
    content = downloader.download("http://jandan.net/ooxx")
    parse = Parse()
    urls,data = parse.parse(content)
    print(urls,data)

if __name__ == "__main__":
    test_downloader()
