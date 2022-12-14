def find_longest_word(words_list):
    word_len=[]
    for n in words_list:
        word_len.append((len(n),n))
    word_len.sort()
    return word_len[-1][0],word_len[-1][1]
result=find_longest_word(["php","python","datastructure"])
print("\n longest word:",result[1])
print("length of the longest word:",result[0])