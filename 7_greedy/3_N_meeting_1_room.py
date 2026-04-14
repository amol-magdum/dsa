# Class to hold solution logic
class Solution:
    # Function to get all meetings that can be scheduled
    def maxMeetings(self, start, end):
        # Store as ( start, end, index)
        n = len(start)
        meetings = []
        for i in range(n):
            meetings.append((start[i], end[i]))
        # Sort by end time
        meetings.sort(key=lambda x: x[1])
        res = 1
        j = 0
        for i in range(n):
            if meetings[i][0] > meetings[j][1]:
                res += 1
                j = i
        return res

# Main driver code
if __name__ == "__main__":
    start = [1, 3, 0, 5, 8, 5,10]
    end   = [2, 4, 6, 7, 9, 9, 12]

    sol = Solution()
    res = sol.maxMeetings(start, end)
    print(res)