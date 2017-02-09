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

#############################
# #Added for fun
word_list = []
choice = ""

while choice != 'e':
    choice = input('Would you like to (a)dd a word or (e)nd your list and view the Longest Common Prefix?\n>').lower()
    if choice == 'a':
        word = input('Enter a New Word:\n>').lower()
        word_list.append(word)
        print("Your word list is: {}\n".format(word_list))
    elif choice == 'e':
        break
    else:
        print("Invalid Choice!")

new_answer = longest_common_prefix(word_list)
print(new_answer)




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
