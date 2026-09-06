class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        right = 0
        max_length = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            max_frequency = max(count.values())

            window_length = right - left + 1
            replacements = window_length - max_frequency
            while replacements > k:
                count[s[left]] -= 1
                left += 1

                window_length = right - left + 1
                max_frequency = max(count.values())
                replacements = window_length - max_frequency
            max_length = max(window_length, max_length)
        return max_length
        