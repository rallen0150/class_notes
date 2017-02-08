# WORKS!!!!!!
def longest_common_prefix(strings):
    prefix = list(strings[0])
    a = prefix
    for i in strings[1:]:
        newpre = []
        word2 = list(i)
        for x in range(len(word2)):
            if prefix[x]==word2[x]:
                newpre.append(prefix[x])
            else:
                prefix = newpre[:]
                break
    return ''.join(prefix)

answer = longest_common_prefix(['catamaran', 'cat', 'car'])
print(answer)

# def commonprefix(m):
#     "Given a list of pathnames, returns the longest common leading component"
#     if not m: return ''
#     s1 = min(m)
#     s2 = max(m)
#     for i, c in enumerate(s1):
#         if c != s2[i]:
#             return s1[:i]
#     return s1
#
# answer = commonprefix(['catamaran', 'cat', 'car', 'carry', 'catty'])
# print(answer)
