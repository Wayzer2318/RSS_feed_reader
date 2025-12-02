import feedparser


def read_rss_feed(feed_url):
    # parse the url
    myfeed = feedparser.parse(feed_url)

    # print metadata
    print(f"feed title: {myfeed.feed.title}")
    print(f"feed link : {myfeed.feed.link}\n")

    # print entries
    for entry in myfeed.entries[:5]:
        print(f"title : {entry.title}")
        print(f"link : {entry.link}")
        print(f" description : {entry.description}\n")


feed_url = input("please enter your feed url : ")

read_rss_feed(feed_url)
