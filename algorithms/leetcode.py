class Solution:
    def smallestNumber(self, n: int) -> int:

        c = 0
        smallest = 0
        while c < 6:
            smallest += pow(2, c)
            print(smallest)
            c += 1


if __name__ == "__main__":
    s = Solution().smallestNumber(5)