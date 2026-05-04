class Twitter:

    def __init__(self):
        self.user_relations = defaultdict(set)
        self.user_tweets = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:

        if userId not in self.user_relations[userId]:
            self.user_relations[userId].add(userId)

        self.time += 1
        self.user_tweets[userId].append((self.time,tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.user_relations:
            return []

        all_users = self.user_relations[userId]
        tweets = []

        for i in all_users:
            tweets = tweets + self.user_tweets[i]

        tweets = [(-i[0],i[1]) for i in tweets]
        heapq.heapify(tweets)
        
        news_feed = []
        i = 0
        while i<10 and tweets:
            frequency, latest = heapq.heappop(tweets)
            news_feed.append(latest)
            i+=1

        return news_feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_relations[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.user_relations and followeeId in self.user_relations[followerId] and followerId != followeeId: 
            self.user_relations[followerId].remove(followeeId)
