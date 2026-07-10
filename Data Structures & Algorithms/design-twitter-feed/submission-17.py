from typing import List
from collections import deque, defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.users_tweet = defaultdict(deque)
        self.users_follower = defaultdict(set)
        self.timestamp_counter = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp_counter += 1
        self.users_tweet[userId].append( (self.timestamp_counter, tweetId) )

    def getNewsFeed(self, userId: int) -> List[int]:
        users_follow_map = self.users_follower[userId].copy()
        users_follow_map.add(userId)
        heap = []
        
        for followeeId in users_follow_map:
            for timestamp, tweetId in self.users_tweet.get(followeeId, []):
                heapq.heappush(heap, (-timestamp, tweetId))

        tweet_li = []
        while heap:
            tweet_li.append(heapq.heappop(heap)[1])

        return tweet_li[:10]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.users_follower[followerId].add( followeeId )

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.users_follower[followerId].discard(followeeId)