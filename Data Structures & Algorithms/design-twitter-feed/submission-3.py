from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.time = 0

        # who does this user follow?
        self.user_to_followees = defaultdict(set)
        
        self.user_to_tweets = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        tweet = (self.time, tweetId)
        self.user_to_tweets[userId].append(tweet)
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # edge case: user should "follow" themselves too 
        self.user_to_followees[userId].add(userId)

        # create heap
        # The heap contains the most recent not-yet-used tweet from each relevant user.
        heap = []
        heapq.heapify_max(heap)

        for followee in self.user_to_followees[userId]:
            tweets = self.user_to_tweets[followee]
            if tweets:
                index = len(tweets) - 1
                latest_tweet = tweets[-1]
                heap_item = (latest_tweet[0], latest_tweet[1], followee, index) # (time, tweetId, userId, index)
                heapq.heappush_max(heap, heap_item)

        feed = []
        while heap and len(feed) < 10:
            heap_item = heapq.heappop_max(heap)
            feed.append(heap_item[1])

            tweets = self.user_to_tweets[heap_item[2]]
            next_index = heap_item[3] - 1
            if next_index >= 0:
                next_tweet = tweets[next_index]
                heap_item = (next_tweet[0], next_tweet[1], heap_item[2], next_index)
                heapq.heappush_max(heap, heap_item)

        return feed


    def follow(self, followerId: int, followeeId: int) -> None:
        # add following relationship
        self.user_to_followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # remove following relationship
        self.user_to_followees[followerId].discard(followeeId)
