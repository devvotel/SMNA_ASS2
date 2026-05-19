from atproto import Client

client = Client()
client.login("devvotel.bsky.social", "hwd3-k373-bh7x-hu3o")

keywords = ["twitter", "elon", "leaving twitter", "twitter refugee", "miss twitter", "deleted twitter", "quit twitter"]
counts = {}
for kw in keywords:
    search_res = client.app.bsky.feed.search_posts({"q":kw, "limit":100})
    counts[kw]= len(search_res.posts)

print(counts)