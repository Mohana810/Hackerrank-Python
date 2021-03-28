def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        # slice string upto k characters
        word = string[i:i + k]
        seen = set()
        for i in word:
            # only print if we haven't already seen this character
            if i not in seen:
                print(i, end="")
                seen.add(i)
        print()

string, k = input(), int(input())
merge_the_tools(string, k)
