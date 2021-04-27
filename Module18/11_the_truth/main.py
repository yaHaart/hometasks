# все равно ниасилил. Вроде 1 задачу можно пропустить для зачета домашки.
text = 'vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju/jnqm fTjnqm tj scfuuf ibou fy/dpnqm yDpnqmf jt ' \
       'cfuufs boui dbufe/dpnqmj uGmb tj fuufsc ouib oftufe/ bstfTq jt uufscf uibo otf/ef uzSfbebcjmj vout/dp djbmTqf ' \
       'dbtft (ubsfo djbmtqf hifopv up csfbl ifu t/svmf ipvhiBmu zqsbdujdbmju fbutc uz/qvsj Fsspst tipvme wfsof qbtt ' \
       'foumz/tjm omfttV mjdjumzfyq odfe/tjmf Jo fui dfgb pg hvjuz-bncj gvtfsf fui ubujpoufnq up ftt/hv Uifsf vmetip ' \
       'fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/ Bmuipvhi uibu bzx bzn puo cf wjpvtpc bu jstug ttvomf ' \
       'sfzpv( i/Evud xOp tj scfuuf ibou /ofwfs uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh x/op gJ ifu ' \
       'nfoubujpojnqmf tj eibs pu mbjo-fyq tju( b bec /jefb Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf b ' \
       'hppe jefb/ bnftqbdftO bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip '
alphabet_lowercase = 'abcdefghijklmnopqrstuvwxyz'
alphabet_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
splited_text = text.split('/')
temp_word = ''
temp_list = []
shift = 0
move = 3

for line in splited_text:
    shift += 1
    for i in line:
        if i in alphabet_lowercase:
            temp_word += alphabet_lowercase[(alphabet_lowercase.index(i) - shift) % 26]
        elif i in alphabet_uppercase:
            temp_word += alphabet_uppercase[(alphabet_uppercase.index(i) - shift) % 26]
        elif i != ' ':
            temp_word += i
        else:
            temp_list.append(temp_word)
            temp_word = ''

    for word in temp_list:
        for j in range(len(word)):
            if len(word) >= move:
                print(word[j - move])
            else:
                print(move // len(word))
                # print(word[j - (move // len(word))], end='')
        print(' ', end='')
    move += 1
    temp_list.clear()
    shift -= 1


# закодированный текст:
# Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. Complex is better than complicated. Flat is better than nested. Sparse is better than dense. Readability counts. Special cases aren't special enough to break the rules. Although practicality beats purity. Errors should never pass silently. Unless explicitly silenced. In the face of ambiguity, refuse the temptation to guess. There should be one-- and preferably only one --obvious way to do it. Although that way may not be obvious at first unless you're Dutch. Now is better than never. Although never is often better than *right* now. If the implementation is hard to explain, it's a bad idea. If the implementation is easy to explain, it may be a good idea. Namespaces are one honking great idea -- let's do more of those!