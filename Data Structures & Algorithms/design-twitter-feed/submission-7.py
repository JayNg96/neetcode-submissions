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
        
        for user, tweet in self.users_tweet.items():
            if user in users_follow_map:
                for ts, tid in tweet:
                    heapq.heappush(heap, (-ts, tid))


        #heapq.heapify(heap) 
        tweet_li = []
        while heap:
            tweet_li.append(heapq.heappop(heap)[1])

        return tweet_li[:10]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.users_follower[followerId].add( followeeId )

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.users_follower[followerId].discard(followeeId)
    