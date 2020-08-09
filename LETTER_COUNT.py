get_word = {}

user_input = input("\nENTER A WORD: ")
for x in user_input:
    count = user_input.count(x)
    count = str(count)
    get_word[x] = count
        
get_word = sorted(get_word.items(), key = lambda x:x[1], reverse = True)
for i in get_word:
    print(i[0], i[1])
