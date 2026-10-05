class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        
        can_store = []

        for i, num in enumerate(capacity):
            if num >= itemSize:
                can_store.append(num)
            
        if can_store:
            return capacity.index(min(can_store))
        else:
            return -1