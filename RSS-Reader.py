import feedparser


def read_rss_feed(feed_url):
    for url in feed_url:
        print(f"\n{'=' * 50}\nFetching: {url}\n{'=' * 50}\n")
        # parse the url
        myfeed = feedparser.parse(url)

        # print metadata
        print(f"feed title: {myfeed.feed.title}")
        print(f"feed link : {myfeed.feed.link}\n")

        # print entries
        for entry in myfeed.entries[:5]:
            print(f"title : {entry.title}")
            print(f"link : {entry.link}")
            print(f" description : {entry.description}\n")


def get_user_feed():
    feeds = []
    while True:
        url = input("> ").strip()
        if not url:
            break
        feeds.append(url)
    return feeds


print(" plz enter ur urls and if press 2 times enter")
# get user feeds
feed_url = get_user_feed()


if feed_url:
    read_rss_feed(feed_url)
else:
    print(" no RSS feed url provided.")
