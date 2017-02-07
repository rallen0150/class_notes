# # Doesn't work
# def longest_common_prefix(strings):
#     prefix = strings[0].split()
#     for i in strings[1:]:
#         newpre = []
#         word2 = i
#         for x in range(len(prefix)):
#             if prefix[x]==word2[x]:
#                 newpre.append(prefix[x])
#             else:
#                 prefix = newpre[:]
#                 break
#     return prefix
#
# answer = longest_common_prefix(['catamaran', 'cat', 'car'])
# print(answer)

def commonprefix(m):
    "Given a list of pathnames, returns the longest common leading component"
    if not m: return ''
    s1 = min(m)
    s2 = max(m)
    for i, c in enumerate(s1):
        if c != s2[i]:
            return s1[:i]
    return s1

answer = commonprefix(['catamaran', 'cat', 'car', 'carry', 'catty'])
print(answer)
