class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        

        data = sorted(zip(timestamp,username,website))
        
        track = defaultdict(list)

        for time, user, site in data:
            track[user].append(site)
        
        patterns = defaultdict(set)
        for user, sites in track.items():
            comb_sites = set(combinations(sites, 3) )
            for combo in comb_sites:
                patterns[combo].add(user)
        max_len=0
        max_seq = []
        for key, value in patterns.items():
            if len(value)>max_len or (len(value) == max_len and key < max_seq):
                max_len = len(value)
                max_seq = key
        return max_seq