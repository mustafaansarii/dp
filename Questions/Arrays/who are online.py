class Solution:
    def findMinMembers(self, a, b):
        n = len(a)
        pos_a = {member: index for index, member in enumerate(a)}
        pos_b = {member: index for index, member in enumerate(b)}

        online_members = set()

        min_seen = float("inf")

        for member in reversed(a):
            if pos_b[member] > min_seen:  
                online_members.add(member)
            min_seen = min(min_seen, pos_b[member])

        return len(online_members)


# Test cases
a1 = [1, 4, 2, 5, 3]
b1 = [4, 5, 1, 2, 3]
print(Solution().findMinMembers(a1, b1)) # Output: 2

a=[5, 6, 4, 3, 1, 2]
b=[5, 1 ,3, 6, 4, 2]
print(Solution().findMinMembers(a,b))  # Output: 3
