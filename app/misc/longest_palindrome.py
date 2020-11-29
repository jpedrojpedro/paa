from utils.measures import log_time


def longest_palindrome(s):
    ws = len(s)
    if ws <= 1:
        return s
    while ws > 0:
        for i in range(len(s)):
            j = i + ws
            if j > len(s):
                break
            ss = s[i:j]
            rs = [c for c in ss]
            rs.reverse()
            rs = ''.join(rs)
            if ss == rs:
                return ss
        ws -= 1
    return ''


if __name__ == '__main__':
    bar = "abbacdhannah"
    t, res = log_time(longest_palindrome, bar)
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
