'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):

    # TBC
    # print(word)

    def cth(w, rest):
        count = 0

        if w == "th":
            count += 1

        if len(rest) >= 2:
            count += cth(rest[0:2], rest[1:])

        return count

    return cth(word, word)


print(count_th("th"))
print()
print(count_th("thabcth"))
