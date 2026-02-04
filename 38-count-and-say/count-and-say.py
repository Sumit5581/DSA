class Solution:
    def countAndSay(self, n: int) -> str:
        result = "1"

        for _ in range(1, n):
            curr = ""
            count = 1

            for i in range(1, len(result)):
                if result[i] == result[i - 1]:
                    count += 1
                else:
                    curr += str(count) + result[i - 1]
                    count = 1

            curr += str(count) + result[-1]
            result = curr

        return result
