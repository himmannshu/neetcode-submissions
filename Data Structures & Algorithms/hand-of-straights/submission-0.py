class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0 or len(hand) < groupSize:
            return False
        hand = sorted(hand)

        d = defaultdict(int)

        for h in hand:
            d[h] += 1
        
        for h in hand:
            if h in d:
                hi = h + groupSize
                for i in range(h, hi):
                    if i not in d:
                        return False
                    d[i] -= 1
                    if d[i] <= 0:
                        d.pop(i)
        
        return len(d) == 0