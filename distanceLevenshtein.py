def canonize(source):
        stop_symbols = '.,!?:;-\n\r()'

        stop_words = ('ПАО', 'ОАО', 'ЗАО',
        'НИИ', 'АО', 'ООО',
        'ИП', 'ГУП', 'МУУП',
        'НПП', 'И')

        onlyWords = [y.strip(stop_symbols) for y in source.upper().split()]
        result = [x for x in onlyWords if (x not in stop_words)]

        return delShortWords(result)

def delShortWords(words):
    return [word for word in words if len(word) > 2]

def distanceLevenshtein(text, pattern):
   text_len, pattern_len = len(text), len(pattern)

   current_column = range(pattern_len+1)
   min_value = pattern_len
   end_pos = 0
   for i in range(1, text_len+1):
      previous_column, current_column = current_column, [0]*(pattern_len+1)
      for j in range(1,pattern_len+1):
         add, delete, change = previous_column[j]+1, current_column[j-1]+1, previous_column[j-1]
         if pattern[j-1] != text[i-1]:
            change += 1
         current_column[j] = min(add, delete, change)

      if min_value > current_column[pattern_len]:
         min_value = current_column[pattern_len]
         end_pos = i

   return min_value, end_pos


def checkWords():
    distance = []
    str1 = u'ПАО Альфа банк'
    str2 = u'ОА Сберегательный банк'
    str1 = canonize(str1)
    str2 = canonize(str2)
    for s1 in str1:
        for s2 in str2:
            n1 = min(distanceLevenshtein(s1, s2))
            distance.append(n1)
            print(n1)
    dl = len(distance)
    dl2 = len([x for x in distance if x > 2])
    result = 1-dl2/dl
    print(result)

checkWords()

