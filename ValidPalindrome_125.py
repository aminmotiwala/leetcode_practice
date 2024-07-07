class SolutionValidPalindrome(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        shrunkInput = self.shrinkString(s)
        start = 0
        end = len(shrunkInput) - 1

        while start <= end:
            if shrunkInput[start] != shrunkInput[end]:
                return False

            start = start + 1
            end = end - 1

        return True


    def shrinkString(self, s):
        finalStrin = ""
        for i in s:
            if i.isalnum():
                finalStrin += i.lower()


        print(finalStrin)
        return finalStrin

    def isPalindromeOptimized(self, s):
        """
        :type s: str
        :rtype: bool
        """

        start = 0
        end = len(s) - 1

        while start <= end:
            while start <= end and not s[start].isalnum():
                start = start + 1

            while start <= end and not s[end].isalnum():
                end = end - 1

            if start <= end and s[start].lower() != s[end].lower():
                return False

            start = start + 1
            end = end - 1

        return True


