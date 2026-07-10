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
        # Push most recent from each followee
        for followeeId in users_follow_map:
            tweets = self.users_tweet.get(followeeId, [])
            if tweets:
                ts, tid = tweets[-1]  # most recent (last element)
                heapq.heappush(heap, (-ts, tid, followeeId, len(tweets) - 1))

        res = []
        while heap and len(res) < 10:
            neg_ts, tid, followeeId, idx = heapq.heappop(heap)
            res.append(tid)
            # If there's an older tweet, push it
            if idx > 0:
                ts, tid = self.users_tweet[followeeId][idx - 1]
                heapq.heappush(heap, (-ts, tid, followeeId, idx - 1))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.users_follower[followerId].add( followeeId )

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.users_follower[followerId].discard(followeeId)