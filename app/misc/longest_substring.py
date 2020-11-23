from utils.measures import log_time


def length_of_longest_substring(s: str) -> int:
    longest = 0
    chars = set()
    for i in range(len(s)):
        for c in s[i:]:
            if c not in chars:
                chars.add(c)
                continue
            longest = max(longest, len(chars))
            chars = set()
            break
    longest = max(longest, len(chars))
    return longest


if __name__ == '__main__':
    foo = "abcabcbb"
    t, res = log_time(length_of_longest_substring, foo)
    print("Solution: {} | {} s".format(res, t))
