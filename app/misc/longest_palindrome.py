from utils.measures import log_time


def is_palindrome(s):
    if len(s) == 0 or len(s) == 1:
        return True
    if s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    return False


def longest_palindrome(s):
    ws = len(s)
    while ws > 0:
        for i in range(len(s)):
            j = i + ws
            if j > len(s):
                break
            ss = s[i:j]
            if is_palindrome(ss):
                return ss
        ws -= 1
    return ''


if __name__ == '__main__':
    foo = "abbacdhannah"
    t, res = log_time(longest_palindrome, foo)
    print("Solution: {} | {} s".format(res, t))
    foo = "ibvjkmpyzsifuxcabqqpahjdeuzaybqsrsmbfplxycsafogotliyvhxjtkrbzqxlyfwujzhkdafhebvsdhkkdbhlhmaoxmbkqiwiusngkb" \
          "dhlvxdyvnjrzvxmukvdfobzlmvnbnilnsyrgoygfdzjlymhprcpxsnxpcafctikxxybcusgjwmfklkffehbvlhvxfiddznwumxosomfbgx" \
          "oruoqrhezgsgidgcfzbtdftjxeahriirqgxbhicoxavquhbkaomrroghdnfkknyigsluqebaqrtcwgmlnvmxoagisdmsokeznjsnwpxygj" \
          "jptvyjjkbmkxvlivinmpnpxgmmorkasebngirckqcawgevljplkkgextudqaodwqmfljljhrujoerycoojwwgtklypicgkyaboqjfivbeq" \
          "dlonxeidgxsyzugkntoevwfuxovazcyayvwbcqswzhytlmtmrtwpikgacnpkbwgfmpavzyjoxughwhvlsxsgttbcyrlkaarngeoaldsdtj" \
          "ncivhcfsaohmdhgbwkuemcembmlwbwquxfaiukoqvzmgoeppieztdacvwngbkcxknbytvztodbfnjhbtwpjlzuajnlzfmmujhcggpdcwdq" \
          "uutdiubgcvnxvgspmfumeqrofewynizvynavjzkbpkuxxvkjujectdyfwygnfsukvzflcuxxzvxzravzznpxttduajhbsyiywpqunnarab" \
          "croljwcbdydagachbobkcvudkoddldaucwruobfylfhyvjuynjrosxczgjwudpxaqwnboxgxybnngxxhibesiaxkicinikzzmonftqkcud" \
          "lzfzutplbycejmkpxcygsafzkgudy"
    t, res = log_time(longest_palindrome, foo)
    print("Solution: {} | {} s".format(res, t))
    foo = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" \
          "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" \
          "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" \
          "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" \
          "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaa" \
          "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" \
          "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" \
          "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" \
          "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" \
          "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    t, res = log_time(longest_palindrome, foo)
    print("Solution: {} | {} s".format(res, t))
