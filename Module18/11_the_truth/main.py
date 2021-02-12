unknown_text = 'vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo ' \
               'jdju/jnqm fTjnqm tj scfuuf ibou fy/dpnqm yDpnqmf jt cfuufs ' \
               'boui dbufe/dpnqmj uGmb tj fuufsc ouib oftufe/ bstfTq jt uufscf ' \
               'uibo otf/ef uzSfbebcjmj vout/dp djbmTqf dbtft (ubsfo djbmtqf ' \
               'hifopv up csfbl ifu t/svmf ipvhiBmu zqsbdujdbmju fbutc uz/qvsj ' \
               'Fsspst tipvme wfsof qbtt foumz/tjm omfttV mjdjumzfyq odfe/tjmf' \
               ' Jo fui dfgb pg hvjuz-bncj gvtfsf fui ubujpoufnq up ftt/hv ' \
               'Uifsf vmetip fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz ' \
               'pu pe ju/ Bmuipvhi uibu bzx bzn puo cf wjpvtpc bu jstug ' \
               'ttvomf sfzpv( i/Evud xOp tj scfuuf ibou /ofwfs uipvhiBm ' \
               'fsofw jt fopgu cfuufs boui iu++sjh x/op gJ ifu nfoubujpojnqmf' \
               ' tj eibs pu mbjo-fyq tju( b bec /jefb Jg fui foubujpojnqmfn ' \
               'jt fbtz up bjo-fyqm ju znb cf b hppe jefb/ bnftqbdftO bsf ' \
               'pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip'

alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
unknown_text.lower()
splited_text = unknown_text.split('/')
print(splited_text)
count = 9
new_line = ''
for line in splited_text:
    count += 1
    for i in range(len(line)):
        if line[i] in alphabet:
           new_line += alphabet[alphabet.index(line[i]) + count]
        else:
            new_line += line[i]

    print(new_line)
    new_line = ''
