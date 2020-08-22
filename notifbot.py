import praw

# reddit api login
reddit = praw.Reddit(
    client_id='yGte15xbd64NdA',
    client_secret='y1sA6T8yp2hVOx-_l3j0oVGtgcw',
    username='apolitebot',
    password='HelloHello123',
    user_agent='Notif')

items = ['tofu', 'tangerine', 'gmk', 'peaches', 'kbd']
subreddits = reddit.subreddit('mechmarket')

onSale = []
for submission in subreddits.stream.submissions():
    for i in range(len(submission.title)):
        if submission.title[i: i+3] == "[H]":
            for j in range(i, len(submission.title)):
                if submission.title[j: j+3] == '[W]':
                    onSale += [[submission.title[i+3: j].lower(), submission]]
                    for item in items:
                        if item in onSale[-1][0]:
                            print(submission.url, item)
                            break
                    