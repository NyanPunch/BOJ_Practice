# 문제: 단어 공부

def count(s):
    s = s.upper()
    s = list(s)
    s_set = list(set(s))
    s_count = []
    for i in s_set:
        s_count.append(s.count(i))
    if s_count.count(max(s_count)) > 1:
        return '?'
    else:
        return s_set[s_count.index(max(s_count))]

def main():
    s = input()
    print(count(s))

if __name__ == "__main__":
    main()