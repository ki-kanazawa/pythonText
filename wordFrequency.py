def word_frequency(sentence):
    words = sentence.split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word,0)+1
        sorted_freq = sorted(freq.items() ,key=lambda x :x[1],reverse=True)
    for word,count in sorted_freq:
        print(f"{word}:{count}")

sentence = input("文章を入力してください：")
word_frequency(sentence)