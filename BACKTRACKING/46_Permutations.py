class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []

        def backtrack(path, remaining):
            # Base case: if no more elements are left to permute
            if not remaining:
                res.append(path[:])
                return

            # Recursive case: iterate over the remaining elements
            for i in range(len(remaining)):
                # Choose the element at index i
                n = remaining.pop(i)
                path.append(n)

                # Explore further with this choice
                backtrack(path, remaining)

                # Backtrack: undo the choice
                path.pop()
                remaining.insert(i, n)

        backtrack([], nums)
        return res
