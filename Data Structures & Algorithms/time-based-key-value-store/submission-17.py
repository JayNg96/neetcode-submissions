class TimeMap:

    def __init__(self):
        self.time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_map:
            self.time_map[key] = ([value], [timestamp])
        else:
            self.time_map[key][0].append(value)
            self.time_map[key][1].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:    

        if key not in self.time_map:
            return ""

        if timestamp < self.time_map[key][1][0]:
            return ""

        for idx, ts in enumerate(self.time_map[key][1]):
            if ts == timestamp:
                return self.time_map[key][0][idx]
            
            if idx != len(self.time_map[key][1]) - 1:
                if self.time_map[key][1][idx] < timestamp and self.time_map[key][1][idx + 1] > timestamp:
                    return self.time_map[key][0][idx]
            else:
                return self.time_map[key][0][-1]