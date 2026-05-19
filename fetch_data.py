from atproto import Client

client = Client()
client.login("devvotel.bsky.social", "hwd3-k373-bh7x-hu3o")

keywords = ["twitter", "elon", "twitter refugee", "bluesky vs twitter", "twitter is dead", "quit twitter", "miss twitter"]
counts = {}
#for kw in keywords:
#    search_res = client.app.bsky.feed.search_posts({"q":kw, "limit":100})
#    counts[kw]= len(search_res.posts)
#
#print(counts)

cursor = None
for kw in keywords:
    count = 0
    while count <= 2000:
        if cursor:
            queryParams = {"q":kw, "limit":100, "lang":"en", "cursor":cursor}
        else:
            queryParams = {"q":kw, "limit":100, "lang":"en"}
        res = client.app.bsky.feed.search_posts(queryParams)
        count += len(res.posts)
        cursor = res.cursor
        if not cursor:
            break
        