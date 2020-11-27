from utils.measures import log_time


def longest_palindrome(s):
    if len(s) == 1:
        return s
    ls = [c for c in s]
    ls.reverse()
    rls = ''.join(ls)
    if s == rls:
        return s
    longest_palindrome(s[:-1])


if __name__ == '__main__':
    aux = 'abbaunfhannah'
    t, res = log_time(longest_palindrome, aux)
    print("Solution: {} | {} s".format(res, t))
